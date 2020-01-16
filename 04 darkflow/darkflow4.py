from darkflow.net.build import TFNet
import cv2

from google.cloud import storage

def download_blob(bucket_name,prefix,dl_dir):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name=bucket_name)
    blobs = bucket.list_blobs(prefix=prefix)  # Get list of files
    for blob in blobs:
        filename = blob.name.replace('/', '_') 
        blob.download_to_filename(dl_dir + filename)  # Download

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))   #Upload 

#Download image from which is uploaded from mobile
download_blob('ai-ufdggn.appspot.com','uploads/','/home/skystone/iitb/darkflow/')
print("All files in directory /uploads downloaded")

options = {"model": "cfg/yolo.cfg", "load": "bin/yolo.weights", "threshold": 0.3}
tfnet = TFNet(options)
#Image passed from the app is test.jpg
imgcv = cv2.imread("uploads_test.jpg")
result = tfnet.return_predict(imgcv)        
#print(result)


#Download all images from surroundings
download_blob('ai-ufdggn.appspot.com','Surr/','/home/skystone/iitb/darkflow/')


for things in result:
    #print(things)
    #objects.append(things["label"])
    PhoneObject = things["label"]

print("Object in the image given by the phone is:")    
print(PhoneObject)
print("\n")


#List of all the images sent by the camera on the drone
DrImgNames = ["Surr_N.jpg","Surr_NE.jpg","Surr_E.jpg","Surr_SE.jpg","Surr_S.jpg","Surr_SW.jpg","Surr_W.jpg","Surr_NW.jpg"]

for images in DrImgNames:
    print("=========================================================================================================================")
    print(images)
    imgcv = cv2.imread(images)
    DrImgResult = tfnet.return_predict(imgcv)
    #print(result)

    print("all the objects present in "+images+" image are")
    DrObjects = []

    for DrImgThings in DrImgResult:
        #print(DrImgThings)
        if PhoneObject in DrImgThings["label"]:
            print("object found at ")
            print(DrImgThings["topleft"])
            print(DrImgThings["bottomright"])
            #for Coordinates in DrImgThings["topleft"]:
            #    print(Coordinates)
            #Upload this image to /Result directory in firebase
            upload_blob('ai-ufdggn.appspot.com', images , 'Result/'+'Result.jpg')
                
        
        DrObjects.append(DrImgThings["label"])
    
    print(DrObjects)
    print("\n")
    
