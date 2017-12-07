# Trainyolo on ImageNet
Train yolo on ImageNet
## Step 1 Download
download files from: [kaggle imagenet](https://www.kaggle.com/c/imagenet-object-detection-from-video-challenge/data)

## Step 2 preprocessing

Here I will show you how to rearrange dataset for trainning folder in  **test_new**(imagenet_object_detection_video_test_new.tar.gz)
####Note
* Use **python3** for the following .py file
* make sure you have at least 10 GB space(otherwise you need to change copyfile to move file in order to save space)
1.  run getData.python: please put this file amd words.txt in test_new/ILSVRC/, this will generate a label folder, this may take several minutes.
2.  run copyfile.py. this file can be whereever, but please change the 'cur' and 'path'. We say 'cur' as finaldataset, and 'path' as original dataset. this will copy from test_new train part to a new folder. Also, it will change the file names(so that we can train)
3. run changexml.xml, this file should be in finaldataset. put it in train but outside JEPGImages etc folders. to change the filename in xml(not sure if this is useful)
4. run getTinyDataset.py, this file should be in finaldataset. you will get some outputput. put the first line into darknet/examples/yolo.c, the second line into darknet/data/voc.names. this python code is for generate a very small dataset and then we use this to tune yolo
5. run changelabel.py, this file should be in tinydataset. 
6. run getTogether.py, this file will generate train.txt and test.txt
## Step 3
To be continue
