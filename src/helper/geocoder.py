from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import folium


class GeoHelper:
    geocoder = Nominatim(user_agent="CaD")
    
    def geocode(self,address):
        try:
            location = self.geocoder.geocode(address)
        except:
            print(f'Unknown Location!')
            return(None,None)
        lat=location.latitude
        lon=location.longitude
        return[lat,lon]
    

    def showMap(self,coordinates):
        map = folium.Map(location=coordinates,zoom_start=11.6)
        return map
        
    
    def addMarker(self,map,location,text):
        folium.Marker(
            location=location,
            popup=text,
            icon=folium.Icon(icon='star')
        ).add_to(map)

    def getDistance(self,coord1,coord2):
        return geodesic(coord1,coord2).kilometers

 

