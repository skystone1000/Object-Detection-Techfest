from darkflow.net.build import TFNet
import cv2

options = {"model": "cfg/yolo.cfg", "load": "bin/yolo.weights", "threshold": 0.3}

tfnet = TFNet(options)

#Image passed from the app is test.jpg

imgcv = cv2.imread("test.jpg")
result = tfnet.return_predict(imgcv)        
#print(result)

#objects = []

for things in result:
    #print(things)
    #objects.append(things["label"])
    PhoneObject = things["label"]

print("Object in the image given by the phone is:")    
print(PhoneObject)
print("\n")



"""
#List of all the images sent by the camera on the drone
DrImgNames = ["N.jpg","NE.jpg","E.jpg","SE.jpg","S.jpg","SW.jpg","W.jpg","NW.jpg"]

for images in DrImgNames:
    print(images)
    imgcv = cv2.imread(images)
    DrImgResult = tfnet.return_predict(imgcv)
    #print(result)

    DrObjects = ["all the objects present in "+images+" image are"]

    for DrThings in DrImgResult:
        #print(DrThings)
        if PhoneObject in DrThings["label"]:
            print("object found")
        
        DrObjects.append(DrThings["label"])
    
    print(DrObjects)
    print("\n")
    
"""
