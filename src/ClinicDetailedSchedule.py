import os
import sys
from datetime import datetime

from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize, QPoint
from PyQt5.QtGui import QFont, QPixmap, QIcon, QColor
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QApplication, QVBoxLayout, \
    QGraphicsDropShadowEffect
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

        self.headerTitle = QLabel(self.centralwidget)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        self.headerTitle.setFont(font)
        self.headerTitle.setObjectName("headerTitle")
        self.headerTitle.setText(f"{self.doctor.getDoctorName()} Schedule")
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

        self.timeSlotButtonList = [[QPushButton() for _ in range(WIDTH)] for _ in range(HEIGHT)]

        scheduleContainer = QLabel(self.centralwidget)
        scheduleContainer.setGeometry(QRect(5, 135, 915, 520))
        scheduleContainer.setStyleSheet("""QLabel {
                                        background: #D0BFFF;
                                        border-radius: 10px;
                                        }""")

        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=10, color=QColor("#120855")
        )
        scheduleContainer.setGraphicsEffect(effect)
        # header of the grid
        timeStart = 8
        timeEnd = 9
        timeSlotLabelXStart = 125
        for i in range(WIDTH):
            timeSlotLabel = QLabel(self.centralwidget)
            timeSlotLabel.setGeometry(QRect(timeSlotLabelXStart,175,95,55))
            timeSlotLabel.setStyleSheet("border: 1px solid black; border-radius: 3px; background-color: white;")
            timeSlotLabel.setAlignment(Qt.AlignCenter)
            timeSlotLabel.setText(str(timeStart) + ":00 - " + str(timeEnd)+ ":00")
            timeSlotLabel.raise_()
            timeSlotLabelXStart = timeSlotLabelXStart + 95
            timeStart = timeStart + 1
            timeEnd = timeStart + 1

        dayCellYStart = 230
        # side of the grid
        daysOfTheWeek = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        for i in range(HEIGHT):
            dayCell = QLabel(self.centralwidget)
            dayCell.setGeometry(QRect(30, dayCellYStart, 95, 55))
            dayCell.setStyleSheet("border: 1px solid black; border-radius: 3px; text-align: center; background-color: white")
            dayCell.setAlignment(Qt.AlignCenter)
            dayCell.raise_()
            dayCell.setText(daysOfTheWeek[i])
            dayCellYStart = dayCellYStart + 55

        tempButtonYStart = 175
        for h in range(HEIGHT):
            tempButtonXStart = 125
            tempButtonYStart = tempButtonYStart + 55
            for w in range(WIDTH):
                timeSlotButton = QPushButton(self.centralwidget)
                timeSlotButton.setGeometry(QRect(tempButtonXStart, tempButtonYStart, 95, 55))
                timeSlotButton.setStyleSheet("border: 1px solid black; border-radius: 3px; text-align: center; background-color: white;")
                timeSlotButton.raise_()
                tempButtonXStart = tempButtonXStart + 95
                self.timeSlotButtonList[h][w] = timeSlotButton
                timeSlotButton.setEnabled(False)


        self.setSchedule()


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

    def setSchedule(self):

        for row in self.timeSlotButtonList:
            for button in row:
                button.setStyleSheet(
                    "border: 1px solid black; border-radius: 3px; text-align: center; background-color: white")

        appointmentList = AppointmentRepository.getAppointmentsWeekly(self.doctor.getDoctorID())

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
                    self.timeSlotButtonList[row][col+(i-1)].setStyleSheet("border: 1px solid black; border-radius: 3px; text-align: center; background-color: green;")
                    self.timeSlotButtonList[row][col+(i-1)].setEnabled(True)
                    self.timeSlotButtonList[row][col+(i-1)].clicked.connect(lambda checked, appointment=appointment: self.gotoAppointment(appointment, self.doctor, self.clinic))

    def backButtonFunction(self):
        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.frameLayoutManager.back()
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())
