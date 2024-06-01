import cv2
import easyocr
import matplotlib.pyplot as plt
import numpy as np

debug = False
# read image
image_path = "gas2.png"
gpsLoc = "228 Front St N, Issaquah, WA 98027"

img = cv2.imread(image_path)

# instance text detector
reader = easyocr.Reader(['en'], gpu=False)

# detect text on image
text_ = reader.readtext(img)

threshold = 0.1
# draw bbox and text

saves = []
for t_, t in enumerate(text_):

    bbox, text, score = t

    if score > threshold:
        # Extract the top-left and bottom-right corners
        top_left = tuple(map(int, bbox[0]))
        bottom_right = tuple(map(int, bbox[2]))
        if debug: cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 5);cv2.putText(img, text, (top_left[0], top_left[1] - 10), cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)
        print(text,top_left[0],top_left[1])
        saves.append([text,top_left[0],top_left[1]])

if debug:
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.show()


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


