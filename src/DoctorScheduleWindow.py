import os
import sys
from datetime import datetime

from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QApplication, QGridLayout, QVBoxLayout
from PyQt5 import QtWidgets

from .DoctorAppointmentDetails import DoctorAppointmentDetails
from .model import Appointment
from .PageManager import PageManager



class DoctorScheduleWindow(QMainWindow):
    def __init__(self, doctor):
        super().__init__()
        self.setWindowTitle("Homepage")
        self.doctor = doctor
        self.setFixedWidth(1280)
        self.setFixedHeight(720)
        self.pageManager = PageManager()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Doctor Schedule")
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
        HEIGHT = 7
        WIDTH = 8

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.topLeftLogo = QLabel(self.centralwidget)
        self.topLeftLogo.setGeometry(QRect(20, 10, 60, 60))
        self.topLeftLogo.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.topLeftLogoIcon = QPixmap(filepath)
        self.topLeftLogoIcon = self.topLeftLogoIcon.scaled(60, 60)
        self.topLeftLogo.setPixmap(self.topLeftLogoIcon)

        self.homepageTitle = QLabel(self.centralwidget)
        self.homepageTitle.setGeometry(QRect(200, 40, 800, 70))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.homepageTitle.setFont(font)
        self.homepageTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.homepageTitle.setText("Doctor Schedule")
        self.homepageTitle.setAlignment(Qt.AlignCenter)

        self.myAccountButton = QPushButton(self.centralwidget)
        self.myAccountButton.setGeometry(QRect(1050, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.myAccountIcon = QIcon(filepath)
        self.myAccountButton.setIconSize(QSize(70,70))
        self.myAccountButton.setIcon(self.myAccountIcon)

        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setGeometry(QRect(1150, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\backbutton.png")
        self.backIcon = QIcon(filepath)
        self.backButton.setIconSize(QSize(70, 70))
        self.backButton.setIcon(self.backIcon)
        self.backButton.clicked.connect(self.backButtonFunction)

        self.timeSlotButtonList = [[QPushButton() for _ in range(WIDTH)] for _ in range(HEIGHT)]

        # header of the grid
        timeStart = 8
        timeEnd = 9
        timeSlotLabelXStart = 275
        for i in range(WIDTH):
            timeSlotLabel = QLabel(self.centralwidget)
            timeSlotLabel.setGeometry(QRect(timeSlotLabelXStart,150,100,60))
            timeSlotLabel.setStyleSheet("border: 1px solid black;")
            timeSlotLabel.setText(str(timeStart) + ":00 - " + str(timeEnd)+ ":00")
            timeSlotLabelXStart = timeSlotLabelXStart + 100
            timeStart = timeStart + 1
            timeEnd = timeStart + 1

        dayCellYStart = 210
        # side of the grid
        daysOfTheWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        for i in range(HEIGHT):
            dayCell = QLabel(self.centralwidget)
            dayCell.setGeometry(QRect(175, dayCellYStart, 100, 60))
            dayCell.setStyleSheet("border: 1px solid black;")
            dayCell.setText(daysOfTheWeek[i])
            dayCellYStart = dayCellYStart + 60

        tempButtonYStart = 150
        for h in range(HEIGHT):
            tempButtonXStart = 275
            tempButtonYStart = tempButtonYStart + 60
            for w in range(WIDTH):
                timeSlotButton = QPushButton(self.centralwidget)
                timeSlotButton.setGeometry(QRect(tempButtonXStart, tempButtonYStart, 100, 60))
                timeSlotButton.setStyleSheet("border: 1px solid black;")
                tempButtonXStart = tempButtonXStart + 100
                self.timeSlotButtonList[h][w] = timeSlotButton
                timeSlotButton.setEnabled(False)

        appointmentList = list()

        # put query and create the appointment objects here

        appointment1 = Appointment("appointment1", "doctor1", "clinicID", "patient1", "Approved", "13:00", "14:00", "24-10-2023",
                                   "light fever")
        appointment2 = Appointment("appointment2", "doctor1", "clinicID", "patient2", "Completed", "8:00", "9:00", "25-10-2023",
                                   "light fever")
        appointment3 = Appointment("appointment3", "doctor1", "clinicID", "patient3", "Approved", "8:00", "9:00", "28-10-2023",
                                   "light fever")

        appointmentList.append(appointment1)
        appointmentList.append(appointment2)
        appointmentList.append(appointment3)

        self.setSchedule(appointmentList)

        MainWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(MainWindow)

    def gotoAppointment(self, appointment, doctor):

        self.doctorAppointmentDetails = DoctorAppointmentDetails(appointment, doctor)
        self.doctorAppointmentDetails.setMode(appointment.getAppointmentStatus())
        self.pageManager.add(self.doctorAppointmentDetails)

    def setSchedule(self, appointmentList):

        for appointment in appointmentList:
            row = 0
            col = 0
            dateTemp = appointment.getAppointmentDate()
            startTime = appointment.getStartTime()
            endTime = appointment.getEndTime()

            startTimeTemp = startTime.split(":")
            startTime = int(startTimeTemp[0])

            endTimeTemp = endTime.split(":")
            endTime = int(endTimeTemp[0])

            dateTemp = dateTemp.split("-")
            print(dateTemp)

            date = datetime(int(dateTemp[2]), int(dateTemp[1]), int(dateTemp[0]))

            row = date.weekday() + 1
            if endTime - startTime >= 1:
                duration = endTime - startTime
                col = startTime - 7
                for i in range(duration):
                    self.timeSlotButtonList[row][col + (i - 1)].setText("Appointment")
                    self.timeSlotButtonList[row][col + (i - 1)].setStyleSheet("background-color: green;")
                    self.timeSlotButtonList[row][col + (i - 1)].setEnabled(True)
                    self.timeSlotButtonList[row][col + (i - 1)].clicked.connect(
                        lambda checked, appointment=appointment: self.gotoAppointment(appointment, self.doctor))

    def backButtonFunction(self):
        self.pageManager.goBack()



