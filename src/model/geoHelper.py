from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import folium


geocoder = Nominatim(user_agent="CaD")

def geocode(address):
    try:
        location = geocoder.geocode(address)
    except:
        try:
            addressComponents = address.split(",")
            location = geocoder.geocode(addressComponents[1:])
        except:
            print("No Location Found")
            return(None,None)
        
    lat=location.latitude
    lon=location.longitude
    return lat,lon 


def showMap(coordinates):
    map = folium.Map(location=coordinates,zoom_start=11.6)
    return map
    

def addMarker(map,location,text):
    folium.Marker(
        location=location,
        popup=text,
        icon=folium.Icon(icon='star')
    ).add_to(map)


def getDistance(coord1,coord2):
    return geodesic(coord1,coord2).kilometers



