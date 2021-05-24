## Machine Learning for <br>Bio-Image-Analysis

<img    width="250" height="250" src="./pics/circuit_board.png">

10.05.2021

Volker Bäcker, Jean-Bernard Fiche, <br>Cedric Hassen Khodja, Francesco Pedaci

***

### Introduction

<div style="float: right;">
<div style="float: top;">
<img       width="200" height="200" src="./pics/Abstract-Brain-Line-Art.png">
</div>
<div style="float: bottom;">
<img   style="float: bottom;"  width="200" height="200" src="./pics/circuit_board.png">
</div>
</div>
<div tyle="float: left;">
- What is bio-image analysis?

- How is it done without machine <br>
learning?

- What is machine learning?

- How is bio-image analysis done <br>
with machine learning?
</div>

***
<section>
### Bio-Image-Analysis

“The extraction of information from digital images in the context of biological research”

![](./pics/bio-image-analysis.png)

***

#### The Image-Analysis Workflow

<img src="./pics/workflow.jpg" width=’1024’>

***

#### Select a scale
<small>

- Use “Gaussian blur”-filter to select a scale
    - Low-pass filter
    - Removes high frequencies from the image
        - The higher sigma, the lower the remaining frequencies

<img style="float: left;" src="./pics/gauss-sigma.png" width="300">
<img style="float: right;" src="./pics/gauss3D.png" width="300">
</small>

***

### Convolution

<div style="float: right">
<img src="./pics/convolution.png" width="300">
</div>
<div style="float: left">
<img src="./pics/eye_in.png" width="200">
<img src="./pics/eye_out.png" width="200">
</div>
<div style="float: top">
<img  src="./pics/conv_formula.jpg" width="600">
</div>

***

#### Features at different scales

<table>
<tr style="align: center">
<th  style="text-align: center; vertical-align: middle;">feature</th>
<th style="text-align: center; vertical-align: middle;">σ=3.5</th>
<th style="text-align: center; vertical-align: middle;">σ=7.0</th>
<th style="text-align: center; vertical-align: middle;">σ=10.</th>
</tr>
<tr>
<td  style="text-align: center; vertical-align: middle;">variance</td><td><img src="./pics/variance01.png" width=200></td><td><img src="./pics/variance02.png" width=200></td><td><img src="./pics/variance03.png" width=200></td>
</tr>
<tr>
<td  style="text-align: center; vertical-align: middle;">sobel</td><td><img src="./pics/sobel01.png"></td><td><img src="./pics/sobel02.png"></td><td><img src="./pics/sobel03.png"></td>
</tr>
</table>

</section>

***

<section>

### Machine Learning

Machine learning algorithms build a mathematical model of sample data, known as ”training data”, in order to make predictions or decisions without being explicitly programmed to perform the task.

<img style="float: center;" src="./pics/ml.png" width="300">

***

#### Machine Learning phases

<div>
<img style="float: left;" src="./pics/brain-train.png" width="150">

-  training
    - a model is learned from training data
</div>
<br>
<div>
<img style="float: right;" src="./pics/jean-victor-balin-green-tick.png" width="150">

- validation
    - the trained model is validated <br>against test data
</div>
<div>
<img style="float: left;" src="./pics/fortune-teller.png" width="200">

- application
    - use the trained model to <br>make predictions on new data

***

#### Machine Learning vocabulary

<small>
<table>
<tr><td>
<img style="float: left;" src="./pics/molumen-woman-eyes.png" width="300">
</td>
<td>
- supervised
    - a model is learned from pairs of input and output data
</td>
<td><img style="float: left;" src="./pics/blindfoldman.png" width="300"></td>
<td>
- unsupervised
    - a model is learned from the inherent structure of the input data alone
</td></tr>
<tr><td><img style="float: left;" src="./pics/TJ-Openclipart-71-remixed-office-stationery-file-sticky-notes-assorted-25-5-16.png" width="300"></td><td>
- classification
    - the result is a category 
</td><td><img style="float: left;" src="./pics/Linear Regression.png" width="300"></td><td>
- regression
    - the result is a real number
</td></tr>
</table>
</small>

***

#### Machine Learning - <br>How is that even possible?

<img style="float: right;" src="./pics/pgb-chip-math.png" width="200">

- ML algorithm implements a <br>mathematical model with a number <br>of model parameters

- given the training data, <br>find parameter values that minimize <br>the prediction error

***

#### Machine Learning Example 1 <br> Linear Regression

<img style="float: left; margin-right: 20px; margin-bottom: 10px;" src="./pics/Femur_-_animation9.gif" width="200">

<div style="float: right; margin-left: 20px;">
<small>
Training Data:

| Femur length (cm) | Height (cm) |
|-------------------|-------------|
| 45                | 153         |
| 44                | 168         |
| 44                | 177         |
| 47                | 180         |
| 44                | 171         |
| 50                | 168         |

