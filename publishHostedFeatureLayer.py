from arcgis.gis import GIS
from arcgis import features
import datetime as dt

def now_dt():
    return str(int(dt.datetime.now().timestamp()))

def createHostedFeatureService():
    print("Creating Hosted Feature Layer")

#Access the portal
gis =GIS("https://epressmaps.maps.arcgis.com/",username="epressmaps",password="dThZ7kGIQ6vksmJ6hF3S")
# check if service name is available
empty_service_item = None
if gis.content.is_service_name_available(service_name= "world_capitals", service_type = 'featureService'):
    empty_service_item = gis.content.create_service(name='world_capitals', service_type='featureService')


