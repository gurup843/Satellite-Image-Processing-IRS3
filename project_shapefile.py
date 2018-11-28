# Created by Thiyaku
# Date: 12-12-2017
# Taken from https://pcjericks.github.io/py-gdalogr-cookbook/projection.html#reproject-a-layer

from osgeo import ogr, osr

ogrDriver = ogr.GetDriverByName('ESRI Shapefile')
shpfile = "../shp/KA_dist.shp"
dataSource = ogrDriver.Open(shpfile, 0) # 0 means read-only. 1 means writeable.


# Get Projection from layer
inLayer = dataSource.GetLayer()
sourceSrs = inLayer.GetSpatialRef()
print '### Projeciton ###'
print sourceSrs

# Layer extent
inExtents = inLayer.GetExtent()
print 'xmin = %s, xmax = %s, ymin = %s, ymax = %s' % (inExtents[0], inExtents[1], inExtents[2], inExtents[3])

# Target projection system
targetSrs = osr.SpatialReference()
targetSrs.ImportFromEPSG(32643) # WGS84 UTM 43N

# create the CoordinateTransformation
coordTrans = osr.CoordinateTransformation(sourceSrs, targetSrs)

outFile = "../shp/KA_dist_utm.shp"

driver = ogr.GetDriverByName('ESRI Shapefile')
outDataSet = driver.CreateDataSource(outFile)
outLayer = outDataSet.CreateLayer("KA_dist_utm", targetSrs, geom_type=ogr.wkbMultiPolygon)

# add fields
inLayerDefn = inLayer.GetLayerDefn()
for i in range(0, inLayerDefn.GetFieldCount()):
    fieldDefn = inLayerDefn.GetFieldDefn(i)
    outLayer.CreateField(fieldDefn)

# get the output layer's feature definition
outLayerDefn = outLayer.GetLayerDefn()

# loop through the input features
inFeature = inLayer.GetNextFeature()
while inFeature:
    # get the input geometry
    geom = inFeature.GetGeometryRef()
    # reproject the geometry
    geom.Transform(coordTrans)
    # create a new feature
    outFeature = ogr.Feature(outLayerDefn)
    # set the geometry and attribute
    outFeature.SetGeometry(geom)
    for i in range(0, outLayerDefn.GetFieldCount()):
        outFeature.SetField(outLayerDefn.GetFieldDefn(i).GetNameRef(), inFeature.GetField(i))
    # add the feature to the shapefile
    outLayer.CreateFeature(outFeature)
    # dereference the features and get the next input feature
    outFeature = None
    inFeature = inLayer.GetNextFeature()

outExtents = outLayer.GetExtent()
print 'xmin = %s, xmax = %s, ymin = %s, ymax = %s' % (outExtents[0], outExtents[1], outExtents[2], outExtents[3])
print outLayer.GetSpatialRef()
# Save and close the shapefiles
dataSource = None
outDataSet = None
