# Create point - vector
from osgeo import ogr, osr

# Function to create point feature
# Input: longitude, latitude, index of the feature, name of the city
# Output: Return the created feature
def createPointFeature(lon, lat, featureIndex, name):
    point = ogr.Geometry(ogr.wkbPoint)
    point.SetPoint(0, lon, lat)
    feature = ogr.Feature(layerDefinition)
    feature.SetGeometry(point)
    feature.SetFID(featureIndex)
    feature.SetField('Name', name)
    return feature

# Set spatial reference as WGS84
srs = osr.SpatialReference()
srs.ImportFromProj4('+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs')

# Create shapefile
driver = ogr.GetDriverByName('ESRI Shapefile')
shpData = driver.CreateDataSource('../shp/cities.shp')

# Create a layer named cities
layer = shpData.CreateLayer('cities', srs, ogr.wkbPoint)
layerDefinition = layer.GetLayerDefn()

# Add a new field 'Name'
nameField = ogr.FieldDefn('Name', ogr.OFTString)
layer.CreateField(nameField)


feature = createPointFeature(77.5946, 12.9716, 0, 'Bengaluru')
layer.CreateFeature(feature)

feature = createPointFeature(76.6394, 12.2958, 1, 'Mysore')
layer.CreateFeature(feature)

feature = createPointFeature(74.8560, 12.9141, 2, 'Mangalore')
layer.CreateFeature(feature)

feature = createPointFeature(74.4977, 15.8497, 3, 'Belgaum')
layer.CreateFeature(feature)

feature = createPointFeature(75.120, 13.3647, 4, 'Hubli')
layer.CreateFeature(feature)

shpData.Destroy()
