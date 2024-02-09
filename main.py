import pytesseract as tess
tess.pytesseract.tesseract_cmd =r'C:\Program Files\Tesseract-OCR\tesseract'
from PIL import Image
import numpy as np

import cv2
vid =cv2.VideoCapture(0)
while(True):
	ret,image = vid.read()
	cv2.imshow('image',image)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	cv2.imwrite("newimage.png",image)
# image1 = cv2.imread('newimage.png')
# kernel = np.ones((5, 5), np.uint8)
# out = cv2.addWeighted(image1, contrast, image1, 0, brightness)

#
# cv2.imshow("new",image)
# cv2.waitKey(0)
vid.release()
cv2.destroyAllWindows()



img = Image.open('newimage.png')
text = tess.image_to_string(img)
print(text)
# list = text.split(",")
# list1=[]
# for i in list:
#     i = i.replace('\n','')
#     list1.append(i)
# print(list1)

