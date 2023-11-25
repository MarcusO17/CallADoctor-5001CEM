import io
import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize, QPoint
from PyQt5.QtGui import QFont, QPixmap, QIcon, QColor
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea, QSizePolicy, QLineEdit, QGraphicsDropShadowEffect
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
        font.setFamily("Montserrat")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.headerTitle.setFont(font)
        self.headerTitle.setText("Clinics Nearby")
        self.headerTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.headerTitle.setGeometry(QRect(30, 40, 800, 70))
        self.headerTitle.setObjectName("headerTitle")
        self.headerTitle.setAlignment(Qt.AlignCenter)
        self.headerTitle.setStyleSheet("""QLabel#headerTitle {
                                                            background: #D0BFFF;
                                                            border-radius: 10px;
                                                            }""")
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        self.headerTitle.setGraphicsEffect(effect)

        self.searchBar = QLineEdit(self.centralwidget)
        self.searchBar.setGeometry(QRect(450, 130, 450, 40))
        self.searchBar.setPlaceholderText("Search Bar")
        self.searchBar.textChanged.connect(self.filterButtons)

        self.buttonContainer = QWidget()
        button_layout = QVBoxLayout(self.buttonContainer)
        self.buttonContainer.setObjectName("buttonContainer")
        self.buttonContainer.setStyleSheet("""QWidget#buttonContainer {
                                                            background: #D0BFFF;
                                                            border-radius: 10px;
                                                            margin-left: 100px;
                                                            }""")
        self.buttonContainer.setContentsMargins(20,20,20,20)
        boxScrollArea = QScrollArea()
        boxScrollArea.setWidgetResizable(True)
        boxScrollArea.setObjectName("boxScrollArea")
        boxScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        #Get Clinics
        clinicList = ClinicRepository.getClinicList()

        buttonFont = QFont()
        buttonFont.setFamily("Montserrat")
        buttonFont.setPointSize(20)
        buttonFont.setBold(True)
        buttonFont.setWeight(75)

        self.clinicButtonList = list()

        #Insert All the Clinics 
        for count, clinic in enumerate(clinicList):

            clinicRowWidget = QWidget()
            clinicRow = QHBoxLayout(clinicRowWidget)


            updateMapButton = QPushButton()
            updateMapButton.setText("update Map")
            updateMapButton.setFixedSize(QSize(100, 100))
            updateMapButton.setStyleSheet("""QPushButton {
                                                    background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                                            stop: 0 rgba(10, 2, 85, 255), 
                                                                            stop: 1 rgba(59, 41, 168, 255));
                                                    border-radius: 10px; color: white;
                                                    text-align: left; 
                                                    padding-left: 20px;
                                                    }
                                                    QPushButton:hover
                                                    {
                                                      background-color: #7752FE;
                                                      text-align: left; 
                                                      padding-left: 20px;
                                                    }""")

            effect = QGraphicsDropShadowEffect(
                offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
            )
            updateMapButton.setGraphicsEffect(effect)
            updateMapButton.clicked.connect(
                lambda checked, clinic=clinic: self.updateMapButton(clinic,clinicList))

            self.clinicButton = QPushButton()
            self.clinicButton.setText(clinic.getClinicName())
            self.clinicButton.setFont(buttonFont)
            self.clinicButton.setFixedSize(QSize(200,100))
            self.clinicButton.setStyleSheet("""QPushButton {
                                                    background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                                            stop: 0 rgba(10, 2, 85, 255), 
                                                                            stop: 1 rgba(59, 41, 168, 255));
                                                    border-radius: 10px; color: white;
                                                    text-align: left; 
                                                    padding-left: 20px;
                                                    }
                                                    QPushButton:hover
                                                    {
                                                      background-color: #7752FE;
                                                      text-align: left; 
                                                      padding-left: 20px;
                                                    }""")

            effect = QGraphicsDropShadowEffect(
                offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
            )
            self.clinicButton.setGraphicsEffect(effect)
            self.clinicButton.clicked.connect(lambda checked, clinic=clinic: self.clinicButtonFunction(clinic, self.patient))

            clinicRow.addWidget(self.clinicButton)
            clinicRow.addWidget(updateMapButton)

            self.clinicButtonList.append(clinicRow)

            self.buttonContainer.layout().addWidget(clinicRowWidget)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.buttonContainer.layout().addWidget(spacer)

        boxScrollArea.setWidget(self.buttonContainer)
        boxScrollArea.setFixedSize(500,500)
        boxScrollArea.setStyleSheet("""QScrollArea#boxScrollArea {
                                                    background: #D0BFFF;
                                                    border-radius: 10px;
                                                    margin-left: 80px;
                                                    }""")
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        boxScrollArea.setGraphicsEffect(effect)
        self.generateMapWidget(clinicList)

        clinicNearbyLayout = QHBoxLayout()
        clinicNearbyLayout.addWidget(self.mapWidget, 5)
        clinicNearbyLayout.addWidget(boxScrollArea, 5)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.centralwidget)
        mainLayout.addLayout(clinicNearbyLayout)

        self.searchBar.raise_()

        self.setLayout(mainLayout)

    def updateMapButton(self,clinic,clinicList): 
        map = geoHelper.recenterMap((clinic.getClinicLat(), clinic.getClinicLon()))  # Return Folium Map
        geoHelper.addMarker(map, self.currLocation, 'We are here!', 'red', 'star')  # Current Loc
        self.generateClinicMarkers(map, clinicList)


        data = io.BytesIO()
        map.save(data, close_file=False)

        #https://stackoverflow.com/questions/4528347/clear-all-widgets-in-a-layout-in-pyqt
        for i in reversed(range(self.mapWidgetLayout.count())):
            widget = self.mapWidgetLayout.itemAt(i).widget()
            if widget and isinstance(widget, QWebEngineView):
                widget.deleteLater()

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())
        self.mapWidgetLayout.addWidget(webView)
    

    def clinicButtonFunction(self, clinic, patient):
        # update the clinic details page here according to button click
        self.clinicDetailsWindow = PatientClinicDetailsWindow(clinic, patient)

        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.frameLayout.addWidget(self.clinicDetailsWindow)
        self.frameLayoutManager.add(self.frameLayout.count() - 1)
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())


    def filterButtons(self):
        searchedText = self.searchBar.text().strip().lower()

        for clinicRow in self.clinicButtonList:
            button = clinicRow.itemAt(0).widget()
            text = button.text().lower()
            for i in range(clinicRow.count()):
                clinicRow.itemAt(i).widget().setVisible(searchedText in text)

    def generateMapWidget(self,clinicList):
        self.mapWidget = QWidget()
        self.mapWidget.setStyleSheet("background-color: #BCCAE0; border-radius: 10px;")
        self.mapWidgetLayout = QVBoxLayout(self.mapWidget)

        map = geoHelper.showMap(self.currLocation)  # Return Folium Map

        geoHelper.addMarker(map, self.currLocation, 'We are here!', 'red', 'star')  # Current Loc
        self.generateClinicMarkers(map,clinicList)
        data = io.BytesIO()
        map.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())

        self.mapWidgetLayout.setContentsMargins(20, 20, 20, 20)
        self.mapWidgetLayout.addWidget(webView)
    
    
    def generateClinicMarkers(self,map,clinicList):
        for clinics in clinicList:
            geoHelper.addMarker(map,(clinics.getClinicLat(),clinics.getClinicLon()),clinics.getClinicName()
                                ,'lightblue','home')
        return map
