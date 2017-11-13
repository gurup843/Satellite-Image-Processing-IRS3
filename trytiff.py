# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 11:01:38 2017

@author: GURU
"""
'''
from PIL import Image
import numpy as np
import cv2
path_to_image = 'C:\Users\GURU\Desktop\cdnd43d_v1.1r1\cdnd43d_v1.1r1.tif'
image = Image.open(path_to_image).convert('RGBA')
image.save(path_to_image)
image = cv2.imread(path_to_image, cv2.IMREAD_UNCHANGED)
print image.shape
cv2.imshow("",image)
cv2.waitKey(0)
'''

'''
#averaging smooting
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('D:\output files\did2.jpg')
kernel = np.ones((3,3),np.float32)/9
#blur = cv2.GaussianBlur(img,(5,5),0)
dst = cv2.filter2D(img,-1,kernel)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
#plt.subplot(123),plt.imshow(blur),plt.title('Gaussian')
#plt.xticks([]), plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("", image)
'''




'''
#Gaussian smooting
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('D:\output files\did.jpg')
kernel = np.ones((3,3),np.float32)/9
blur = cv2.GaussianBlur(img,(5,5),0)
#dst = cv2.filter2D(img,-1,kernel)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
#plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
#plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Gaussian')
plt.xticks([]), plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("", image)

'''


#averaging smooting
import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('D:\output files\did2.jpg')

kernel = np.ones((5,5),np.float32)/24
#blur = cv2.GaussianBlur(img,(5,5),0)
#dst = cv2.filter2D(img,-1,kernel)
median = cv2.medianBlur(img,5)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(median),plt.title('median')
plt.xticks([]), plt.yticks([])
#plt.subplot(123),plt.imshow(blur),plt.title('Gaussian')
#plt.xticks([]), plt.yticks([])
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow("", image)
'''
#bilateral filter
 high effective in noise removal and keeping sharp edges 
blur = cv2.bilateralFilter(img,9,75,75)

'''