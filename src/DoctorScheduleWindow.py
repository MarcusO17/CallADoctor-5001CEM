import os
import sys
from datetime import datetime

from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize, QPoint
from PyQt5.QtGui import QFont, QPixmap, QIcon, QColor
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QApplication, QGridLayout, QVBoxLayout, \
    QGraphicsDropShadowEffect
from PyQt5 import QtWidgets

from .AccountPage import AccountPage
from .DoctorAppointmentDetails import DoctorAppointmentDetails
from .model import Appointment
from .model.AppointmentRepo import AppointmentRepository
from .PageManager import PageManager, FrameLayoutManager


class DoctorScheduleWindow(QWidget):
    def __init__(self, doctor):
        super().__init__()
        self.setWindowTitle("Homepage")
        self.doctor = doctor
        self.pageManager = PageManager()
        self.setupUi()

    def setupUi(self):
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
        HEIGHT = 7
        WIDTH = 8
        self.centralwidget = QWidget()

        self.headerTitle = QLabel(self.centralwidget)
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(28)
        self.headerTitle.setFont(font)
        self.headerTitle.setText("My Schedule")
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

        # Qlabel background
        scheduleContainer = QLabel(self.centralwidget)
        scheduleContainer.setGeometry(QRect(5, 145, 915, 520))
        scheduleContainer.setStyleSheet("""QLabel {
                                                background: #D0BFFF;
                                                border-radius: 10px;
                                                }""")

        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=10, color=QColor("#120855")
        )
        scheduleContainer.setGraphicsEffect(effect)

        # creating 2d list of placeholder buttons
        self.timeSlotButtonList = [[QPushButton() for _ in range(WIDTH)] for _ in range(HEIGHT)]

        # header of the grid
        timeStart = 8
        timeEnd = 9
        timeSlotLabelXStart = 125
        for i in range(WIDTH):
            timeSlotLabel = QLabel(self.centralwidget)
            timeSlotLabel.setGeometry(QRect(timeSlotLabelXStart, 185, 95, 55))
            timeSlotLabel.setStyleSheet("border: 1px solid black; border-radius: 3px; background-color: white;")
            timeSlotLabel.setAlignment(Qt.AlignCenter)
            timeSlotLabel.setText(str(timeStart) + ":00 - " + str(timeEnd) + ":00")
            timeSlotLabel.raise_()
            timeSlotLabelXStart = timeSlotLabelXStart + 95
            timeStart = timeStart + 1
            timeEnd = timeStart + 1

        dayCellYStart = 240
        # side of the grid
        daysOfTheWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        for i in range(HEIGHT):
            dayCell = QLabel(self.centralwidget)
            dayCell.setGeometry(QRect(30, dayCellYStart, 95, 55))
            dayCell.setStyleSheet(
                "border: 1px solid black; border-radius: 3px; text-align: center; background-color: white")
            dayCell.setAlignment(Qt.AlignCenter)
            dayCell.raise_()
            dayCell.setText(daysOfTheWeek[i])
            dayCellYStart = dayCellYStart + 55

        tempButtonYStart = 185
        for h in range(HEIGHT):
            tempButtonXStart = 125
            tempButtonYStart = tempButtonYStart + 55
            for w in range(WIDTH):
                timeSlotButton = QPushButton(self.centralwidget)
                timeSlotButton.setGeometry(QRect(tempButtonXStart, tempButtonYStart, 95, 55))
                timeSlotButton.setStyleSheet(
                    "border: 1px solid black; border-radius: 3px; text-align: center; background-color: white;")
                timeSlotButton.raise_()
                tempButtonXStart = tempButtonXStart + 95
                self.timeSlotButtonList[h][w] = timeSlotButton
                timeSlotButton.setEnabled(False)

        self.appointmentList = list()

        self.setSchedule()

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.centralwidget)

        self.setLayout(mainLayout)

    # this method is triggered when any of the appointment button is clicked
    def gotoAppointment(self, appointment, doctor):

        self.doctorAppointmentDetails = DoctorAppointmentDetails(appointment, doctor)
        self.doctorAppointmentDetails.setMode(appointment.getAppointmentStatus())

        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.frameLayout.addWidget(self.doctorAppointmentDetails)
        self.frameLayoutManager.add(self.frameLayout.count() - 1)
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    # this methods sets the schedule according to the appointment they have this current week
    def setSchedule(self):

        self.appointmentList.clear()

        self.appointmentList = AppointmentRepository.getAppointmentsWeekly(self.doctor.getDoctorID())
        
        for appointment in self.appointmentList:
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

            row = date.weekday()
            if endTime - startTime >= 1:
                duration = endTime - startTime
                col = startTime - 7
                for i in range(duration):
                    self.timeSlotButtonList[row][col+(i-1)].setText("Appointment")
                    self.timeSlotButtonList[row][col+(i-1)].setStyleSheet("border: 1px solid black; border-radius: 3px; text-align: center; background-color: green;")
                    self.timeSlotButtonList[row][col+(i-1)].setEnabled(True)
                    self.timeSlotButtonList[row][col+(i-1)].clicked.connect(lambda checked, appointment=appointment: self.gotoAppointment(appointment, self.doctor))




