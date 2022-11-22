import jarray
import random
import math
import os
from ij import IJ
from ij import ImageStack
from ij.plugin import Duplicator
from ij import ImagePlus
from ij.process import ByteProcessor
from ij.gui import GenericDialog
from org.apache.commons.math3.ml.distance import EuclideanDistance
from org.apache.commons.math3.ml.clustering import DoublePoint
from org.apache.commons.math3.ml.clustering import KMeansPlusPlusClusterer

def main():

    kMeansClusteringApp = KMeansClusteringApplication()
    if not kMeansClusteringApp.showDialog():
        return
    kMeansClusteringApp.run()
    
class KMeansClusteringApplication:

    def __init__(self):
        self.k = 2
        self.sampleRate = 0.1
        self.maxIterations = -1
        self.normalize = True
        self.lut = "glasbey"
        self.luts = IJ.getLuts()
        self.classifierName = "classifier"
        self.apply = False
        self.applyClassifierName = ""
        self.classifiers = ["None"]
        pluginsDir = IJ.getDir("plugins");
        self.classifierDir = pluginsDir + "/Clustering/"
        if not os.path.exists(self.classifierDir):
            os.makedirs(self.classifierDir) 
        storedClassifiers = [filename.split('.')[0] for filename in os.listdir(self.classifierDir) if  filename.endswith(".kmc")]
        if storedClassifiers:
            self.classifiers = storedClassifiers
            
    def showDialog(self):
        dialog = GenericDialog("k-means clustering options")
        dialog.addMessage("Training")
        dialog.addNumericField("number of classes k: ", self.k)
        dialog.addNumericField("sample rate: ", self.sampleRate)
        dialog.addNumericField("max. iterations: ", self.maxIterations)
        dialog.addChoice("lut: ", self.luts, self.lut)
        dialog.addCheckbox("normalize", self.normalize)
        dialog.addStringField("save classifier as: ", self.classifierName)
        dialog.addMessage("Apply existing Classifier")
        dialog.addCheckbox("apply classifier", self.apply)
        dialog.addChoice("classifier: ", self.classifiers, self.applyClassifierName)
        
        dialog.showDialog()
        if dialog.wasCanceled():
            return False
        self.k = int(dialog.getNextNumber())
        self.sampleRate = float(dialog.getNextNumber())
        self.maxIterations = int(dialog.getNextNumber())
        self.lut = dialog.getNextChoice()
        self.normalize = dialog.getNextBoolean()
        self.classifierName = dialog.getNextString()
        self.apply = dialog.getNextBoolean()
        self.applyClassifierName = dialog.getNextChoice()
        return True
            
    def run(self):
        if self.normalize:
            IJ.run("normalize feature stack", "")
        featureImage = IJ.getImage()
        miner = DataMiner(featureImage, self.sampleRate)
        if self.isApply():
            print("Applying classifier")
            miner.setCentroids(self.loadClassifier())
        else:
            print("Clustering")
            miner.cluster(self.k, self.maxIterations)
        labelImage = miner.createLabels()
        labelImage.show()
        IJ.run(labelImage, self.lut, "")
        labelImage.setDisplayRange(0, self.k)
        labelImage.updateAndDraw()
        if self.normalize:
            featureImage.close()
        centroids = miner.getCentroids();
        IJ.log(str(centroids))
        if not self.isApply():
            with open(self.classifierDir + self.classifierName + ".kmc", 'w') as f:
                for centroid in centroids:
                    f.write(','.join(str(e) for e in list(centroid)))
                    f.write("\n")        
        
    def isApply(self) :
        return self.apply
        
    def loadClassifier(self):
        centroids = []
        with open(self.classifierDir + self.applyClassifierName + ".kmc", 'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                centroid = line.split(',')
                centroid = jarray.array([float(v) for v in centroid], 'd')
                centroids.append(centroid)
        self.k = len(centroids)
        return centroids
        
        
class DataMiner:

    def __init__(self, image, sampleRate):
        self.image = image
        self.numberOfFeatures = image.getStack().getSize()
        self.sampleRate = sampleRate        
        self.featureVectors = self.calculateFeatureVectors()
        self.size = len(self.featureVectors)
        self.dimensions = len(self.featureVectors[0].getPoint())
        self.trainingData = []
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
        self.trainingData = self.calculateTrainingData()
        clusterer = KMeansPlusPlusClusterer(k, maxIterations)
        clusters = clusterer.cluster(self.trainingData)
        self.centroids = [c.getCenter().getPoint() for c in clusters]
        
    def getCentroids(self):
        return self.centroids
    
    def setCentroids(self, centroids):
        self.centroids = centroids
    
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
        
                
main()