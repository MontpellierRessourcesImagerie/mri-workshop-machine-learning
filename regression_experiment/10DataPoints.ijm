femurLength = newArray(40, 45, 32, 50, 37, 41, 30, 34, 47, 45);
height = newArray(170, 183, 151, 195, 162, 174, 141, 151, 185, 182);

ranks = Array.rankPositions(femurLength);

orderedFemurLength = newArray(femurLength.length);
orderedHeight = newArray(femurLength.length);

for (i = 0; i < ranks.length; i++) {
    orderedFemurLength[i] = femurLength[ranks[i]];
    orderedHeight[i] = height[ranks[i]];
}


Plot.create("height by femur length", "femur length [cm]", "height [cm]");
Plot.add("x", orderedFemurLength, orderedHeight);
Plot.setStyle(0, "black,none,2.0,X");
Plot.show();