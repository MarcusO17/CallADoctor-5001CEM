import os
import sys
from datetime import datetime

from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QApplication, QGridLayout, QVBoxLayout, \
    QHBoxLayout, QSplitter
from PyQt5 import QtWidgets

from .AccountPage import AccountPage
from .DoctorAppointmentDetails import DoctorAppointmentDetails
from .model import Appointment
from .model.AppointmentRepo import AppointmentRepository
from .PageManager import PageManager


class DoctorDashboard(QWidget):
    def __init__(self, doctor):
        super().__init__()
        self.doctor = doctor
        self.pageManager = PageManager()
        self.setupUi()

    def setupUi(self):

        self.mainLayout = QHBoxLayout()
        self.rightLayout = QVBoxLayout()
        self.leftLayout = QVBoxLayout()

        HEIGHT = 7
        WIDTH = 8
        self.centralwidget = QWidget()

        self.timeSlotButtonList = [[QPushButton() for _ in range(WIDTH)] for _ in range(HEIGHT)]

        scheduleWidget = QWidget()
        scheduleLayout = QGridLayout(scheduleWidget)

        # header of the grid
        timeStart = 8
        timeEnd = 9
        for i in range(WIDTH):
            timeSlotLabel = QLabel()
            timeSlotLabel.setFixedSize(50,30)
            scheduleLayout.addWidget(timeSlotLabel, 0, i+1)
            timeSlotLabel.setStyleSheet("border: 1px solid black;")
            timeSlotLabel.setText(str(timeStart) + ":00")
            timeStart = timeStart + 1
            timeEnd = timeStart + 1

        # side of the grid
        daysOfTheWeek = ["Sun", "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat"]
        for i in range(HEIGHT):
            dayCell = QLabel()
            dayCell.setFixedSize(50, 30)
            scheduleLayout.addWidget(dayCell, i + 1, 0)
            dayCell.setStyleSheet("border: 1px solid black;")
            dayCell.setText(daysOfTheWeek[i])

        for h in range(HEIGHT):

            for w in range(WIDTH):
                timeSlotButton = QPushButton()
                timeSlotButton.setFixedSize(50, 30)
                scheduleLayout.addWidget(timeSlotButton, h + 1, w+1)
                timeSlotButton.setStyleSheet("border: 1px solid black;")
                self.timeSlotButtonList[h][w] = timeSlotButton
                timeSlotButton.setEnabled(False)

        appointmentList = AppointmentRepository.getAppointmentsWeekly(self.doctor.getDoctorID())

        self.setSchedule(appointmentList)

        self.upcomingAppointmentWidget = QWidget()
        self.upcomingAppointmentLayout = QVBoxLayout(self.upcomingAppointmentWidget)


        self.upcomingAppointmentTitle = QLabel()
        self.upcomingAppointmentTitle.setText("Upcoming Appointment")
        self.upcomingAppointmentLayout.addWidget(self.upcomingAppointmentTitle)

        self.leftLayout.addWidget(scheduleWidget, 3)
        self.leftLayout.addWidget(self.upcomingAppointmentWidget, 7)

        self.mainLayout.addLayout(self.leftLayout, 5)
        self.mainLayout.addLayout(self.rightLayout, 5)

        self.setLayout(self.mainLayout)

    def gotoAppointment(self, appointment, doctor):

        self.doctorAppointmentDetails = DoctorAppointmentDetails(appointment, doctor)
        self.doctorAppointmentDetails.setMode(appointment.getAppointmentStatus())
        self.pageManager.add(self.doctorAppointmentDetails)

    def setSchedule(self, appointmentList):

        for appointment in appointmentList:
            row = 0
            col = 0
            date = appointment.getAppointmentDate()
            startTime = appointment.getStartTime()
            endTime = appointment.getEndTime()

            startTimeTemp = startTime.split(":")  # HH:MM:SS
            startTime = int(startTimeTemp[0])

            print(endTime)
            endTimeTemp = endTime.split(":")  # HH:MM:SS
            endTime = int(endTimeTemp[0])

            # print(date)
            # dateTemp = dateTemp.split("-") #YYYY-MM-DD

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

    def goToAccountPage(self):
        self.accountPage = AccountPage()
        self.accountPage.setUser("Doctor", self.doctor)
        self.pageManager.add(self.accountPage)


