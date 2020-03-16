# Object-Detection-Techfest
Stood in top 8 for Techfest - 2018 ,could not get to top 3 finalists
https://www.linkedin.com/pulse/tata-makerthon-2018-finalists-piyush-mishra

In this we had to build a model which was capable of detecting the object from one image and then check if the object is detected in the surrounding. We first had to click the photo of an image and then we needed to check in the surroundings.

## Apps - [05 app](https://github.com/skystone1000/Object-Detection-Techfest/tree/master/05%20app)
The "object detection" app clicks the photo of an image and uploads it to the firebase cloud storage. Next the "surrounding camera" app clicks the picture in all the directions and then upload them too to the firebase storage.

## Detection of object (Script) - [04 darkflow](https://github.com/skystone1000/Object-Detection-Techfest/tree/master/04%20darkflow) 
Next the task of detecting the object from the first image with the images from the surrounding and then giving the result if match was found then it would upload the resultant image to firebase so as to be seen from the app. We have used darkflow which is the python implementation of YOLO you can get the weights and config from the following links. 
link - https://pjreddie.com/darknet/yolo/ 

## Firebase (upload/download) - [03 upload and download from firebase](https://github.com/skystone1000/Object-Detection-Techfest/tree/master/03%20upload%20and%20download%20from%20firebase)
you can use download.py to download and upload.py to upload any file accoring to your firebase path


# Training for Custom Object 
You can train the YOLO model based on your requirements. I have trained the YOLO model for detecting puppies 

## Labeling - [06 labeling images](https://github.com/skystone1000/Object-Detection-Techfest/tree/master/06%20labeling%20images)
Initailly you need to download the images having the object and some which do not contain the object. You can do that with the help of a chrome extension very easily. 

Next number them starting from 1 till the end. you can do that with the help of "name.py" file present.

Now you need to generate labels for the bounding boxesyou can do that with boudbox.py, this will generate the text file for all the images.

## Training - [07 training](https://github.com/skystone1000/Object-Detection-Techfest/tree/master/07%20training)
I have trained the model on google colab you can do it locally if you want. For training on google colb you need download the yolo-master zip and update the classes and add the images

for furthur details look [training.md](https://github.com/skystone1000/Object-Detection-Techfest/blob/master/07%20training/training%20readme.md)

Zip the file again and upload to google drive and then you can run the Tatamakerthon yolo_v2_tiny.ipynb
