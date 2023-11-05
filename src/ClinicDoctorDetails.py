import os
import sys
import typing
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QHBoxLayout, \
    QApplication, \
    QScrollArea
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
        font.setBold(True)
        font.setWeight(75)
        self.headerTitle.setFont(font)
        self.headerTitle.setText(f"{self.doctor.getDoctorName()} Details")
        self.headerTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.headerTitle.setGeometry(QRect(100, 40, 800, 70))
        self.headerTitle.setAlignment(Qt.AlignCenter)
        self.headerTitle.setStyleSheet("margin-left: 20px; margin-right: 20px")

        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setFixedSize(70, 70)
        self.backButton.setGeometry(QRect(900, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\backbutton.png")
        self.backIcon = QIcon(filepath)
        self.backButton.setIconSize(QSize(70, 70))
        self.backButton.setIcon(self.backIcon)
        self.backButton.clicked.connect(self.backButtonFunction)

        self.doctorNameTitle = QLabel(self.centralwidget)
        self.doctorNameTitle.setGeometry(QRect(180, 200, 400, 30))
        self.doctorNameTitle.setText("Name: ")

        self.doctorNameLabel = QLabel(self.centralwidget)
        self.doctorNameLabel.setGeometry(QRect(180, 230, 400, 50))
        self.doctorNameLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.doctorNameLabel.setText(self.doctor.getDoctorName())

        self.doctorIDTitle = QLabel(self.centralwidget)
        self.doctorIDTitle.setGeometry(QRect(180, 280, 400, 30))
        self.doctorIDTitle.setText("Doctor ID: ")

        self.doctorIDLabel = QLabel(self.centralwidget)
        self.doctorIDLabel.setGeometry(QRect(180, 310, 400, 50))
        self.doctorIDLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.doctorIDLabel.setText(self.doctor.getDoctorID())

        self.doctorICNumberTitle = QLabel(self.centralwidget)
        self.doctorICNumberTitle.setGeometry(QRect(180, 360, 400, 30))
        self.doctorICNumberTitle.setText("Doctor IC: ")

        self.doctorICNumber = QLabel(self.centralwidget)
        self.doctorICNumber.setGeometry(QRect(180, 390, 400, 50))
        self.doctorICNumber.setFrameShape(QtWidgets.QFrame.Box)
        self.doctorICNumber.setText(str(self.doctor.getDoctorICNumber()))

        self.doctorTypeTitle = QLabel(self.centralwidget)
        self.doctorTypeTitle.setGeometry(QRect(180, 440, 400, 30))
        self.doctorTypeTitle.setText("Doctor Type: ")

        self.doctorTypeLabel = QLabel(self.centralwidget)
        self.doctorTypeLabel.setGeometry(QRect(180, 470, 400, 50))
        self.doctorTypeLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.doctorTypeLabel.setText(self.doctor.getDoctorType())

        self.doctorContactTitle = QLabel(self.centralwidget)
        self.doctorContactTitle.setGeometry(QRect(180, 520, 400, 30))
        self.doctorContactTitle.setText("Doctor Contact: ")

        self.doctorContactLabel = QLabel(self.centralwidget)
        self.doctorContactLabel.setGeometry(QRect(180, 550, 400, 50))
        self.doctorContactLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.doctorContactLabel.setText(str(self.doctor.getDoctorContact()))

        self.doctorYearOfExperienceTitle = QLabel(self.centralwidget)
        self.doctorYearOfExperienceTitle.setGeometry(QRect(180, 600, 400, 30))
        self.doctorYearOfExperienceTitle.setText("Years of Experience: ")

        self.doctorYearOfExperienceLabel = QLabel(self.centralwidget)
        self.doctorYearOfExperienceLabel.setGeometry(QRect(180, 630, 400, 50))
        self.doctorYearOfExperienceLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.doctorYearOfExperienceLabel.setText(f"{self.doctor.getYearsOfExperience()} Years")

        self.scheduleButton = QPushButton(self.centralwidget)
        self.scheduleButton.setGeometry(QRect(710, 400, 325, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.scheduleButton.setFont(font)
        self.scheduleButton.setLayoutDirection(Qt.RightToLeft)
        self.scheduleButton.setText("Check Schedule")
        self.scheduleButton.clicked.connect(self.goToSchedule)

        self.scheduleButtonLabel = QLabel(self.centralwidget)
        self.scheduleButtonLabel.setGeometry(QRect(730, 425, 50, 50))
        self.scheduleButtonLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.scheduleButtonIcon = QPixmap(filepath)
        self.scheduleButtonIcon = self.scheduleButtonIcon.scaled(50, 50)
        self.scheduleButtonLabel.setPixmap(self.scheduleButtonIcon)

        self.scheduleButton.hide()
        self.scheduleButtonLabel.hide()

        self.removeDoctorButton = QPushButton(self.centralwidget)
        self.removeDoctorButton.setGeometry(QRect(710, 545, 325, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.removeDoctorButton.setFont(font)
        self.removeDoctorButton.setLayoutDirection(Qt.RightToLeft)
        self.removeDoctorButton.setText("Remove Doctor")
        self.removeDoctorButton.clicked.connect(self.removeDoctor)

        self.removeDoctorLabel = QLabel(self.centralwidget)
        self.removeDoctorLabel.setGeometry(QRect(730, 570, 50, 50))
        self.removeDoctorLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.removeDoctorIcon = QPixmap(filepath)
        self.removeDoctorIcon = self.removeDoctorIcon.scaled(50, 50)
        self.removeDoctorLabel.setPixmap(self.removeDoctorIcon)
        self.removeDoctorButton.hide()
        self.removeDoctorLabel.hide()

        self.addDoctorButton = QPushButton(self.centralwidget)
        self.addDoctorButton.setGeometry(QRect(710, 545, 325, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.addDoctorButton.setFont(font)
        self.addDoctorButton.setLayoutDirection(Qt.RightToLeft)
        self.addDoctorButton.setText("Add Doctor")
        self.addDoctorButton.clicked.connect(self.addDoctor)

        self.addDoctorLabel = QLabel(self.centralwidget)
        self.addDoctorLabel.setGeometry(QRect(730, 570, 50, 50))
        self.addDoctorLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.addDoctorIcon = QPixmap(filepath)
        self.addDoctorIcon = self.addDoctorIcon.scaled(50, 50)
        self.addDoctorLabel.setPixmap(self.addDoctorIcon)
        self.addDoctorButton.hide()
        self.addDoctorLabel.hide()

        self.removeDoctorButton.raise_()
        self.scheduleButton.raise_()
        self.removeDoctorLabel.raise_()
        self.scheduleButtonLabel.raise_()
        self.addDoctorButton.raise_()
        self.addDoctorLabel.raise_()

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
