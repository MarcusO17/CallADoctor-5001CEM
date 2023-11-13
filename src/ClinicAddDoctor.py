import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize, QPoint
from PyQt5.QtGui import QFont, QPixmap, QIcon, QColor
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QScrollArea, QSizePolicy, QLineEdit, \
    QGraphicsDropShadowEffect
from PyQt5 import QtWidgets

from .AccountPage import AccountPage
from .ClinicDoctorDetails import ClinicDoctorDetails
from .model import Clinic
from .ClinicDetailedSchedule import ClinicDetailedSchedule
from .model import Doctor
from .model.DoctorRepo import DoctorRepository
from .PageManager import PageManager, FrameLayoutManager


class ClinicAddDoctor(QWidget):
    def __init__(self, clinic):
        super().__init__()
        self.clinic = clinic
        self.setupUi()

    def setupUi(self):
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        # this is the header (logo, title, my back button
        self.centralwidget = QWidget()

        self.headerTitle = QLabel(self.centralwidget)
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(28)
        self.headerTitle.setFont(font)
        self.headerTitle.setText("Add Doctor")
        self.headerTitle.setObjectName("headerTitle")
        self.headerTitle.setGeometry(QRect(80, 40, 700, 70))
        self.headerTitle.setAlignment(Qt.AlignCenter)
        self.headerTitle.setStyleSheet("""QLabel#headerTitle {
                                                    background: #D0BFFF;
                                                    border-radius: 10px;
                                                    }""")
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        self.headerTitle.setGraphicsEffect(effect)

        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setGeometry(QRect(800, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-back-64.png")
        self.backIcon = QIcon(filepath)
        self.backButton.setIconSize(QSize(70, 70))
        self.backButton.setIcon(self.backIcon)
        self.backButton.setObjectName("backButton")
        self.backButton.clicked.connect(self.backButtonFunction)
        self.backButton.setStyleSheet("""QPushButton#backButton {
                                                background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                                        stop: 0 rgba(10, 2, 85, 255), 
                                                                        stop: 1 rgba(59, 41, 168, 255));
                                                border-radius: 10px; color: white;

                                                }
                                                QPushButton#backButton:hover
                                                {
                                                  background-color: #7752FE;
                                                }""")
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        self.backButton.setGraphicsEffect(effect)

        self.searchBar = QLineEdit(self.centralwidget)
        self.searchBar.setGeometry(QRect(80, 120, 800, 40))
        self.searchBar.setPlaceholderText("   Search Bar")
        self.searchBar.textChanged.connect(self.filterButtons)
        self.searchBar.setStyleSheet("""QLineEdit {
                                                border-radius: 10px;
                                                border: 1px solid black;
                                                }""")

        self.buttonContainer = QWidget()
        self.buttonContainer.setObjectName("buttonContainer")
        self.buttonContainer.setStyleSheet("""QWidget#buttonContainer {
                                                    background: #D0BFFF;
                                                    border-radius: 10px;
                                                    margin-left: 100px;
                                                    }""")
        self.buttonContainer.setContentsMargins(20,20,20,20)
        self.buttonLayout = QVBoxLayout(self.buttonContainer)
        self.buttonLayout.setSpacing(20)

        boxScrollArea = QScrollArea()
        boxScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        boxScrollArea.setWidgetResizable(True)
        boxScrollArea.setObjectName("scrollArea")

        self.doctorList = list()

        self.generateDoctorButtons()

        boxScrollArea.setWidget(self.buttonContainer)
        boxScrollArea.setFixedSize(900, 500)
        boxScrollArea.setStyleSheet("""QScrollArea#scrollArea {
                                            background: #D0BFFF;
                                            border-radius: 10px;
                                            margin-left: 80px;
                                            }""")

        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        boxScrollArea.setGraphicsEffect(effect)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.centralwidget)
        mainLayout.addWidget(boxScrollArea)

        self.searchBar.raise_()

        self.setLayout(mainLayout)


    def doctorButtonFunction(self, doctor, clinic):
        self.doctorDetails = ClinicDoctorDetails(doctor, clinic)
        self.doctorDetails.setMode("Add")

        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.frameLayout.addWidget(self.doctorDetails)
        self.frameLayoutManager.add(self.frameLayout.count() - 1)
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    def backButtonFunction(self):
        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.frameLayoutManager.back()
        self.frameLayout.widget(self.frameLayoutManager.top()).generateDoctorButtons()
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    def filterButtons(self):
        searchedText = self.searchBar.text().strip().lower()

        for i in range(self.buttonLayout.count()):
            item = self.buttonLayout.itemAt(i)
            if item and isinstance(item.widget(), QPushButton):
                button = item.widget()
                text = button.text().lower()
                button.setVisible(searchedText in text)

    def generateDoctorButtons(self):

        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

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
        self.doctorList = DoctorRepository.getUnassignedDoctors()

        buttonFont = QFont()
        buttonFont.setFamily("Montserrat")
        buttonFont.setPointSize(20)

        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-doctor-64.png")
        doctorIcon = QIcon(filepath)

        for count, doctor in enumerate(self.doctorList):
            doctorButton = QPushButton()
            doctorButton.setText(f"    {doctor.getDoctorID()} - {doctor.getDoctorName()}")
            doctorButton.setFont(buttonFont)
            doctorButton.setIconSize(QSize(80, 80))
            doctorButton.setFixedSize(QSize(700, 100))
            doctorButton.setIcon(doctorIcon)
            doctorButton.clicked.connect(lambda checked, doctor=doctor: self.doctorButtonFunction(doctor, self.clinic))
            doctorButton.setStyleSheet("""QPushButton {
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
            doctorButton.setGraphicsEffect(effect)

            self.buttonLayout.addWidget(doctorButton)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.buttonLayout.addWidget(spacer)
