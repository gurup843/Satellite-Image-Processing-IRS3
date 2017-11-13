# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 05:47:58 2017
Intern: KSRSAC
@author: GURU
reference from Stackflow and Internet and updated as per convenience to local image
"""


from osgeo import gdal
from osgeo import gdal_array
import cv2
import numpy as np
from matplotlib import pyplot as plt
'''
to read image

'''
s1 = gdal.Open('F:\L3_SAT_8B_V1_74.75E14.75N_d43i13_18nov11\l3d43i1318nov11\BAND3.tif')
s2 = gdal.Open('F:\L3_SAT_8B_V1_74.75E14.75N_d43i13_18nov11\l3d43i1318nov11\BAND4.tif')
s3 = gdal.Open('F:\L3_SAT_8B_V1_74.75E14.75N_d43i13_18nov11\l3d43i1318nov11\BAND5.tif')

'''
GetRaterBand(1): 

'''
'''gdal.AllRegister()
'''
b1 = s1.GetRasterBand(1)
img1 = b1.ReadAsArray(0,0,s1.RasterXSize, s1.RasterYSize)
b2 = s2.GetRasterBand(1)
img2 = b2.ReadAsArray(0,0,s2.RasterXSize, s2.RasterYSize)
b3 = s3.GetRasterBand(1)
img3 = b3.ReadAsArray(0,0,s3.RasterXSize, s3.RasterYSize)
#import numpy as np
img = np.dstack((img1,img2, img3))
#from matplotlib import pyplot as plt
##plt.imshow(img)
##plt.show()
#plt.imwrite('image.tif')
imgn = img
hist,bins = np.histogram(imgn.flatten(), 256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(imgn.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()
#equ = cv2.equalizeHist(imgn)
cv2.imwrite('D:did.jpg', imgn)
cv2.imwrite('D:did.tif', imgn)
imgn = cv2.imread('D:did.jpg', 0)
equ = cv2.equalizeHist(imgn)
#res = np.hstack(imgn,equ)
cv2.imwrite('D:did2.jpg', imgn)
cv2.imshow('okok',equ)
cv2.waitKey(0)

hist,bins = np.histogram(equ.flatten(), 256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/cdf.max()
plt.plot(cdf_normalized, color = 'b')
plt.hist(equ.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()

cv2.imshow('image', imgn)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow()

#resize(imgn, 0.5, 0.5, interploation);
imgn = cv2.imread(img,0,0,100,100)
       
band = s1.GetRasterBand(1)
print("band Type={}".format(gdal.GetDataTypeByName(band.DataType)))
