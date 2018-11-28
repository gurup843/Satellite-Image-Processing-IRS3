# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 07:18:02 2017

@author: user
"""



def download_s2(min_lon,max_lon,min_lat,max_lat, start_date, end_date, download_dir):
    
    from sentinelsat.sentinel import SentinelAPI
    
    location_str = 'POLYGON((%.2f %.2f,%.2f %.2f,%.2f %.2f,%.2f %.2f,%.2f %.2f))' % (min_lon, min_lat,
                                                                          max_lon, min_lat,
                                                                          max_lon, max_lat,
                                                                          min_lon, max_lat,
                                                                          min_lon, min_lat)
  
    api = SentinelAPI('gurup843', 'intelibm',
                      'https://scihub.copernicus.eu/dhus/')
    prod = api.query(location_str,(start_date,end_date), platformname="Sentinel-2")
     
   #len(prod.items())
    
    
    api.download_all(prod,download_dir, checksum=True, max_attempts=5)
    
    return download_dir

def extract_zip_from_s2(input_folder):
    import glob
    import zipfile
    import os
    # Read the zip files
    
    zip_files=glob.glob(os.path.join(input_folder, '*.zip'))
        
    # Loop through zip files
    for zip_file in zip_files:
        zip_ref = zipfile.ZipFile(zip_file, 'r')
        zip_ref.extractall(input_folder)
        zip_ref.close()
        print(zip_file)
        
def stack_raster(raw_dir, out_dir):
    import os
    import glob
    import gdal    
    
    raw_files = glob.glob(os.path.join(raw_dir, 'S2A*.SAFE'))
    for raw_file in raw_files:
        bands = glob.glob(os.path.join(raw_file, 'GRANULE\L1C*\IMG_DATA\*_B*.jp2'))
        tenm_bands = []
        for band in bands:
            res  = gdal.Open(band).GetGeoTransform()[1]
            if res == 10:
                tenm_bands.append(band)
        if len(tenm_bands):
            bn = os.path.basename(tenm_bands[0])
            dTime = bn[:-8]
            outvrt = os.path.join(out_dir, dTime + '.vrt')
            outtif = os.path.join(out_dir, dTime + '.tif')
            print outtif
            if not os.path.exists(outtif):
                outds = gdal.BuildVRT(outvrt, tenm_bands, separate=True)
                outds = gdal.Translate(outtif, outds)
                outds = None           

 
def merge_raster(in_dir, out_dir):
    import glob    
    import os
    import subprocess
    in_files = glob.glob(os.path.join(in_dir, '*.tif'))
    yyyymmdds = []
    for in_file in in_files:
        bn = os.path.basename(in_file)
        yyyymmdds.append('201' + bn.split('201')[1][:5])
    unique_yyyymmdds = list(set(yyyymmdds))
    for u_yyyymmdd in unique_yyyymmdds:
        out_file = os.path.join(out_dir, u_yyyymmdd + '.tif')
        in_files = glob.glob(os.path.join(in_dir, '*' + u_yyyymmdd + '*.tif'))
        if not os.path.exists(out_file):
            merge_cmd = 'python C:\Users\user\Anaconda2\Scripts\gdal_merge.py -o %s' % (out_file)
            for in_file in in_files:
                merge_cmd = merge_cmd + ' ' + in_file
            #print merge_cmd
            subprocess.call(merge_cmd, shell = True)
            
def clip_raster(raster_dir, vector_file, clip_dir):
    import os
    import subprocess
    import glob
    in_files = glob.glob(os.path.join(raster_dir, '*.tif'))
    for in_file in in_files:
        out_file = os.path.join(clip_dir, os.path.basename(in_file))
        if not os.path.exists(out_file):
            clip_cmd = 'gdalwarp -cutline %s -crop_to_cutline %s %s' % (vector_file, in_file, out_file)
            print clip_cmd
            subprocess.call(clip_cmd, shell=True)
        

def raster_to_vector(raster_dir, vector_dir):
    import glob
    import os
    import subprocess
    raster_files = glob.glob(os.path.join(raster_dir, '*.tif'))
    for raster_file in raster_files:
        bn = os.path.basename(raster_file)        
        vector_file = os.path.join(vector_dir, bn[:-4] + '.shp')
        if not os.path.exists(vector_file):
            rtv_cmd = 'python C:\Users\user\Anaconda2\Scripts\gdal_polygonize.py %s -f "ESRI Shapefile" %s' % (raster_file, vector_file)
            print rtv_cmd
            subprocess.call(rtv_cmd, shell = True)
#    tif_dir = '/home/thiyaku/training/20171215/data/tif'
#    #extract_zip_from_s2(download_dir)
#    
#    stack_raster(download_dir, tif_dir)
#    merge_dir = '/home/thiyaku/training/20171215/data/tif_merged'    
#    merge_raster(tif_dir, merge_dir)
#    
#    clip_dir = '/home/thiyaku/training/20171215/data/tif_clip'
#    vector_file = '/home/thiyaku/training/20171215/data/shp/test2.shp'
#    clip_raster(merge_dir, vector_file, clip_dir)    
#    vector_dir = '/home/thiyaku/training/20171215/data/vector'
#    raster_to_vector(clip_dir, vector_dir)

if __name__ == '__main__':
    min_lat = 14.0
    max_lat = 15.0
    min_lon = 77.0
    max_lon = 78.0
    # Dates yyyymmdd format
    start_date = '20170501'
    end_date = '20170510'
    download_dir='D:\input'
    download_s2(min_lon,max_lon,min_lat,max_lat, start_date, end_date, download_dir)
    
#    tif_dir = 'C:\Users\user\Desktop\python_gis\miral\\tif'
#    extract_zip_from_s2(download_dir)
#    
#    stack_raster(download_dir, tif_dir)
#    merge_dir = 'C:\Users\user\Desktop\python_gis\miral\\tif_merged'    
#    #merge_raster(tif_dir, merge_dir)
#    
#    clip_dir = 'C:\Users\user\Desktop\python_gis\miral\\tif_clip'
#    vector_file = 'C:\Users\user\Desktop\python_gis\miral\shp\\test2.shp'
#    clip_raster(merge_dir, vector_file, clip_dir)    
#    vector_dir = 'C:\Users\user\Desktop\python_gis\miral\\vector'
#    raster_to_vector(clip_dir, vector_dir)
