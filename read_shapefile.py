# Created by Thiyaku
# Date: 12-12-2017
# Taken from https://gis.stackexchange.com/questions/145015/is-it-possible-to-look-at-the-contents-of-shapefile-using-python-without-an-arcm/145029

from osgeo import ogr

ogrDriver = ogr.GetDriverByName('ESRI Shapefile')
shpfile = "/home/thiyaku/aapahsystem/Projects/1000/10000000/training/shp/KA_dist.shp"
dataSource = ogrDriver.Open(shpfile, 0) # 0 means read-only. 1 means writeable.


# Get Projection from layer
layer = dataSource.GetLayer()
spatialRef = layer.GetSpatialRef()
print '### Projeciton ###'
print spatialRef

# Layer extent
layerExtent = layer.GetExtent()
print 'xmin = %s, xmax = %s, ymin = %s, ymax = %s' % (layerExtent[0], layerExtent[1], layerExtent[2], layerExtent[3])
# Get number of features in the layer
featureCount = layer.GetFeatureCount()
print 'Number of features:', featureCount

# Get Shapefile Fields and Types
layerDefinition = layer.GetLayerDefn()
print '\n### Shapefile field and type ###'
print "Name  -  Type  Width  Precision"

nFields = layerDefinition.GetFieldCount()

fieldNames = []
for i in range(nFields):
    fieldName =  layerDefinition.GetFieldDefn(i).GetName()
    fieldTypeCode = layerDefinition.GetFieldDefn(i).GetType()
    fieldType = layerDefinition.GetFieldDefn(i).GetFieldTypeName(fieldTypeCode)
    fieldWidth = layerDefinition.GetFieldDefn(i).GetWidth()
    GetPrecision = layerDefinition.GetFieldDefn(i).GetPrecision()
    print fieldName + " - " + fieldType+ " " + str(fieldWidth) + " " + str(GetPrecision)
    fieldNames.append(fieldName)

# Prints the attribute table
print '\n### Attribute table ###'
print(", ".join(str(x) for x in fieldNames))
#print fieldNames
for i in range(featureCount):
    feature = layer.GetFeature(i)
    attrData = []
    for j in range(nFields):
        attrData.append(feature.GetField(j))
    print(", ".join(str(x) for x in attrData))
