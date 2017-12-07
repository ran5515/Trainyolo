import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import random

path = 'Annotations'

for rootdir, subdirs, files in os.walk(path):
    for file in files:
        if '.xml' in file:
	    cur = rootdir + r'/' + file
	    tree=ET.parse(cur)
    	    root = tree.getroot()
	    folder = root.find('folder').text.split(r'/')[-1]
	    filename = root.find('filename').text
    	    root.find('filename').text = folder + filename + '.JPEG'
	    tree.write(cur)
