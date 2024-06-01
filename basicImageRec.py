#READ ME
#this file is for inputting image data into the system
#this is where the image recognitionhappens
#
#

#import libraries
import cv2
import easyocr
import matplotlib.pyplot as plt
import numpy as np


#debug mode
debug = False
#image path
image_path = "gas2.png"
gpsLoc = "228 Front St N, Issaquah, WA 98027"

#read image
img = cv2.imread(image_path)
#this computes faster on gpu but most laptops dont come with gpu
reader = easyocr.Reader(['en'], gpu=False)
text_ = reader.readtext(img)

#this number should be adjusted based on image (didnt have time for that)
threshold = 0.1


#identify all of the text
saves = []
for t_, t in enumerate(text_):
    bbox, text, score = t
    if score > threshold:
        top_left = tuple(map(int, bbox[0]))
        bottom_right = tuple(map(int, bbox[2]))
        if debug: cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 5);cv2.putText(img, text, (top_left[0], top_left[1] - 10), cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)
        print(text,top_left[0],top_left[1])
        #prints all of the found text and adds it to array
        saves.append([text,top_left[0],top_left[1]])

#only to debug (prints a piccture of the image with all identified text)
if debug:
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()

#this to pair prices with costs, (this could be done better)
cats=[]
a=""
for y in saves:
    x=y[0]
    if x.isdigit():
        if a!="":
            cats.append(a + "*"+x)
            a=''
    else:
        a=x

print(cats)

#outpuut findings to file (using special fcharacters to
#between different items to differentiate between different types of data)
tot=[]
file = open('data.txt', 'r')
while True:
    line = file.readline()
    if not line:
        break
    tot.append(line)

tem = '^'.join(cats)
tem= tem + ';'+gpsLoc+"\n"
if tem not in tot:
    tot.append(tem)

with open("data.txt", "w") as file1:

    file1.writelines(tot)


