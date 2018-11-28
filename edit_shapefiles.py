import ogr

shpfile = '/home/thiyaku/training/data/TM_WORLD_BORDERS-0.3.shp'

dataSource =  ogr.Open(shpfile, 0)

