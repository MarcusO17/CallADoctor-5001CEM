import os
import sys
from datetime import datetime

from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QApplication, QVBoxLayout
from PyQt5 import QtWidgets

from .AccountPage import AccountPage
from .ClinicAppointmentDetails import ClinicAppointmentDetails
from .model import Appointment, Doctor
from .model.AppointmentRepo import AppointmentRepository
from .PageManager import PageManager, FrameLayoutManager


class ClinicDetailedSchedule(QWidget):
    def __init__(self, doctor, clinic):
        super().__init__()
        self.doctor = doctor
        self.clinic = clinic
        self.setupUi()

    def setupUi(self):
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
        HEIGHT = 7
        WIDTH = 8

        self.centralwidget = QWidget()

        self.homepageTitle = QLabel(self.centralwidget)
        self.homepageTitle.setGeometry(QRect(100, 40, 800, 70))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.homepageTitle.setFont(font)
        self.homepageTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.homepageTitle.setText("Doctor Schedule")
        self.homepageTitle.setAlignment(Qt.AlignCenter)

        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setGeometry(QRect(900, 40, 70, 70))
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

        appointmentList = AppointmentRepository.getAppointmentsWeekly(self.doctor.getDoctorID())
        self.setSchedule(appointmentList)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.centralwidget)

        self.setLayout(mainLayout)
    def gotoAppointment(self, appointment, doctor, clinic):

        self.clinicAppointmentDetails = ClinicAppointmentDetails(appointment, doctor, clinic)

        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.frameLayout.addWidget(self.clinicAppointmentDetails)
        self.frameLayoutManager.add(self.frameLayout.count() - 1)
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    def setSchedule(self, appointmentList):

        for appointment in appointmentList:
            row = 0
            col = 0
            date = appointment.getAppointmentDate()
            startTime = appointment.getStartTime()
            endTime = appointment.getEndTime()

            startTimeTemp = startTime.split(":") #HH:MM:SS
            startTime = int(startTimeTemp[0])

            print(endTime)
            endTimeTemp = endTime.split(":") #HH:MM:SS
            endTime = int(endTimeTemp[0])

            #print(date)
            #dateTemp = dateTemp.split("-") #YYYY-MM-DD

            row = date.weekday()+1
            if endTime - startTime >= 1:
                duration = endTime - startTime
                col = startTime - 7
                for i in range(duration):
                    self.timeSlotButtonList[row][col+(i-1)].setText("Appointment")
                    self.timeSlotButtonList[row][col+(i-1)].setStyleSheet("background-color: green;")
                    self.timeSlotButtonList[row][col+(i-1)].setEnabled(True)
                    self.timeSlotButtonList[row][col+(i-1)].clicked.connect(lambda checked, appointment=appointment: self.gotoAppointment(appointment, self.doctor, self.clinic))

    def backButtonFunction(self):
        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.frameLayoutManager.back()
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())
