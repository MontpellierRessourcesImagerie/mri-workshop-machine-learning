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

</section>



