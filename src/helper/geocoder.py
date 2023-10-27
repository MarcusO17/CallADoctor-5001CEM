from geopy.geocoders import Nominatim
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
        return(lat,lon)
    




    