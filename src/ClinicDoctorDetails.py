import os
import sys
import typing
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize, QPoint
from PyQt5.QtGui import QFont, QPixmap, QIcon, QColor
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QHBoxLayout, \
    QApplication, \
    QScrollArea, QGraphicsDropShadowEffect
from PyQt5 import QtCore, QtWidgets

from .AccountPage import AccountPage
from .ClinicDetailedSchedule import ClinicDetailedSchedule
from .model import Appointment
from .model import Clinic
from .model import Doctor
from .model.DoctorRepo import DoctorRepository
from .PageManager import PageManager, FrameLayoutManager


class ClinicDoctorDetails(QWidget):

    def __init__(self, doctor, clinic):
        super().__init__()
        # set the information here
        self.clinic = clinic
        self.doctor = doctor
        self.setupUi()

    def setupUi(self):
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        self.centralwidget = QWidget()

        self.headerTitle = QLabel(self.centralwidget)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        self.headerTitle.setFont(font)
        self.headerTitle.setObjectName("headerTitle")
        self.headerTitle.setText(f"{self.doctor.getDoctorName()} Details")
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

        self.doctorNameTitle = QLabel(self.centralwidget)
        self.doctorNameTitle.setGeometry(QRect(80, 150, 400, 30))
        self.doctorNameTitle.setText("Name: ")

        self.doctorNameLabel = QLabel(self.centralwidget)
        self.doctorNameLabel.setGeometry(QRect(80, 180, 400, 50))
        self.doctorNameLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.doctorNameLabel.setText(self.doctor.getDoctorName())
        self.doctorNameLabel.setStyleSheet("""QLabel {
                                            border-radius: 10px;
                                            border: 1px solid black;
                                            background: white;
                                            }""")

        self.doctorIDTitle = QLabel(self.centralwidget)
        self.doctorIDTitle.setGeometry(QRect(80, 230, 400, 30))
        self.doctorIDTitle.setText("Doctor ID: ")

        self.doctorIDLabel = QLabel(self.centralwidget)
        self.doctorIDLabel.setGeometry(QRect(80, 260, 400, 50))
        self.doctorIDLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.doctorIDLabel.setText(self.doctor.getDoctorID())
        self.doctorIDLabel.setStyleSheet("""QLabel {
                                            border-radius: 10px;
                                            border: 1px solid black;
                                            background: white;
                                            }""")

        self.doctorICNumberTitle = QLabel(self.centralwidget)
        self.doctorICNumberTitle.setGeometry(QRect(80, 310, 400, 30))
        self.doctorICNumberTitle.setText("Doctor IC: ")

        self.doctorICNumber = QLabel(self.centralwidget)
        self.doctorICNumber.setGeometry(QRect(80, 340, 400, 50))
        self.doctorICNumber.setFrameShape(QtWidgets.QFrame.Box)
        self.doctorICNumber.setText(str(self.doctor.getDoctorICNumber()))
        self.doctorICNumber.setStyleSheet("""QLabel {
                                                border-radius: 10px;
                                                border: 1px solid black;
                                                background: white;
                                                }""")

        self.doctorTypeTitle = QLabel(self.centralwidget)
        self.doctorTypeTitle.setGeometry(QRect(80, 390, 400, 30))
        self.doctorTypeTitle.setText("Doctor Type: ")

        self.doctorTypeLabel = QLabel(self.centralwidget)
        self.doctorTypeLabel.setGeometry(QRect(80, 420, 400, 50))
        self.doctorTypeLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.doctorTypeLabel.setText(self.doctor.getDoctorType())
        self.doctorTypeLabel.setStyleSheet("""QLabel {
                                            border-radius: 10px;
                                            border: 1px solid black;
                                            background: white;
                                            }""")

        self.doctorContactTitle = QLabel(self.centralwidget)
        self.doctorContactTitle.setGeometry(QRect(80, 470, 400, 30))
        self.doctorContactTitle.setText("Doctor Contact: ")

        self.doctorContactLabel = QLabel(self.centralwidget)
        self.doctorContactLabel.setGeometry(QRect(80, 500, 400, 50))
        self.doctorContactLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.doctorContactLabel.setText(str(self.doctor.getDoctorContact()))
        self.doctorContactLabel.setStyleSheet("""QLabel {
                                                border-radius: 10px;
                                                border: 1px solid black;
                                                background: white;
                                                }""")

        self.doctorYearOfExperienceTitle = QLabel(self.centralwidget)
        self.doctorYearOfExperienceTitle.setGeometry(QRect(80, 550, 400, 30))
        self.doctorYearOfExperienceTitle.setText("Years of Experience: ")

        self.doctorYearOfExperienceLabel = QLabel(self.centralwidget)
        self.doctorYearOfExperienceLabel.setGeometry(QRect(80, 580, 400, 50))
        self.doctorYearOfExperienceLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.doctorYearOfExperienceLabel.setText(f"{self.doctor.getYearsOfExperience()} Years")
        self.doctorYearOfExperienceLabel.setStyleSheet("""QLabel {
                                                        border-radius: 10px;
                                                        border: 1px solid black;
                                                        background: white;
                                                        }""")

        self.scheduleButton = QPushButton(self.centralwidget)
        self.scheduleButton.setGeometry(QRect(550, 380, 325, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.scheduleButton.setFont(font)
        self.scheduleButton.setLayoutDirection(Qt.RightToLeft)
        self.scheduleButton.setText("Check Schedule")
        self.scheduleButton.clicked.connect(self.goToSchedule)
        self.scheduleButton.setStyleSheet("""QPushButton {
                                        background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                                stop: 0 rgba(10, 2, 85, 255), 
                                                                stop: 1 rgba(59, 41, 168, 255));
                                        border-radius: 10px; color: white;
                                        text-align: center; 
                                        color:white;
                                        }
                                        QPushButton:hover
                                        {
                                          background-color: #7752FE;
                                          text-align: center; 
                                          color:white;
                                        }""")

        self.scheduleButtonLabel = QLabel(self.centralwidget)
        self.scheduleButtonLabel.setGeometry(QRect(570, 405, 50, 50))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-calendar-64.png")
        self.scheduleButtonIcon = QPixmap(filepath)
        self.scheduleButtonIcon = self.scheduleButtonIcon.scaled(50, 50)
        self.scheduleButtonLabel.setPixmap(self.scheduleButtonIcon)

        self.scheduleButton.hide()
        self.scheduleButtonLabel.hide()

        self.removeDoctorButton = QPushButton(self.centralwidget)
        self.removeDoctorButton.setGeometry(QRect(550, 525, 325, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.removeDoctorButton.setFont(font)
        self.removeDoctorButton.setLayoutDirection(Qt.RightToLeft)
        self.removeDoctorButton.setText("Remove Doctor")
        self.removeDoctorButton.clicked.connect(self.removeDoctor)
        self.removeDoctorButton.setStyleSheet("""QPushButton {
                                            background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                                    stop: 0 rgba(10, 2, 85, 255), 
                                                                    stop: 1 rgba(59, 41, 168, 255));
                                            border-radius: 10px; color: white;
                                            text-align: center; 
                                            color:white;
                                            }
                                            QPushButton:hover
                                            {
                                              background-color: #7752FE;
                                              text-align: center; 
                                              color:white;
                                            }""")

        self.removeDoctorLabel = QLabel(self.centralwidget)
        self.removeDoctorLabel.setGeometry(QRect(570, 550, 50, 50))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-remove-64.png")
        self.removeDoctorIcon = QPixmap(filepath)
        self.removeDoctorIcon = self.removeDoctorIcon.scaled(50, 50)
        self.removeDoctorLabel.setPixmap(self.removeDoctorIcon)
        self.removeDoctorButton.hide()
        self.removeDoctorLabel.hide()

        self.addDoctorButton = QPushButton(self.centralwidget)
        self.addDoctorButton.setGeometry(QRect(550, 525, 325, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.addDoctorButton.setFont(font)
        self.addDoctorButton.setLayoutDirection(Qt.RightToLeft)
        self.addDoctorButton.setText("Add Doctor")
        self.addDoctorButton.clicked.connect(self.addDoctor)
        self.addDoctorButton.setStyleSheet("""QPushButton {
                                                background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                                        stop: 0 rgba(10, 2, 85, 255), 
                                                                        stop: 1 rgba(59, 41, 168, 255));
                                                border-radius: 10px; color: white;
                                                text-align: center; 
                                                color:white;
                                                }
                                                QPushButton:hover
                                                {
                                                  background-color: #7752FE;
                                                  text-align: center; 
                                                  color:white;
                                                }""")

        self.addDoctorLabel = QLabel(self.centralwidget)
        self.addDoctorLabel.setGeometry(QRect(570, 550, 50, 50))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-add-64.png")
        self.addDoctorIcon = QPixmap(filepath)
        self.addDoctorIcon = self.addDoctorIcon.scaled(50, 50)
        self.addDoctorLabel.setPixmap(self.addDoctorIcon)
        self.addDoctorButton.hide()
        self.addDoctorLabel.hide()

        self.informationBox = QLabel(self.centralwidget)
        self.informationBox.setGeometry(QRect(70, 120, 830, 550))
        self.informationBox.setStyleSheet("""QLabel {
                                        background: #D0BFFF;
                                        border-radius: 10px;
                                        }""")
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        self.informationBox.setGraphicsEffect(effect)

        self.removeDoctorButton.raise_()
        self.scheduleButton.raise_()
        self.removeDoctorLabel.raise_()
        self.scheduleButtonLabel.raise_()
        self.addDoctorButton.raise_()
        self.addDoctorLabel.raise_()
        self.doctorNameLabel.raise_()
        self.doctorNameTitle.raise_()
        self.doctorYearOfExperienceLabel.raise_()
        self.doctorYearOfExperienceTitle.raise_()
        self.doctorContactLabel.raise_()
        self.doctorContactTitle.raise_()
        self.doctorTypeLabel.raise_()
        self.doctorTypeTitle.raise_()
        self.doctorICNumberTitle.raise_()
        self.doctorIDLabel.raise_()
        self.doctorIDTitle.raise_()
        self.doctorICNumber.raise_()

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.centralwidget)

        self.setLayout(mainLayout)

    def goToSchedule(self):
        self.doctorSchedule = ClinicDetailedSchedule(self.doctor, self.clinic)

        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.frameLayout.addWidget(self.doctorSchedule)
        self.frameLayoutManager.add(self.frameLayout.count() - 1)
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    def removeDoctor(self):
        removeDoctorDialogBox = QMessageBox.question(self, "Remove Confirmation",
                                                          "Are you sure you want to remove this doctor from the doctor list?",
                                                          QMessageBox.Yes | QMessageBox.No)
        if removeDoctorDialogBox == QMessageBox.Yes:
            print(self.doctor.getDoctorName(), self.doctor.getClinicID())
            DoctorRepository.unassignDoctorClinic(self.doctor.getDoctorID())
            print(self.doctor.getDoctorName(), self.doctor.getClinicID())

            self.frameLayoutManager = FrameLayoutManager()
            self.frameLayout = self.frameLayoutManager.getFrameLayout()

            self.frameLayoutManager.back()
            self.frameLayout.widget(self.frameLayoutManager.top()).generateDoctorButtons()
            self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    def addDoctor(self):
        addDoctorDialogBox = QMessageBox.question(self, "Add Confirmation",
                                                          "Are you sure you want to Add this doctor to the doctor list?",
                                                          QMessageBox.Yes | QMessageBox.No)
        if addDoctorDialogBox == QMessageBox.Yes:
            print(self.doctor.getDoctorName(), self.doctor.getClinicID())
            print("THIS IS THE CLINIC ID", self.clinic.getClinicID())
            DoctorRepository.assignDoctorClinic(self.clinic.getClinicID(),self.doctor.getDoctorID())
            print(self.doctor.getDoctorName(), self.doctor.getClinicID())

            self.frameLayoutManager = FrameLayoutManager()
            self.frameLayout = self.frameLayoutManager.getFrameLayout()

            self.frameLayoutManager.back()
            self.frameLayout.widget(self.frameLayoutManager.top()).generateDoctorButtons()
            self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    def backButtonFunction(self):
        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.frameLayoutManager.back()
        self.frameLayout.widget(self.frameLayoutManager.top()).generateDoctorButtons()
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    def setMode(self, state):
        if state == "Remove":
            self.removeDoctorButton.show()
            self.removeDoctorLabel.show()
            self.addDoctorButton.hide()
            self.addDoctorLabel.hide()
            self.scheduleButton.show()
            self.scheduleButtonLabel.show()

        elif state == "Add":
            self.removeDoctorButton.hide()
            self.removeDoctorLabel.hide()
            self.addDoctorButton.show()
            self.addDoctorLabel.show()
            self.scheduleButton.hide()
            self.scheduleButtonLabel.hide()
