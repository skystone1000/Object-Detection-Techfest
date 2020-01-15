from darkflow.net.build import TFNet

options = {"model": "cfg/yolo.cfg", "load": "bin/yolo.weights", "threshold": 0.3}
tfnet = TFNet(options)
#Image passed from the app is test.jpg
imgcv = cv2.imread("NE.jpg")
result = tfnet.return_predict(imgcv)        
print(result)
