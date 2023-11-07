import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea, QSizePolicy, QLineEdit
from PyQt5 import QtWidgets
from .ClinicDetailedSchedule import ClinicDetailedSchedule
from .PageManager import FrameLayoutManager
from src.model import geoHelper
import sys
import io
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from folium import Map, Marker


class ClinicMap(QWidget):
    def __init__(self, clinic):
        super().__init__()
        self.clinic = clinic
        self.setupUi()

    def setupUi(self):

        self.centralwidget = QWidget()

        self.generateMapWidget()

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.mapWidget)

        self.setLayout(mainLayout)

    def generateMapWidget(self):
        self.mapWidget = QWidget()
        self.mapWidget.setStyleSheet("background-color: #BCCAE0; border-radius: 10px;")
        self.mapWidgetLayout = QVBoxLayout(self.mapWidget)

        map = geoHelper.showMap(geoHelper.geocode('Penang')) #Return Folium Map

        data = io.BytesIO()
        map.save(data,close_file=False)
        
        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
    
        self.mapWidgetLayout.setContentsMargins(20, 20, 20, 20)
        self.mapWidgetLayout.addWidget(webView)


