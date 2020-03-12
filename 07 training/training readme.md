Training The Yolo 

	1) Download the yolo-v2-darknet-master.zip
	2) Extract the zip and goto 
		yolo-v2-darknet-master/data/obj
	3) Copy all the images to obj folder
	4) Copy all bounding-box txt file to the same obj folder
	5) Goto yolo-v2-darknet-master/data/coco.names  && obj.names
		add the class names that you have collected data for
	6) Goto yolo-v2-darknet-master/data/obj.data
		specify number of classes you have added
	7) Replace the train file created in
		yolo-v2-darknet-master/data/
	8) Zip the folder yolo-v2
	9) Upload the zip and yolo_v2_tiny.ipynb to google drive
	10) Right click on yolo ipynb -> open with -> colaboratory -> install
	11) Open with google colab 

	12) Run the cells and remaining instructions are given there