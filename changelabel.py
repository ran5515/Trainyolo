import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
from shutil import copyfile

#put this in tinydataset
labels = [ "n01662784","n02503517","n02121808","n01674464","n04468005","n02062744","n02131653","n02484322","n04530566","n02324045","n02411705","n02834778","n03790512","n02342885","n02402425","n02924116","n02691156","n02355227","n02958343","n02129604","n02084071","n01726692","n02118333","n01503061","n02374451","n02129165"]

d = {}
for i in range(len(labels)):
	d[labels[i]] = i	

def f():
	path = "labels"
	for root, subdirs, files in os.walk(path):
		for file in files:
			with open(root + r"/" + file) as f:
				file_str = f.read()
				#print('file: ' + str(file))
				#print(file_str)
				#return
			# do stuff with file_str
				for item in labels:
					file_str = file_str.replace(item,str(d[item]))

			with open(root + r"/" + file , "w") as f:
				f.write(file_str)

f() 
