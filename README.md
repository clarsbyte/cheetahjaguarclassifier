# Cheetah Jaguar Classifier Model

## Introduction
There are two models provided in the `main.ipynb` file. First is the model trained from scratch, and the second is a model utilizing transfer learning. <br/>
<br/>

### First Model
The first model implements a CNN (Convolutional Neural Network). It is best described with the following picture.   ![](https://mriquestions.com/uploads/3/4/5/7/34572113/screenshot-2024-09-04-at-3-35-24-pm_orig.png)
In short, convolution and maxpooling serve as a way to filter the distinguishing features of the picture in matrix form. Subsequently, the flatten layer converts the matrix to a list of numbers as the hidden layer accepts an array of numbers rather than matrices. After processing the data
through the hidden layer, the numbers will go through a sigmoid function to classify the image: in this case, an output below 0.5 is a cheetah, and an output above 0.5 is a jaguar.

### Second Model
The second model uses transfer learning from imagenet to assist the learning process. It is much more accurate because of the experienced base model. The picture below illustrates the process well. ![](https://pub.mdpi-res.com/sensors/sensors-23-00570/article_deploy/html/images/sensors-23-00570-g001.png?1672823988) 
We do not need to do the complex convolutional layers as the base model already executes the operation. The numbers will also go through a sigmoid activation function at the end as described previously in the first model.
## Instructions
1. Download dataset from [Kaggle](https://www.kaggle.com/datasets/iluvchicken/cheetah-jaguar-and-tiger)
2. Install libraries via `pip install requirements.txt`
3. Train the model
4. Test images by uploading images from the internet and linking them through the path directory 
```
test_img1 = cv2.imread('chee.jpg') # modify chee.jpg
result = int(model.predict(np.expand_dims(test_img1/255,0)) > 0.5)
result
```
