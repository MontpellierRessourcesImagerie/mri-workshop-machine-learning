---
title: "Untitled"
subtitle    : Supervised learning
author      : Cédric Hassen-Khodja, Volker Baecker, Jean-Bernard Fiche, Francesco Pedaci
url         : {lib: /home/cedric/Documents/ML_FormationBC/mydeck}
framework   : io2012        # {io2012, html5slides, shower, dzslides, ...}
highlighter : highlight.js  # {highlight.js, prettify, highlight}
hitheme     : tomorrow      # 
widgets     : mathjax            # {mathjax, quiz, bootstrap}
mode        : selfcontained # {standalone, draft}
knit        : slidify::knit2slides
output: beamer_presentation
---

## History of SVM

1. <span style="color:#ee7600">1963</span>: Linear classifier - Maximal Margin Classifier by Vapnik and 	Chervonenkis.
2. <span style="color:#ee7600">1992</span>: Nonlinear classification – Kernel trick by Bernhard E. Boser.
3. <span style="color:#ee7600">1995</span>: The Soft Margin Classifier by Corinna Cortes and Vapnik.

---

## Types of Machine Learning
![plot of chunk unnamed-chunk-1](assets/fig/unnamed-chunk-1-1.png)

---

## What is support vector machine ?

Support vector machines (SVMs) aim to find a decision <span style="color:#ee7600">hyperplane</span> that separates data points of different classes with a <span style="color:#ee7600">maximal margin</span>.

---

## How does it work ?
We are given a set of people with different:
  
Height | Weight | Sex
------ | ------ | ----
145    | 55     | Woman
155    | 50     | Woman
160    | 52     | Woman
158    | 68     | Woman
174    | 74     | Man
170    | 86     | Man
180    | 62     | Man
185    | 78     | Man

---

## How does it work ?
![](/home/cedric/Documents/ML_FormationBC/mydeck/plot_SVM.png)

---

## How does it work ?
Let's add a new data point and figure out if it's a man or woman.
![](/home/cedric/Documents/ML_FormationBC/mydeck/plot_SVM_2.png)

---

## How does it work ?
### Maximize the margin 
We can split our data by choosing any of these lines.
![](/home/cedric/Documents/ML_FormationBC/mydeck/plot_SVM_3.png)

---

## How does it work ?
### Maximize the margin 

To predict the gender of a new data point we should split the data in the best possible way.
![](/home/cedric/Documents/ML_FormationBC/mydeck/plot_SVM_3.png)

---

## How does it work ?
### Maximize the margin 
This red / blue line has the maximum space that separates the two classes.
![](/home/cedric/Documents/ML_FormationBC/mydeck/lines.png)



---

## How does it work ?
### Maximize the margin 
While the others lines (black / green) doesn't have the maximum space that separates the two classes.
![](/home/cedric/Documents/ML_FormationBC/mydeck/lines_2.png)



---

## How does it work ?
### Maximize the margin 
We can also say that the distance between the support and the line should be far as possible. Where support vectors are the extreme points in the datasets and *hyperplane* has the maximum distance to the support vectors of any class. Based on the distance margin we can say the new data point belongs to woman gender.

<img src="/home/cedric/Documents/ML_FormationBC/mydeck/plot_SVM_6.png" title="plot of chunk unnamed-chunk-2" alt="plot of chunk unnamed-chunk-2" width="459px" height="320px" />

---

## How does it work ?
### Soft Margin 

If we select a hyperplane having low margin then there is high chance of misclassification.
![](/home/cedric/Documents/ML_FormationBC/mydeck/cost_function.png)

---

## How does it work ?
### Kernel trick

![](/home/cedric/Documents/ML_FormationBC/mydeck/plot_SVM_8.png)

it's necessary to move away from a 1-D view of the data to a 2-D view. For the transformation we use a *kernel* function.    

![](/home/cedric/Documents/ML_FormationBC/mydeck/plot_SVM_9.png)

---

## How does it work ?
### Kernel trick

![](/home/cedric/Documents/ML_FormationBC/mydeck/plot_SVM_10.png)

---

## How does it work ?
### Kernel trick

How to perform SVM for this type of dataset ?

