# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 14:01:56 2017

@author: user
"""

from osgeo import gdal
from osgeo.gdalconst import *
import matplotlib.pyplot as plt
import numpy as np
import glob

in_file1 = "C:\\Users\\user\\Desktop\\python_gis\\data\\16FEB08053710-M2AS_R4C1-056583190020_01_P034.TIF"

dataset = gdal.Open(in_file1, GA_ReadOnly)
geotransform = dataset.GetGeoTransform( )
projection = dataset.GetProjection( )
band3 = dataset.GetRasterBand(3).ReadAsArray()
band4 = dataset.GetRasterBand(4).ReadAsArray()
dataset = None

band3 = band3*1.0
band4 = band4*1.0

band3[band3<=1] = np.nan
band4[band4<=1] = np.nan

ndvi = (band4-band3)/(band3+band4)

plt.matshow(ndvi)
plt.colorbar()
plt.show()

#plt.hist(band1.ravel())
#plt.show()