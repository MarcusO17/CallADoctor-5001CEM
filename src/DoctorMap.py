import os
import sys
import requests
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea, QSizePolicy, QLineEdit
from PyQt5 import QtWidgets
from .ClinicDetailedSchedule import ClinicDetailedSchedule
from .PageManager import FrameLayoutManager
from src.model import geoHelper, Clinic
from .model.AppointmentRepo import AppointmentRepository
import sys
import io
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from folium import Map, Marker


class DoctorMap(QWidget):
    def __init__(self, doctor):
        super().__init__()
        self.doctor = doctor
        self.clinic = Clinic.getClinicfromID(self.doctor.getClinicID())
        self.currLocation = (self.clinic.getClinicLat(), self.clinic.getClinicLon())
        self.setupUi()

    def setupUi(self):
        self.centralwidget = QWidget()

        self.generateMapWidget()

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.mapWidget)

        self.setLayout(mainLayout)

    def generateMapWidget(self):
        self.mapWidget = QWidget()
        self.mapWidget.setObjectName("mapWidget")
        self.mapWidget.setStyleSheet("""QWidget#mapWidget {background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                                                stop: 0 rgba(25, 4, 130, 255), 
                                                                                stop: 1 rgba(119, 82, 254, 255)
                                                                            );
                                                                            border-radius: 10px;
                                                                            text-align: center;
                                                                            color: white;
                                                                        }""")
        self.mapWidgetLayout = QVBoxLayout(self.mapWidget)

        map = geoHelper.showMap(self.currLocation)  # Return Folium Map

        geoHelper.addMarker(map, self.currLocation, 'We are here!', 'red', 'star')  # Current Loc
        map = self.generatePatientMarkers(map=map)

        data = io.BytesIO()
        map.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())

        self.mapWidgetLayout.setContentsMargins(20, 20, 20, 20)
        self.mapWidgetLayout.addWidget(webView)

    def generatePatientMarkers(self, map):
        patientsWeekly = AppointmentRepository.getPatientLocations(self.clinic.getClinicID())
        for patients in patientsWeekly:
            geoHelper.addMarker(map, (patients.getPatientLat(), patients.getPatientLon()), patients.getPatientAddress()
                                , 'lightblue', 'home')
        return map
