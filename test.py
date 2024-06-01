import cv2
import easyocr
import matplotlib.pyplot as plt
import numpy as np

# read image
image_path = "gas2.png"

img = cv2.imread(image_path)

# instance text detector
reader = easyocr.Reader(['en'], gpu=True)

# detect text on image
text_ = reader.readtext(img)

threshold = 0.1
# draw bbox and text
for t_, t in enumerate(text_):

    bbox, text, score = t

    if score > threshold:
        # Extract the top-left and bottom-right corners
        top_left = tuple(map(int, bbox[0]))
        bottom_right = tuple(map(int, bbox[2]))
        cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 5)
        cv2.putText(img, text, (top_left[0], top_left[1] - 10), cv2.FONT_HERSHEY_COMPLEX, 0.65, (255, 0, 0), 2)
        print(text,top_left[0],top_left[1])

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()