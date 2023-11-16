import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize, QPoint
from PyQt5.QtGui import QFont, QPixmap, QIcon, QColor
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea, QSizePolicy, QGraphicsDropShadowEffect, QLineEdit
from PyQt5 import QtWidgets
from .AccountPage import AccountPage
from .model import Patient,Doctor
from .DoctorPatientHistory import DoctorPatientHistoryWindow
from .PageManager import PageManager, FrameLayoutManager


class DoctorPatientRecordWindow(QWidget):
    def __init__(self, doctor):
        super().__init__()
        self.doctor = doctor
        self.setWindowTitle("Patient Record (Doctor)")
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
        self.headerTitle.setFont(font)
        self.headerTitle.setText("Doctor List")
        self.headerTitle.setObjectName("headerTitle")
        self.headerTitle.setGeometry(QRect(80, 40, 800, 70))
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
        self.searchBar.setGeometry(QRect(80, 120, 800, 40))
        self.searchBar.setPlaceholderText("   Search Bar")
        self.searchBar.textChanged.connect(self.filterButtons)
        self.searchBar.setStyleSheet("""QLineEdit {
                                                border-radius: 10px;
                                                border: 1px solid black;
                                                }""")

        self.buttonContainer = QWidget()
        self.buttonContainer.setContentsMargins(20,20,20,20)
        self.buttonContainer.setObjectName("buttonContainer")
        self.buttonContainer.setStyleSheet("""QWidget#buttonContainer {
                                                    background: #D0BFFF;
                                                    border-radius: 10px;
                                                    margin-left: 100px;
                                                    }""")

        buttonLayout = QVBoxLayout(self.buttonContainer)
        buttonLayout.setSpacing(20)

        boxScrollArea = QScrollArea()
        boxScrollArea.setObjectName("scrollArea")
        boxScrollArea.setWidgetResizable(True)
        boxScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        patientList = Doctor.getDoctorPastPatients(self.doctor.getDoctorID())

        buttonFont = QFont()
        buttonFont.setFamily("Montserrat")
        buttonFont.setPointSize(20)

        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-document-60.png")
        recordIcon = QIcon(filepath)

        for count, patient in enumerate(patientList):
            self.patientButton = QPushButton()
            self.patientButton.setText(patient.getPatientID() + " - " + patient.getPatientName())
            self.patientButton.setFont(buttonFont)
            self.patientButton.setIconSize(QSize(80, 80))
            self.patientButton.setFixedSize(QSize(700, 100))
            self.patientButton.setIcon(recordIcon)
            self.patientButton.setStyleSheet("""QPushButton {
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
            self.patientButton.setGraphicsEffect(effect)
            self.patientButton.clicked.connect(lambda checked, patient=patient: self.patientButtonFunction(patient, self.doctor))
            self.buttonContainer.layout().addWidget(self.patientButton)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.buttonContainer.layout().addWidget(spacer)

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

        self.setLayout(mainLayout)

    def patientButtonFunction(self, patient, doctor):
        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()
        # update the clinic details page here according to button click
        self.patientHistoryWindow = DoctorPatientHistoryWindow(patient, doctor)
        self.frameLayout.addWidget(self.patientHistoryWindow)
        self.frameLayoutManager.add(self.frameLayout.count() - 1)
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    def filterButtons(self):
        searchedText = self.searchBar.text().strip().lower()

        for i in range(self.buttonContainer.layout().count()):
            item = self.buttonContainer.layout().itemAt(i)
            if item and isinstance(item.widget(), QPushButton):
                button = item.widget()
                text = button.text().lower()
                button.setVisible(searchedText in text)