![](/home/cedric/Documents/ML_FormationBC/mydeck/plot_SVM_11.png)

---

## How does it work ?
### Kernel trick
![](/home/cedric/Documents/ML_FormationBC/mydeck/plot_SVM_13.png)

---

## SVM in practice - Implementing biological application with Python
### Use Case - Problem Statement
Estimate the lowest dose necessary to induce the cytoplasm to nucleus translocation of the 
FKHR-EGFP in U2OS (osteosarcoma cell line).

<img src="/home/cedric/Documents/ML_FormationBC/mydeck/workflow.png" title="plot of chunk unnamed-chunk-3" alt="plot of chunk unnamed-chunk-3" width="759px" height="406px" />

---

### Use Case - Translocation Activity

#### Importing libraries

![](/home/cedric/Documents/ML_FormationBC/mydeck/import_librairies.png)

#### Importing the dataset

![](/home/cedric/Documents/ML_FormationBC/mydeck/importing_dataset.png)

---

### Use Case - Translocation Activity

#### Preprocessing

![](/home/cedric/Documents/ML_FormationBC/mydeck/preprocessing.png)

#### Split Data

![](/home/cedric/Documents/ML_FormationBC/mydeck/split_dataset.png)

---

### Use Case - Translocation Activity

#### Training the Model on the training data

Scikit-Learn contains the *SVC* library, which contains built-in classes for different SVM algorithms. In the case of a simple SVM we simply set this parameter as "linear" since simple SVMs can only classify linearly separable data.  
The fit method of SVC class is called to train the algorithm on the training data, which is passed as a parameter to the fit method.

![](/home/cedric/Documents/ML_FormationBC/mydeck/train_dataset.png)

---


### Use Case - Translocation Activity

#### feature importance

---

### Use Case - Translocation Activity

#### Prediction on the test data

![](/home/cedric/Documents/ML_FormationBC/mydeck/predict.png)

---

#### Evaluating the Model

![](/home/cedric/Documents/ML_FormationBC/mydeck/evaluate_model.png)

---

### Use Case - Translocation Activity

#### Prediction on the unlabelled dataset

<img src="/home/cedric/Documents/ML_FormationBC/mydeck/unlabeled.png" title="plot of chunk unnamed-chunk-4" alt="plot of chunk unnamed-chunk-4" width="975px" height="530px" />

---

### Use Case - Translocation Activity

#### Prediction on the unlabelled dataset

![](/home/cedric/Documents/ML_FormationBC/mydeck/features.png)

---

### Use Case - Translocation Activity

#### Prediction on the unlabelled dataset

<img src="/home/cedric/Documents/ML_FormationBC/mydeck/check_prediction.png" title="plot of chunk unnamed-chunk-5" alt="plot of chunk unnamed-chunk-5" width="975px" height="530px" />

---

### Use Case - Translocation Activity
#### Model Accuracy
        
$$
$$
$Accuracy = (\frac{Count Positives Cells}{Count Total Cells})*100$
$$
$$
$Accuracy = (\frac{18}{20}*100)$
$$
$$
$Accuracy = 90$%

---

---

## History of Random Forest

1. <span style="color:#ee7600">1998</span>: Ho has written a number of papers on "the random subspace" method which does a random selection of a subset of features to use to grow each tree.
2. <span style="color:#ee7600">1997</span>: In an important paper on written character recognition, Amit and Geman define a large number of geometric features and search over a random selection of these for the best split at each node.
3. <span style="color:#ee7600">2001</span>: The introduction of random forests proper was first made in a paper by Leo Breiman. This paper describes a method of building a forest of uncorrelated trees using a CART like procedure, combined with randomized node optimization and bagging.

---

## Types of Machine Learning
![plot of chunk unnamed-chunk-6](assets/fig/unnamed-chunk-6-1.png)

---

## Why Random Forest ?
<b>Overfitting</b>:    
* Number of trees increase
* Training time is less   

<b>Accuracy</b>:
* Run efficiently on large database

<b>Missing data</b>:
* Accuracy when large proportion of data is missing

---

## What is Random Forest ?

<p> Random Forest creates multiple Decision Trees during training phase.    
The Decision of the majority of the trees is chosen by the random forest as the final decision. </p>

