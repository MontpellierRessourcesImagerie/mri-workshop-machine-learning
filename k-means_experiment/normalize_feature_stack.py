from ij import IJ
from ij import ImageStack
from ij import ImagePlus
from ij.plugin import Duplicator

def main():
    image = IJ.getImage()
    normalizedImage, _ = normalizeFeatureStack(image)
    normalizedImage.show()
    
def normalizeFeatureStack(imp):
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