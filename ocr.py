#Herp tunush programmisi
from PIL import Image, ImageChops
import os
import numpy as np
from sklearn.tree import DecisionTreeClassifier
herpler=["چ","ۋ","ې","ر","ت","ي","ۇ","ڭ","و","پ","ھ","س","د","ا","ە","ى","ق","ك","ل","ز","ش","غ","ۈ","ۈ","ب","ن","م","ژ","ف","گ","خ","ج","ۆ"]
clf=DecisionTreeClassifier()


# Bu kedemde birilgen herp hvjjitini aldin bir terep kilidu
def preprocess(filepath):
    file=Image.open(filepath)
    file=trim(file)
    file=resize(file)
    return file

#Bu fonkisiye herp resimidiki tvt tereptiki bsohluklani chikirip tashlaydu
def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    lenth=bbox[2]-bbox[0]
    high=bbox[3]-bbox[1]
    len=max([lenth,high])
    if len < 16:
        len=16
    nbox=(bbox[0],bbox[1],bbox[0]+len,bbox[1]+len)
    if nbox:
        return im.crop(nbox)


#Bu fonkisiye her bir herp resimini 16*16 lik resimge aylanduridu
def resize(infile):
    size = 16, 16
    im = infile
    im.thumbnail(size)
    return im


#Bu fonkisiye resim hvjjitini vekrorgha almashturidu
def makevektor(im):
    rgb_im = im.convert('RGB')
    vektor=[]
    for i in range(16):
        for j in range(16):
            r, g, b = rgb_im.getpixel((i, j))
            if r>=100:
                vektor.append(0)
            if r<100:
                vektor.append(1)
    return vektor


#oginish jeryani mushu yerde
root="data"
matris=[]
for herp in herpler:
    path=os.path.join(root,herp)
    files=os.listdir(path)
    for file in files:
        fpath=os.path.join(path,file)
        image=preprocess(fpath)
        vector=makevektor(image)
        vector.insert(0,herp)
        #print(vector)
        matris.append(vector)
matrix=np.matrix(matris)
xtrain=matrix[0:,1:]
train_label=matrix[0:,0]
clf.fit(xtrain,train_label)


#oginish netijisini korush
testroot="ocrtest"
count=0;
files=os.listdir(testroot)
for file in files:
    fpath=os.path.join(testroot,file)
    image=preprocess(fpath)
    vector=makevektor(image)
    pridected=clf.predict([vector])
    actual_data=os.path.splitext(file)[0]
    print("Aslidiki herp:",actual_data, "\t tonughuni:", pridected[0])
    if actual_data == pridected[0]:
        count += 1
print("toghrilik nisbiti",count/len(files)*100)
