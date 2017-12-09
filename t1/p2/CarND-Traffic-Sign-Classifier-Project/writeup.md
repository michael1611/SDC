# **Traffic Sign Recognition** 

[//]: # (Image References)

[signs]: ./images/signs.JPG "Signs"
[bar_chart]: ./images/bar_chart.JPG "Visualization"
[preprocessed]: ./images/preprocessed.JPG "Preprocessed"
[rotated]: ./images/rotated.JPG "Rotated"
[german_labels]: ./images/german_labels.JPG "German Traffic Signs"
[german_predictions]: ./images/german_predictions.JPG "German Traffic Signs Predictions"
[top_5_probs]: ./images/top_5_probs.JPG "German Traffic Signs Predictions Top 5"

**Build a Traffic Sign Recognition Project**

The goals / steps of this project are the following:

* Load the data set (see below for links to the project data set)
* Explore, summarize and visualize the data set
* Design, train and test a model architecture
* Use the model to make predictions on new images
* Analyze the softmax probabilities of the new images
* Summarize the results with a written report


![Space for Traffic Signs Image][signs]



## Rubric Points
### Here I will consider the [rubric points](https://review.udacity.com/#!/rubrics/481/view) individually and describe how I addressed each point in my implementation.  

---
### Writeup / README


You're reading it! and here is a link to my [project code](https://github.com/michael1611/sdc/blob/master/t1/p2/CarND-Traffic-Sign-Classifier-Project/Traffic_Sign_Classifier.ipynb).

### Files and Folders

<b> Traffic\_Sign\_Classifier.ipynb: </b> This notebook contains all the code.

<b> lenet.*</b>(wildcard)<b>:</b> These are saved model files.

<b> signnames.csv: </b> This file contains traffic sign name to label mapping.

<b> German Traffic Signs: </b> Folder containing german traffic signs downloaded from net for testing.

### Data Set Summary & Exploration

#### 1. Data Statistics

I used the pandas library to calculate summary statistics of the traffic
signs data set:

* The size of training set is 34799.
* The size of the validation set is 4410.
* The size of test set is 12630.
* The shape of a traffic sign image is (32, 32, 3).
* The number of unique classes/labels in the data set is 43.

#### 2. Exploratory visualization of the dataset.

Here is an exploratory visualization of the data set. It is a bar chart showing types of signs vs number of samples of that sign in the dataset.

![Sign types vs #Samples][bar_chart]

### Design and Test a Model Architecture

#### 1. Data Preprocessing

* As a first step, We resize the input image to (32, 32, 2) if not already so because our model expects the input image shape to be the Height and width to be (32, 32).
* Second, I covert the image to grayscale as working with grayscale images is faster than working with colored images.
* Third, I observed that some of the imput images are not clear so I sharpened the image using the kernel ([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]]).
* Fourth, I normalize the image to have 0 mean and equal variance using the formula (pixel_value - mean)/ mean. Note: normally mean is 128.
* Last but not the least, I shuffle the data because mini-batch training works best with shuffled data.

Here are some preprocessed images:

![Space to show preprocessed images][preprocessed]

I decided to generate additional data because the initial accuracy I got with the original data was not too good, the number of samples were too less for some signs and I thought it is a good idea to train the model with slightly tilted images as some images may contain slightly rotated traffic signs in real life as well.

Here is an example of an original image and a rotated image:

![Space to show rotated image][rotated]


#### 2. Describe what your final model architecture looks like including model type, layers, layer sizes, connectivity, etc.) Consider including a diagram and/or table describing the final model.

My final model consisted of the following layers:

| Layer         		|     Description	        					| 
|:---------------------:|:---------------------------------------------:| 
| Input         		| 32x32x1 grayscale image   							| 
| Convolution     	| 1x1 stride, same padding, outputs 28x28x6	|
| RELU					|												|
| Max pooling	      	| 2x2 stride,  outputs 14x14x6 
| Dropout      	| Keep_prob = 0.75 
| Convolution     	| 1x1 stride, same padding, outputs 10x10x16	|
| RELU					|												|
| Max pooling	      	| 2x2 stride,  outputs 5x5x16 
| Dropout      	| Keep_prob = 0.75 				|
| Fully connected		| Input = 400, Output = 120       									|
| RELU				|   
| Dropout      	| Keep_prob = 0.75      									
| Fully connected		| Input = 120, Output = 84       									|
| RELU				|    
| Dropout      	| Keep_prob = 0.75      									
| Fully connected		| Input = 84, Output = 10       									|
| RELU
 


#### 3. Hyper-Parameters.

To train the model, I used the following paramters:

* EPOCHS: 40
* BATCHSIZE: 128
* Dropout (Keep_prob): 0.75
* learning_rate: 0.0003
* optimizer: Adam
* Loss: CrossEntropy

#### 4. Approach and Evaluation

My final model results were:

* training set accuracy of 0.992.
* validation set accuracy of 0.958.
* test set accuracy of 0.941.

If a well known architecture was chosen:
* I chose Lenet model architecture for classifying traffic signals but also added 4 dropout layers at various levels.
* Lenet is already known to work well for image classification as it is able to learn various features from the data to correctly classify images of different classes. It also helps us get a little translational invariance which lets us get better classification accuracy.
* We can be pretty confident with the model's performance on training set as it gives us an accuracy 99%. The comparatively lower but still high enough validation accuracy of 95.8% tell us that the model performs good on probably unseen data as well.

Lastly, the test accuracy of 94.1% approves the model of good performace by classifying 94 out of 100 traffic signs correctly from unseen dataset.
 

### Test a Model on New Images

#### Downloaded german traffic images from the web

Here are five German traffic signs that I found on the web:

![Space for test German Traffic Images][german_labels]

And, here are the <b>predictions</b>:

![Space for test German Traffic Predicted Images][german_predictions]

The model was able to correctly guess only 1 of the 5 traffic signs, which gives an accuracy of 20%. The poor results may be due to the difference in quality of images on which the model is trained as compared to the images against which we are testing.

#### 3. Top 5 softmax probabilities

![Space for test German Traffic Predicted Images with Softmax][top_5_probs]

Almost for all the images the model is pretty confident about its predictions except for the 5th image <b>(Roundabout Mandatory)</b>.

To be truthful, these results are somewhat dissappointing because the images I used for testing were pretty straightforward to me however, the model failed to classify them with high accuracy.


