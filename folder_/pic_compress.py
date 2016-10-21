#coding=utf-8
from PIL import Image
import os
myPath = './'
outPath = './compress_oic/'
def processImage(filesource,destsource,name,imgtype):
    imgtype = 'jpeg' if imgtype == '.jpg' else 'png'

    im = Image.open(filesource + name)

    rate = max(im.size[0]/640.0 if im.size[0] > 640 else 0,im.size[1]/1136.0 if im.size[1] > 1136 else 0)
    if rate:
        im.thumbnail((im.size[0]/rate,im.size[1]/rate))
    im.save(destsource + name, imgtype)

def run():

    img_list = []

    pos_list = []

    os.chdir(myPath)

    for i in os.listdir(os.getcwd()):
        postfix = os.path.splitext(i)[1]

        if postfix == '.jpg' or postfix == '.png':
            pos_list.append(postfix)
            img_list.append(i)

    return (img_list,pos_list)

def path_(addr,img_):
    
    addr_list = []
    for p in img_:
        addr_list.append(addr)

    return addr_list 

if __name__ == '__main__':
    
    name = run()

    my_path = path_(myPath,name[0])
    out_path = path_(outPath,name[0])
    map(processImage,my_path,out_path,name[0],name[1])

    


















