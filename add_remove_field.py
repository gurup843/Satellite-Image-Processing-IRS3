# Created by Thiyaku
# Date: 12-12-2017
# Taken from https://pcjericks.github.io/py-gdalogr-cookbook/projection.html#reproject-a-layer

from osgeo import ogr, osr

ogrDriver = ogr.GetDriverByName('ESRI Shapefile')
shpfile = "../shp/KA_dist_f.shp"
dataSource = ogrDriver.Open(shpfile, 1) # 0 means read-only. 1 means writeable.


# Get Projection from layer
inLayer = dataSource.GetLayer()
sourceSrs = inLayer.GetSpatialRef()
print '### Projeciton ###'
print sourceSrs

# Layer extent
inExtents = inLayer.GetExtent()
print 'xmin = %s, xmax = %s, ymin = %s, ymax = %s' % (inExtents[0], inExtents[1], inExtents[2], inExtents[3])

# Create a new field
areaField = ogr.FieldDefn('Area', ogr.OFTReal)
inLayer.CreateField(areaField)
areaField.SetWidth(32)
areaField.SetPrecision(2) #added line to set precision

# Target projection system
targetSrs = osr.SpatialReference()
targetSrs.ImportFromEPSG(32643) # WGS84 UTM 43N

# create the CoordinateTransformation
coordTrans = osr.CoordinateTransformation(sourceSrs, targetSrs)

# loop through the input features
inFeature = inLayer.GetNextFeature()
while inFeature:
    # get the input geometry
    geom = inFeature.GetGeometryRef()
    print geom.GetArea()
    # Project the geom to UTM to get the area in square meters
    geom.Transform(coordTrans)
    geomArea = geom.GetArea()
    geomArea =  round(geomArea, 2)
    inFeature.SetField('Area', geomArea)
    inLayer.SetFeature(inFeature)
    inFeature = None
    inFeature = inLayer.GetNextFeature()
#outFile = "../shp/KA_dist_f.shp"

#driver = ogr.GetDriverByName('ESRI Shapefile')
#outDataSet = driver.CreateDataSource(outFile)
#outLayer = outDataSet.CreateLayer("KA_dist_utm", targetSrs, geom_type=ogr.wkbMultiPolygon)

# add fields
# inLayerDefn = inLayer.GetLayerDefn()


