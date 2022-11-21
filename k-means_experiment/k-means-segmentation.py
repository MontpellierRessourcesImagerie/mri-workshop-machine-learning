import jarray
import random
import math
from ij import IJ
from ij import ImageStack
from ij.plugin import Duplicator
from ij import ImagePlus
from ij.process import ByteProcessor
from org.apache.commons.math3.ml.distance import EuclideanDistance
from org.apache.commons.math3.ml.clustering import DoublePoint
from org.apache.commons.math3.ml.clustering import KMeansPlusPlusClusterer

def main():
    k = 6
    SAMPLE_RATE = 0.1
    MAX_ITERATIONS = -1
    LUT = "brgbcmyw"
    
    image = IJ.getImage()
    normalizedImage, nrOfFeatures = normalizedFeatureStack(image)
    normalizedImage.show()

    miner = DataMiner(normalizedImage, SAMPLE_RATE)
    miner.cluster(k, MAX_ITERATIONS)
    labelImage = miner.createLabels()
    labelImage.show()
    IJ.run(labelImage, LUT, "");
    labelImage.setDisplayRange(0, k);
    labelImage.updateAndDraw();
    
class DataMiner:

    def __init__(self, image, sampleRate):
        self.image = image
        self.numberOfFeatures = image.getStack().getSize()
        self.sampleRate = sampleRate        
        self.featureVectors = self.calculateFeatureVectors()
        self.size = len(self.featureVectors)
        self.dimensions = len(self.featureVectors[0].getPoint())
        self.trainingData = self.calculateTrainingData()
        self.centroids = []
    
    def createLabels(self):
        k = len(self.centroids)
        distance = EuclideanDistance()
        labels = [None] * self.size
        distanceCalc = EuclideanDistance()
        index = 0
        for vector in self.featureVectors:
            distances = [distanceCalc.compute(vector.getPoint(), centroid) for centroid in self.centroids]
            label = distances.index(min(distances)) + 1
            labels[index] = label
            index = index + 1
        processor = ByteProcessor(self.image.getWidth(), self.image.getHeight(), labels)
        labelImage = ImagePlus("labels of " + self.image.getTitle(), processor)
        return labelImage
                
    def cluster(self, k, maxIterations):
        clusterer = KMeansPlusPlusClusterer(k, maxIterations)
        clusters = clusterer.cluster(self.getTrainingData())
        self.centroids = [c.getCenter().getPoint() for c in clusters]
        
    def getCentroids(self):
        return self.centroids
    
    def calculateFeatureVectors(self):
        pixels = self.image.getStack().getImageArray()
        zipped = zip(*list(pixels)[0:self.numberOfFeatures])
        features = [DoublePoint(jarray.array(v, 'd')) for v in zipped]
        return features
        
    def calculateTrainingData(self):
        trainingData = random.sample(self.featureVectors, int(math.floor(self.sampleRate * self.size)))
        return trainingData
        
    def getSampleRate(self):
        return self.sampleRate
        
    def setSampleRate(self, rate):
        self.sampleRate = rate
        
    def getTrainingData(self):
        return self.trainingData
        
    def plot(self, combinations):
        pass
        
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