<img src="/home/cedric/Documents/ML_FormationBC/mydeck/what_RF.png" title="plot of chunk unnamed-chunk-7" alt="plot of chunk unnamed-chunk-7" width="1061px" height="388.443px" />

---

## Decision Tree
<p>Decision Tree is a tree shaped diagram. Each branch of the tree is an action 
and each node as a result of the decision taken.</p>

<img src="/home/cedric/Documents/ML_FormationBC/mydeck/DT_1.png" title="plot of chunk unnamed-chunk-8" alt="plot of chunk unnamed-chunk-8" width="385.577px" height="500px" />

---

## Decision Tree - Entropy

<img src="/home/cedric/Documents/ML_FormationBC/mydeck/DT_2.png" title="plot of chunk unnamed-chunk-9" alt="plot of chunk unnamed-chunk-9" width="953.289px" height="600px" />

---

## Decision Tree - Entropy

<img src="/home/cedric/Documents/ML_FormationBC/mydeck/DT_3.png" title="plot of chunk unnamed-chunk-10" alt="plot of chunk unnamed-chunk-10" width="1066px" height="260.140px" />

---

## Decision Tree

<img src="/home/cedric/Documents/ML_FormationBC/mydeck/DT_4.png" title="plot of chunk unnamed-chunk-11" alt="plot of chunk unnamed-chunk-11" width="1066px" height="531.235px" />

---

## Decision Tree - Information Gain

<img src="/home/cedric/Documents/ML_FormationBC/mydeck/DT_5.png" title="plot of chunk unnamed-chunk-12" alt="plot of chunk unnamed-chunk-12" width="920.956px" height="573.500px" />

---

## Decision Tree - Information Gain

<img src="/home/cedric/Documents/ML_FormationBC/mydeck/DT_6.png" title="plot of chunk unnamed-chunk-13" alt="plot of chunk unnamed-chunk-13" width="1005.65px" height="520px" />

---

## Decision Tree - Leaf node / Decision node

![](/home/cedric/Documents/ML_FormationBC/mydeck/DT_26.png)

---

## Decision Tree - Leaf node / Decision node

<img src="/home/cedric/Documents/ML_FormationBC/mydeck/DT_7.png" title="plot of chunk unnamed-chunk-14" alt="plot of chunk unnamed-chunk-14" width="651.359px" height="570.037px" />

---

## Decision Tree - Root node

<img src="/home/cedric/Documents/ML_FormationBC/mydeck/DT_8.png" title="plot of chunk unnamed-chunk-15" alt="plot of chunk unnamed-chunk-15" width="945px" height="590px" />

---

## Decision Tree - Root node

<img src="/home/cedric/Documents/ML_FormationBC/mydeck/DT_9.png" title="plot of chunk unnamed-chunk-16" alt="plot of chunk unnamed-chunk-16" width="573px" height="487px" />

---

## How Does a decision tree work ?

![](/home/cedric/Documents/ML_FormationBC/mydeck/DT_10.png)

---

## How Does a decision tree work ?

![](/home/cedric/Documents/ML_FormationBC/mydeck/DT_11.png)

---

## How Does a decision tree work ?

![](/home/cedric/Documents/ML_FormationBC/mydeck/DT_12.png)

---

## How Does a decision tree work ?

![](/home/cedric/Documents/ML_FormationBC/mydeck/DT_13.png)

---

## How Does a decision tree work ?

![](/home/cedric/Documents/ML_FormationBC/mydeck/DT_14.png)

---

## How Does a decision tree work ?

![](/home/cedric/Documents/ML_FormationBC/mydeck/DT_15.png)

---

## How Does a decision tree work ?

![](/home/cedric/Documents/ML_FormationBC/mydeck/DT_16.png)

---

## How Does a random forest work ?

![](/home/cedric/Documents/ML_FormationBC/mydeck/DT_17.png)

---

## How Does a random forest work ?

![](/home/cedric/Documents/ML_FormationBC/mydeck/DT_18.png)

---

## How Does a random forest work ?

![](/home/cedric/Documents/ML_FormationBC/mydeck/DT_19.png)

---

## How Does a random forest work ?