</small>
</div>
estimate body height f(x) given the femur length x.

model: f(x) = &omega;<sub>1</sub> + &omega;<sub>2</sub> &times; x

parameter of the model: <br>&nbsp;&omega;<sub>1</sub> and &omega;<sub>2</sub>

***

#### Machine Learning Example 1 <br> Linear Regression

<img  style="float: right;" src="./pics/linear-regression-femur.png" width="600">

<small>

- find parameters <br>ω1, ω2 

- so that error <br>between <br>training data <br>and model <br>is minimal 

</small>

***

#### Example 1 - Squared Loss function

<img src="./pics/loss_plot.png" style="float: right;" width="200">

<img src="./pics/linear-regression-femur.png" style="float: right;" width="200">

<img src="./pics/linear.png">

<img src="./pics/loss.png">

***

#### Example 1 - Gradient descent

<img src="./pics/gradient_descent.png" style="float: right;" width="400">

- find the minimum of <br>the loss function

- by using gradient <br>descent

***

#### Example 1 - Predictions

<img src="./pics/predictions.png" style="float: right;">

<div style="text-align: left; font-size: 32px;">

f(x) = &omega;<sub>1</sub> + &omega;<sub>2</sub> &times; x 

&omega;<sub>1</sub> = 131.13cm

&omega;<sub>2</sub> = 0.87

f(55cm) = 131.13cm + 0.87 &times; 55cm

f(55cm) = 179.42cm

</div>

***

#### Femur example

- Supervised or Unsupervised?

- Classification or Regression?

</section>

***

### The programs

<div style="text-align: left">

<img src="./pics/fiji.png" style="float: right;" width="80">

- ImageJ/FIJI 

<img src="./pics/weka.png" style="float: right;" width="80">

- Weka / Labkit

<img src="./pics/ilastik.png" style="float: right;" width="80">

- Ilastik

<img src="./pics/cellprofiler.png" style="float: right;" width="80">

- Cellprofiler / CP Analyst

<img src="./pics/orbit.png" style="float: right;" width="80">

- Orbit

</div>

***

<section>

### ImageJ/FIJI

- Demo ImageJ 01
    - Open Image
    - Threshold
    - Binary Watershed
    - Compare to GT

***

### ImageJ/FIJI

- Demo ImageJ 02
    - Revert Image
    - Laplacian of Gaussian (scale 3)
    - Threshold (Yen)
    - Binary Watershed
    - Compare to GT

***

### Ilastik

- Demo Ilastik
    - import image(s)
    - select features and scales
    - name classes
    - select training data
    - export result
    - batch

***

### Exercises 01

</section>

***

<section>

### Clustering

- A machine learning method

    - Unsupervised
    
    -  Classification

***

### Clustering

<div style="font-size: 32px;">

<img src="./pics/clustering.png" style="float: right;" width="300">

- Clustering 

    - Group objects in a way that 

        - objects in the same cluster are <br>more similar to each other

        - than to objects in other clusters

</div>

***

### Clustering algorithms

- K-means
- DBScan
- hierarchical clustering
- expectation-maximization 
- ...

***

### k-means clustering

<div style = "float: right; font-size: 28px;">
- Algorithm:
    - Start with k initial means
    - Repeat until convergence
        - Assign feature-vectors to clusters
        - Recalculate the means of the clusters
</div>
<div style = "float: left; font-size: 32px;" >
- Partition the feature-<br>space into k-clusters

- Each feature-vector <br>belongs to the cluster <br>with nearest mean
<div>

***

### K-means example

<img src="./pics/k-means.png" width="500">

***

### K-means clustering in <br>machine learning

<div style = "float: right; font-size: 30px;" >
- Classification of unknown data:

    - calculate the feature vector

    - assign it to the cluster <br>with the nearest mean
</div>
<div style = "float: left; font-size: 30px;">
- Training phase:

    - randomly select a number of <br>feature vectors

        - for example 5% of the data	

    - run the k-means clustering on <br>the selected feature vectors

    - the resulting means are the <br>classifier
</div>

***

### Classify pixels by color

<div align= "center">

<div style = "float: right;" width = "400" >

- RGB

<img src="./pics/rgb.png">

</div>

<div style = "float: left;" width="400" >

- input image

<img src="./pics/plant.png">

</div>

</div>

***

### CIEL\*a\*b\* color-space

<img src="./pics/cielab.png" style="float: right;" width="300">

<div style="font-size: 30px;">
- CIEL*a*b* color-space
    - L = lightness
    - a = green (-) to red (+)
    - b = yellow (-) to blue (+)
<br>
<br>
- Designed, so that 
    - distances correspond to perceived <br>distances between colors.
</div>

***

### Software

- color clustering in FIJI
- comes with WEKA
- Plugins>Segmentation>Color Clustering

<img src="./pics/color-clustering.png" style="float: bottom;" width="400">

***

### Exercises 02

</section>