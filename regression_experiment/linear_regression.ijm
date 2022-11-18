DIR_X = newArray(-1, -0.5, 0, 0.5, 1, -1, -0.5, 0, 0.5, 1, -1, -0.5, 0, 0.5, 1, -1, -0.5, 0, 0.5, 1, -1, -0.5, 0, 0.5, 1);
DIR_Y = newArray(-1, -1, -1, -1, -1, -0.5, -0.5, -0.5, -0.5, -0.5, 0, 0, 0, 0, 0, 0.5, 0.5, 0.5, 0.5, 0.5, 1, 1, 1, 1, 1);
table = "Plot Values";
XColumn = "femur_length_[cm]";
YColumn = "height_[cm]";
X = Table.getColumn(XColumn, table);
Y = Table.getColumn(YColumn, table);
WIDTH = 512;
HEIGHT = 512;

/*
w = fitLine(X, Y);
loss = meanSquaredLoss(w, X, Y);
print("w1=" + w[0] + ", w2=" + w[1] + ", loss=" + loss);
Plot.create("Regression Line", XColumn, YColumn);
Plot.add("cross", X, Y);
Plot.drawLine(X[0], w[0] + (w[1] * X[0]), X[X.length-1], w[0] + (w[1] * X[X.length - 1]));
Plot.show();
*/
lossImage(WIDTH, HEIGHT, 0.5, 0.025, X, Y);
waitForUser("Select a point!");
Roi.getCoordinates(xpoints, ypoints);
w1 = xpoints[0];
w2 = ypoints[0];
toScaled(w1, w2);
gradientDescent(w1, w2, 0.5, 0.025, 20, X, Y);

function fitLine(X, Y) {
    Array.getStatistics(X, min, max, XMean, stdDev);
    Array.getStatistics(Y, min, max, YMean, stdDev);
    deltaX = newArray(X.length);
    deltaXSquared = newArray(X.length);
    deltaY = newArray(Y.length);
    deltaXTimesDeltaY = newArray(Y.length);
    sumDeltaXTimesDeltaY = 0;
    sumDeltaXSquared = 0;
    for (i = 0; i < X.length; i++) {
        deltaX[i]            = X[i] - XMean;
        deltaXSquared[i]     = deltaX[i] * deltaX[i];
        deltaY[i]            = Y[i] - YMean;
        deltaXTimesDeltaY[i] = deltaX[i] * deltaY[i];
        sumDeltaXTimesDeltaY = sumDeltaXTimesDeltaY + deltaXTimesDeltaY[i];
        sumDeltaXSquared     = sumDeltaXSquared + deltaXSquared[i];
    }
    slope = sumDeltaXTimesDeltaY / sumDeltaXSquared;
    yIntercept = YMean - (slope * XMean);
    return newArray(yIntercept, slope);
}

function meanSquaredLoss(w, X, Y) {
    squaredLoss = newArray(X.length);
    sumOfSquaredLoss = 0;
    for (i = 0; i < X.length; i++) {
        squaredLoss[i] = Math.sqr(Y[i] - (w[0] + (w[1] * X[i])));
        sumOfSquaredLoss = sumOfSquaredLoss + squaredLoss[i];
    }
    result = sumOfSquaredLoss / X.length;
    return result;
}

function lossImage(width, height, stepW1, stepW2, X, Y) {
    newImage("loss", "32-bit", width, height, 1);
    imageID = getImageID();
    selectImage(imageID);
    run("Properties...", "channels=1 slices=1 frames=1 pixel_width="+stepW1+" pixel_height="+stepW2+" voxel_depth=1.0000 origin="+(width/2)+","+(height/2) + " invert");
    for (x = 0; x < width; x++) {
        for (y = 0; y < height; y++) {
            xS = x;
            yS = y;
            toScaled(xS, yS);
            v = meanSquaredLoss(newArray(xS, yS), X, Y);
            setPixel(x, y, v);
        }   
    }
    run("Fire");
    resetMinAndMax();
}

function gradientDescent(w1Start, w2Start, scaleW1, scaleW2, stepWidth, X, Y) {
    w1Points = newArray(0);
    w2Points = newArray(0);
    atBottom = false;
    w1 = w1Start;
    w2 = w2Start;
    maxSteps = 2000;
    step = 0
    minValue = 999999999999999999999;
    while(!atBottom && (step < maxSteps)) {      
        w1Points = Array.concat(w1Points, w1);
        w2Points = Array.concat(w2Points, w2);
        value = meanSquaredLoss(newArray(w1, w2), X, Y);
        bestW1 = w1;
        bestW2 = w2;
        bestDir = -1;
        for (d = 0; d < DIR_X.length; d++) {
            w1n = w1 + DIR_X[d] * stepWidth * scaleW1;
            w2n = w2 + DIR_Y[d] * stepWidth * scaleW2;
            neighborValue = meanSquaredLoss(newArray(w1n, w2n), X, Y);
            if ((neighborValue < value) && (neighborValue < minValue)) {
                minValue = neighborValue;
                bestDir = d;               
                bestW1 = w1n;
                bestW2 = w2n;
            }
        }
        if (bestDir == -1 && stepWidth<=1) {
            atBottom = true;
            print(minValue, "at bottom", stepWidth);
        }
        else {
            w1 = bestW1;
            w2 = bestW2;
            print("loss: ", minValue, "step width: ", stepWidth);
            if (stepWidth>1) stepWidth = stepWidth - 0.1;
        }
        step++;
    }
    xpoints = newArray(w1Points.length);
    ypoints = newArray(w2Points.length);
    for (i = 0; i < xpoints.length; i++) {
        x = w1Points[i];
        y = w2Points[i];
        toUnscaled(x, y);
        xpoints[i] = x;
        ypoints[i] = y;
    }
    print("w1=" + w1Points[w1Points.length-1] + ", w2=" + w2Points[w2Points.length-1]);
    makeSelection("polyline", xpoints, ypoints);
    Overlay.addSelection;
    makeOval(xpoints[xpoints.length - 1] - 1, ypoints[ypoints.length - 1] - 1, 3, 3);
    Overlay.addSelection;
}