![](/home/cedric/Documents/ML_FormationBC/mydeck/DT_20.png)

---

## How Does a random forest work ?

![](/home/cedric/Documents/ML_FormationBC/mydeck/DT_21.png)

---

## How Does a random forest work ?

![](/home/cedric/Documents/ML_FormationBC/mydeck/DT_22.png)

---

## How Does a random forest work ?

![](/home/cedric/Documents/ML_FormationBC/mydeck/DT_23.png)

---

## How Does a random forest work ?

![](/home/cedric/Documents/ML_FormationBC/mydeck/DT_24.png)

---

## How Does a random forest work ?

![](/home/cedric/Documents/ML_FormationBC/mydeck/DT_25.png)

---

## RF in practice - Implementing biological application with Python
### Use Case - Problem Statement
Estimate the lowest dose necessary to induce the cytoplasm to nucleus translocation of the 
FKHR-EGFP in U2OS (osteosarcoma cell line).

<img src="/home/cedric/Documents/ML_FormationBC/mydeck/workflow.png" title="plot of chunk unnamed-chunk-17" alt="plot of chunk unnamed-chunk-17" width="759px" height="406px" />

### Use Case - Translocation Activity

#### Importing libraries

![](/home/cedric/Documents/ML_FormationBC/mydeck/import_librairies.png)

#### Importing the dataset

![](/home/cedric/Documents/ML_FormationBC/mydeck/importing_dataset.png)

---

### Use Case - Translocation Activity

#### Preprocessing

![](/home/cedric/Documents/ML_FormationBC/mydeck/preprocessing.png)

#### Split Data

![](/home/cedric/Documents/ML_FormationBC/mydeck/split_dataset.png)

---

### Use Case - Translocation Activity

#### Training the Model on the training data

Scikit-Learn contains the *RandomForestClassifier* library. In this case we set two parameters n_jobs for parallelization task and random_state for get reproducible results.
The fit method of RandomForestClassifier class is called to train the algorithm on the training data, which is passed as a parameter to the fit method.

![](/home/cedric/Documents/ML_FormationBC/mydeck/rf_train.png)

---

### Use Case - Translocation Activity

#### feature importance

---

### Use Case - Translocation Activity

#### Prediction on the test data

![](/home/cedric/Documents/ML_FormationBC/mydeck/rf_predict.png)

---

#### Evaluating the Model

![](/home/cedric/Documents/ML_FormationBC/mydeck/evaluate_rfmodel.png)

---

### Use Case - Translocation Activity

#### Prediction on the unlabelled dataset

<img src="/home/cedric/Documents/ML_FormationBC/mydeck/unlabeled.png" title="plot of chunk unnamed-chunk-18" alt="plot of chunk unnamed-chunk-18" width="975px" height="530px" />

---

### Use Case - Translocation Activity

#### Prediction on the unlabelled dataset

![](/home/cedric/Documents/ML_FormationBC/mydeck/features.png)

---

### Use Case - Translocation Activity

#### Prediction on the unlabelled dataset

![](/home/cedric/Documents/ML_FormationBC/mydeck/check_prediction2.png)

---

### Use Case - Translocation Activity
#### Model Accuracy
        
$$
$$
$Accuracy = (\frac{Count Positives Cells}{Count Total Cells})*100$
$$
$$
$Accuracy = (\frac{16}{20}*100)$
$$
$$
$Accuracy = 80$%

---

## Machine Learning in Bioimage

<img src="/home/cedric/Documents/ML_FormationBC/mydeck/pipelineML.png" title="plot of chunk unnamed-chunk-19" alt="plot of chunk unnamed-chunk-19" width="750px" height="560.498px" />

---

## Machine Learning in Bioimage

<img src="/home/cedric/Documents/ML_FormationBC/mydeck/classification_supervised.png" title="plot of chunk unnamed-chunk-20" alt="plot of chunk unnamed-chunk-20" width="750px" height="555.653px" />

---

## Machine Learning in Bioimage

<img src="/home/cedric/Documents/ML_FormationBC/mydeck/implementing_optimization_ML.png" title="plot of chunk unnamed-chunk-21" alt="plot of chunk unnamed-chunk-21" width="750px" height="557.469px" />

---

