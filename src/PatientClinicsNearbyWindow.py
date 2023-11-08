import io
import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea, QSizePolicy, QLineEdit
from PyQt5 import QtWidgets

from .AccountPage import AccountPage
from .PatientClinicDetailsWindow import PatientClinicDetailsWindow
from .model import geoHelper
from .model.Clinic import Clinic
from .model.ClinicRepo import ClinicRepository
from .PatientClinicDetailsWindow import PatientClinicDetailsWindow
from .PageManager import PageManager, FrameLayoutManager


class PatientClinicsNearbyWindow(QWidget):
    def __init__(self, patient):
        super().__init__()
        self.patient = patient
        self.currLocation = (self.patient.getPatientLat(), self.patient.getPatientLon())
        self.pageManager = PageManager()
        self.setupUi()

    def setupUi(self):
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        # this is the header (logo, title, my back button
        self.centralwidget = QWidget()

        self.headerTitle = QLabel(self.centralwidget)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.headerTitle.setFont(font)
        self.headerTitle.setText("Clinics Nearby")
        self.headerTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.headerTitle.setGeometry(QRect(100, 40, 800, 70))
        self.headerTitle.setAlignment(Qt.AlignCenter)
        self.headerTitle.setStyleSheet("margin-left: 20px; margin-right: 20px")

        # Push Button 5 (Log Out)
        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setFixedSize(70, 70)
        self.backButton.setGeometry(QRect(900, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\backbutton.png")
        self.backIcon = QIcon(filepath)
        self.backButton.setIconSize(QSize(70, 70))
        self.backButton.setIcon(self.backIcon)
        self.backButton.clicked.connect(self.backButtonFunction)

        self.searchBar = QLineEdit(self.centralwidget)
        self.searchBar.setGeometry(QRect(500, 130, 450, 40))
        self.searchBar.setPlaceholderText("Search Bar")
        self.searchBar.textChanged.connect(self.filterButtons)

        self.buttonContainer = QWidget()
        button_layout = QVBoxLayout(self.buttonContainer)
        self.buttonContainer.setContentsMargins(20,20,20,20)
        boxScrollArea = QScrollArea()
        boxScrollArea.setWidgetResizable(True)
        boxScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        #Get Clinics
        clinicList = ClinicRepository.getClinicList()

        buttonFont = QFont()
        buttonFont.setFamily("Arial")
        buttonFont.setPointSize(28)
        buttonFont.setBold(True)
        buttonFont.setWeight(75)

        #Insert All the Clinics 
        for count, clinic in enumerate(clinicList):

            clinicRowWidget = QWidget()
            clinicRow = QHBoxLayout(clinicRowWidget)


            updateMapButton = QPushButton()
            updateMapButton.setText("update Map")
            updateMapButton.setFixedSize(QSize(100, 100))
            updateMapButton.clicked.connect(
                lambda checked, clinic=clinic: self.updateMapButton(clinic, self.patient))

            self.clinicButton = QPushButton()
            self.clinicButton.setText(clinic.getClinicName())
            self.clinicButton.setFont(buttonFont)
            self.clinicButton.setFixedSize(QSize(300,100))
            self.clinicButton.clicked.connect(lambda checked, clinic=clinic: self.clinicButtonFunction(clinic, self.patient))

            clinicRow.addWidget(self.clinicButton)
            clinicRow.addWidget(updateMapButton)

            self.buttonContainer.layout().addWidget(clinicRowWidget)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.buttonContainer.layout().addWidget(spacer)

        boxScrollArea.setWidget(self.buttonContainer)
        boxScrollArea.setFixedSize(500,500)
        self.generateMapWidget()

        clinicNearbyLayout = QHBoxLayout()
        clinicNearbyLayout.addWidget(self.mapWidget, 5)
        clinicNearbyLayout.addWidget(boxScrollArea, 5)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.centralwidget)
        mainLayout.addLayout(clinicNearbyLayout)

        self.searchBar.raise_()

        self.setLayout(mainLayout)

    def updateMapButton(self, clinic, patient):
        pass

    def clinicButtonFunction(self, clinic, patient):
        # update the clinic details page here according to button click
        self.clinicDetailsWindow = PatientClinicDetailsWindow(clinic, patient)

        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.frameLayout.addWidget(self.clinicDetailsWindow)
        self.frameLayoutManager.add(self.frameLayout.count() - 1)
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    def backButtonFunction(self):
        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.frameLayoutManager.back()
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    def filterButtons(self):
        searchedText = self.searchBar.text().strip().lower()

        for i in range(self.buttonContainer.layout().count()):
            item = self.buttonContainer.layout().itemAt(i)
            if item and isinstance(item.widget(), QPushButton):
                button = item.widget()
                text = button.text().lower()
                button.setVisible(searchedText in text)

    def generateMapWidget(self):
        self.mapWidget = QWidget()
        self.mapWidget.setStyleSheet("background-color: #BCCAE0; border-radius: 10px;")
        self.mapWidgetLayout = QVBoxLayout(self.mapWidget)

        map = geoHelper.showMap(self.currLocation)  # Return Folium Map

        geoHelper.addMarker(map, self.currLocation, 'We are here!', 'red', 'star')  # Current Loc

        data = io.BytesIO()
        map.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())

        self.mapWidgetLayout.setContentsMargins(20, 20, 20, 20)
        self.mapWidgetLayout.addWidget(webView)