import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join


def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)


d = {}
with open("words.txt") as f:
    print(f.name.split(r'.')[0])
    for line in f:
        tmp =  line.split()
        (key, val) = tmp[0],tmp[1:]
        d[key] = val


def convert_annotation(file,cur):
    in_file = open(file)
    tree = ET.parse(in_file)
    root = tree.getroot()
    folder = cur + root.find('folder').text
    # print(folder)
    # print(in_file.name)
    if not os.path.exists(folder):
        os.makedirs(folder)
    out_file = open('%s/%s.txt' % (folder,in_file.name.split(r'/')[-1].split('.')[0]) , 'w')#test_new/ILSVRC/labels/
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        cls = obj.find('name').text
        if cls not in d:
            continue
        cls_id = cls
        cls = d[cls_id]
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


# cur = '../mobicom/data/test_new/'
# with open(cur) as f:
cur = 'labels/train/'
path = 'Annotations/VID/train/'
for root, subdirs, files in os.walk(path):
    for file in files:
        if '.xml' in file:
            print
            convert_annotation(root+r'/'+file, cur)



