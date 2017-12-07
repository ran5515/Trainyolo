from shutil import copyfile
import xml.etree.ElementTree as ET
import pickle
import os


cur = '../mobicom/data/final/train/Annotations/'
path = '../mobicom/data/test_new/ILSVRC/Annotations/VID/train'
if not os.path.exists(cur):
	os.makedirs(cur)

for root, subdirs, files in os.walk(path):
    for file in files:
        if '.xml' in file:
            src = root + r'/' + file
            dst = cur + str(root).split('/')[-1] + file
            copyfile(src, dst)


cur = '../mobicom/data/final/train/JPEGImages/'
path = '../mobicom/data/test_new/ILSVRC/Data/VID/train'
if not os.path.exists(cur):
	os.makedirs(cur)

for root, subdirs, files in os.walk(path):
    for file in files:
        if '.JPEG' in file:
            src = root + r'/' + file
            dst = cur + str(root).split('/')[-1]+file
            copyfile(src, dst)


cur = '../mobicom/data/final/train/labels/'
path = '../mobicom/data/test_new/ILSVRC/labels'
if not os.path.exists(cur):
	os.makedirs(cur)
for root, subdirs, files in os.walk(path):
    for file in files:
        if '.txt' in file:
            src = root + r'/' + file
            dst = cur + str(root).split('/')[-1]+file
            copyfile(src, dst)
