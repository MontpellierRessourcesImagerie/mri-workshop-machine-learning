import jarray
import random
import math
from ij import IJ
from ij import ImageStack
from ij.plugin import Duplicator
from ij import ImagePlus
from org.apache.commons.math3.ml.clustering import DoublePoint

def main():
    k = 2
    SAMPLE_RATE = 0.1
    
    imp = IJ.getImage()
    normImp, nrOfFeatures = normalizedFeatureStack(imp)
    normImp.show()

    pixels = normImp.getStack().getImageArray()
    zipped = zip(*list(pixels)[0:nrOfFeatures])
    features = [DoublePoint(jarray.array(v, 'd')) for v in zipped]
    trainingData = random.sample(features, int(math.floor(SAMPLE_RATE * len(features))))
    print(trainingData[0:3])
    
    
def normalizedFeatureStack(imp):
    stack = imp.getStack()
    nrOfFeatures = stack.getSize()
    normStack = ImageStack()
    for i in range(1, nrOfFeatures+1):
        impSlice = Duplicator().run(imp, i, i, 1, 1, 1, 1);
        impSlice.show()
        IJ.run("16-bit")
        IJ.run("Enhance Contrast...", "saturated=0.35 equalize")
        IJ.run("32-bit")
        IJ.run("Divide...", "value=65535 stack")
        normStack.addSlice("f" + str(i), impSlice.getProcessor())
        impSlice.changes = False
        impSlice.close()      
    normImp = ImagePlus("normalized features", normStack)
    IJ.resetMinAndMax(normImp)
    return normImp, nrOfFeatures;
    
main()