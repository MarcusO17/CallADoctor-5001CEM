import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea, QSizePolicy, QLineEdit
from PyQt5 import QtWidgets

from .ClinicAddDoctor import ClinicAddDoctor
from .ClinicDoctorDetails import ClinicDoctorDetails
from .model import Clinic
from .ClinicDetailedSchedule import ClinicDetailedSchedule
from .model import Doctor
from .model.DoctorRepo import DoctorRepository
from .PageManager import PageManager


class ClinicDoctorList(QMainWindow):
    def __init__(self, clinic):
        super().__init__()
        self.setWindowTitle("Doctor List")
        self.clinic = clinic
        self.pageManager = PageManager()
        self.setFixedWidth(1280)
        self.setFixedHeight(720)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        # this is the header (logo, title, my back button
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # header (probably reused in most files)
        self.topLeftLogo = QLabel(self.centralwidget)
        self.topLeftLogo.setFrameShape(QtWidgets.QFrame.Box)
        self.topLeftLogo.setGeometry(QRect(20, 10, 60, 60))

        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.topLeftLogoIcon = QPixmap(filepath)
        self.topLeftLogoIcon = self.topLeftLogoIcon.scaled(60, 60)
        self.topLeftLogo.setPixmap(self.topLeftLogoIcon)

        self.headerTitle = QLabel(self.centralwidget)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.headerTitle.setFont(font)
        self.headerTitle.setText("Doctor List")
        self.headerTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.headerTitle.setGeometry(QRect(200, 40, 800, 70))
        self.headerTitle.setAlignment(Qt.AlignCenter)
        self.headerTitle.setStyleSheet("margin-left: 20px; margin-right: 20px")

        self.myAccountButton = QPushButton(self.centralwidget)
        self.myAccountButton.setGeometry(QRect(1050, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.myAccountIcon = QIcon(filepath)
        self.myAccountButton.setIconSize(QSize(70, 70))
        self.myAccountButton.setIcon(self.myAccountIcon)

        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setGeometry(QRect(1150, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\backbutton.png")
        self.backIcon = QIcon(filepath)
        self.backButton.setIconSize(QSize(70, 70))
        self.backButton.setIcon(self.backIcon)
        self.backButton.clicked.connect(self.backButtonFunction)

        self.searchBar = QLineEdit(self.centralwidget)
        self.searchBar.setGeometry(QRect(200, 130, 800, 40))
        self.searchBar.setPlaceholderText("Search Bar")
        self.searchBar.textChanged.connect(self.filterButtons)

        self.addDoctorButton = QPushButton(self.centralwidget)
        #self.addDoctorButton.setGeometry(QRect(1000, 120, 120, 50))
        self.addDoctorButton.setGeometry(QRect(1100, 120, 120, 50))
        self.addDoctorButton.setText("Add Doctor")
        self.addDoctorButton.clicked.connect(self.addDoctorFunction)

        self.buttonContainer = QWidget()
        buttonLayout = QVBoxLayout(self.buttonContainer)
        self.buttonContainer.setContentsMargins(20,20,20,20)
        boxScrollArea = QScrollArea()
        boxScrollArea.setWidgetResizable(True)
        boxScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.doctorList = list()

        self.generateDoctorButtons()

        boxScrollArea.setWidget(self.buttonContainer)
        boxScrollArea.setFixedSize(1000,500)
        topSpacer = QWidget()
        topSpacer.setFixedHeight(150)
        topSpacer.setFixedWidth(50)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(topSpacer)
        mainLayout.addWidget(boxScrollArea)
        mainLayout.setAlignment(Qt.AlignHCenter)

        self.centralwidget.setLayout(mainLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(MainWindow)

    def doctorButtonFunction(self, doctor, clinic):
        self.doctorDetails = ClinicDoctorDetails(doctor, clinic)
        self.doctorDetails.setMode("Remove")
        self.pageManager.add(self.doctorDetails)

    def addDoctorFunction(self):
        self.addDoctorPage = ClinicAddDoctor(self.clinic)
        self.pageManager.add(self.addDoctorPage)

    def backButtonFunction(self):
        self.pageManager.goBack()

    def generateDoctorButtons(self):

        # delete and clear the buttons, generating back later
        for i in range(self.buttonContainer.layout().count()):
            widget = self.buttonContainer.layout().itemAt(0).widget()
            self.buttonContainer.layout().removeWidget(widget)
            print("in the loop ", i)
            if widget is not None:
                widget.deleteLater()
                print("deleting 1 widget")

        self.doctorList.clear()

        # Query and get the doctor list here
        self.doctorList = DoctorRepository.getDoctorListClinic(self.clinic.getClinicID())

        buttonFont = QFont()
        buttonFont.setFamily("Arial")
        buttonFont.setPointSize(28)
        buttonFont.setBold(True)
        buttonFont.setWeight(75)

        for count, doctor in enumerate(self.doctorList):
            doctorButton = QPushButton()
            doctorButton.setText(doctor.getDoctorID() + " - " + doctor.getDoctorName())
            doctorButton.setFont(buttonFont)
            doctorButton.setFixedSize(QSize(900, 150))
            doctorButton.clicked.connect(lambda checked, doctor=doctor: self.doctorButtonFunction(doctor, self.clinic))
            self.buttonContainer.layout().addWidget(doctorButton)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.buttonContainer.layout().addWidget(spacer)

    def filterButtons(self):
        searchedText = self.searchBar.text().strip().lower()

        for i in range(self.buttonContainer.layout().count()):
            item = self.buttonContainer.layout().itemAt(i)
            if item and isinstance(item.widget(), QPushButton):
                button = item.widget()
                text = button.text().lower()
                button.setVisible(searchedText in text)
