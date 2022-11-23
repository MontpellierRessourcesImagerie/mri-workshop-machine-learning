from __future__ import division
import jarray
from org.apache.commons.math3.ml.distance import EuclideanDistance
from org.apache.commons.math3.ml.clustering import DoublePoint
from org.apache.commons.math3.ml.clustering import KMeansPlusPlusClusterer
from ij import IJ
from ij.process import ByteProcessor
from ij import ImagePlus

k = 2
maxIterations = -1
lut = "glasbey"

image = IJ.getImage();
stats = image.getStatistics()
counts = list(stats.getHistogram())
maxCount = max(counts)
counts = [count / maxCount for count in counts]
indices = range(0, len(counts))
indices = [index / indices[-1] for index in indices]
data = zip(indices, counts)
features = [DoublePoint(jarray.array(v, 'd')) for v in data]

clusterer = KMeansPlusPlusClusterer(k, maxIterations)
clusters = clusterer.cluster(features)
centroids = [c.getCenter().getPoint() for c in clusters]
print(centroids)

distance = EuclideanDistance()
labels = [None] * len(features)
distanceCalc = EuclideanDistance()
index = 0
for vector in features:
    distances = [distanceCalc.compute(vector.getPoint(), centroid) for centroid in centroids]
    label = distances.index(min(distances))
    labels[index] = label
    index = index + 1

processor = ByteProcessor(image.getWidth(), image.getHeight())
pixels = image.getProcessor().getPixels()
newPixels = [0] * len(pixels)

for index, pixel in enumerate(pixels):
    newPixels[index] = labels[pixel]
bytes = jarray.array(newPixels, 'b')
processor.setPixels(bytes)
labelImage = ImagePlus("labels of " + image.getTitle(), processor)
labelImage.show()
IJ.run(labelImage, lut, "")
labelImage.setDisplayRange(0, k)
labelImage.updateAndDraw()