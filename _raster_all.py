# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 14:56:11 2017

@author: user
"""

from osgeo import gdal
from osgeo.gdalconst import *
import matplotlib.pyplot as plt
import numpy as np
import glob
import os

tif_files = glob.glob("D:\*.TIF")
out_dir = "D:\outputtry"

for tif_file in tif_files:
    dataset = gdal.Open(tif_file, GA_ReadOnly)
    geotransform = dataset.GetGeoTransform( )
    projection = dataset.GetProjection( )
    band3 = dataset.GetRasterBand(1).ReadAsArray()
    band4 = dataset.GetRasterBand(1).ReadAsArray()
    dataset = None
    
    band3 = band3*1.0
    band4 = band4*1.0
    
    band3[band3<=1] = np.nan
    band4[band4<=1] = np.nan
    
    ndvi = (band4-band3)/(band3+band4)
    
    out_file = os.path.join(out_dir, os.path.basename(tif_file))
    driver = gdal.GetDriverByName('GTiff')
    dataset = driver.Create(out_file, ndvi.shape[1], ndvi.shape[0],1,gdal.GDT_Float32)
    dataset.SetGeoTransform(geotransform)
    dataset.SetProjection(projection)
    dataset.GetRasterBand(1).WriteArray(ndvi, 0, 0)
    dataset = None
    
    #plt.matshow(ndvi)
    #plt.colorbar()
    #plt.show()
    
    print(tif_file)


#
