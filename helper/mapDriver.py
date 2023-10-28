import geocoder
import sys
import io
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from folium import Map, Marker


class MapWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.geoHelper = geocoder.GeoHelper()
        self.setWindowTitle('Folium')
        self.windowWidth, self.windowHeight = 1600,1200
        self.setMinimumSize(400,400)

        layout=QVBoxLayout()
        self.setLayout(layout)

        map = self.geoHelper.showMap(self.geoHelper.geocode('Penang'))

        self.geoHelper.addMarker(map,self.geoHelper.geocode('Bayan Lepas,Pulau Pinang'),'Clinic1')
        self.geoHelper.addMarker(map,self.geoHelper.geocode('Sungai Dua, Pulau Pinang'),'Clinic2')
        self.geoHelper.addMarker(map,self.geoHelper.geocode('Sungai Petani, Kedah'),'Clinic3')
        
        # Save the Folium map as an HTML file
        data = io.BytesIO()
        map.save(data,close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        layout.addWidget(webView)

        # Load the HTML file into the QWebEngineView


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mapWidgetDisplay = MapWidget()
    mapWidgetDisplay.show()
    sys.exit(app.exec_())