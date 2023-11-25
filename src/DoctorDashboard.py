import io
import os

from PyQt5.QtCore import QSize, QDate, QPoint, Qt
from PyQt5.QtGui import QFont, QIcon, QColor
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, \
    QHBoxLayout, QSizePolicy, QGraphicsDropShadowEffect

from .AccountPage import AccountPage
from .DoctorAppointmentDetails import DoctorAppointmentDetails
from .DoctorPatientHistory import DoctorPatientHistoryWindow
from .model import Appointment, AppointmentRepo, Patient, Clinic, geoHelper
from .model.AppointmentRepo import AppointmentRepository
from .PageManager import PageManager, FrameLayoutManager


class DoctorDashboard(QWidget):
    def __init__(self, doctor):
        super().__init__()
        self.doctor = doctor
        self.clinic = Clinic.getClinicfromID(self.doctor.getClinicID())
        self.currLocation = (self.clinic.getClinicLat(), self.clinic.getClinicLon())
        print(doctor.getDoctorID())
        self.setupUi()

    def setupUi(self):

        self.mainLayout = QHBoxLayout()
        self.rightLayout = QVBoxLayout()
        self.leftLayout = QVBoxLayout()

        self.generateSchedule()

        self.appointmentList = AppointmentRepository.getAppointmentsWeekly(self.doctor.getDoctorID())

        self.setSchedule()

        self.generateUpcomingAppointments()

        self.generateMapWidget()

        self.leftLayout.addWidget(self.mainScheduleWidget, 3)
        self.leftLayout.addWidget(self.mainMapWidget, 7)

        self.userInfoLayout = QHBoxLayout()
        spacer = QWidget()
        spacer.setFixedWidth(230)
        self.userInfoLayout.addWidget(spacer)
        self.userInfoWidget = QLabel(f"{self.doctor.getDoctorName()}")
        self.userInfoWidget.setObjectName("userInfoWidget")
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(15)
        self.userInfoWidget.setFont(font)
        self.userInfoWidget.setAlignment(Qt.AlignCenter)
        self.userInfoWidget.setFixedSize(220, 75)
        self.userInfoWidget.setStyleSheet("""QLabel#userInfoWidget {background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                        stop: 0 rgba(25, 4, 130, 255), 
                                                        stop: 1 rgba(119, 82, 254, 255)
                                                    );
                                                    border-radius: 10px;
                                                    text-align: center;
                                                    color: white;
                                                }""")

        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        self.userInfoWidget.setGraphicsEffect(effect)
        self.userInfoWidget.setContentsMargins(10, 10, 10, 10)

        self.userInfoLayout.addWidget(self.userInfoWidget)

        self.rightLayout.addLayout(self.userInfoLayout)

        spacer = QWidget()
        spacer.setFixedHeight(50)
        self.rightLayout.addWidget(spacer)
        self.upcomingAppointmentWidget.setFixedWidth(500)
        self.rightLayout.addWidget(self.upcomingAppointmentWidget)

        self.mainLayout.addLayout(self.leftLayout, 20)
        self.mainLayout.addLayout(self.rightLayout, 5)

        self.setLayout(self.mainLayout)

    def setSchedule(self):

        self.appointmentList.clear()
        self.appointmentList = AppointmentRepository.getAppointmentsWeekly(self.doctor.getDoctorID())

        for appointment in self.appointmentList:
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

            row = date.weekday()
            if endTime - startTime >= 1:
                duration = endTime - startTime
                col = startTime - 7
                for i in range(duration):
                    self.timeSlotButtonList[row][col + (i - 1)].setStyleSheet("background-color: green;")
                    self.timeSlotButtonList[row][col + (i - 1)].setEnabled(True)

    def generateSchedule(self):

        HEIGHT = 7
        WIDTH = 8

        self.timeSlotButtonList = [[QPushButton() for _ in range(WIDTH)] for _ in range(HEIGHT)]

        self.mainScheduleWidget = QWidget()
        self.mainScheduleLayout = QVBoxLayout(self.mainScheduleWidget)

        self.scheduleWidget = QWidget()
        self.scheduleWidget.setObjectName("ScheduleWidget")
        self.scheduleWidget.setStyleSheet("""QWidget#ScheduleWidget {background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                                stop: 0 rgba(25, 4, 130, 255), 
                                                                stop: 1 rgba(119, 82, 254, 255)
                                                            );
                                                            border-radius: 10px;
                                                            text-align: center;
                                                            color: white;
                                                        }""")
        scheduleLayout = QVBoxLayout(self.scheduleWidget)
        scheduleLayout.setSpacing(0)

        scheduleRowLayout = QHBoxLayout()
        scheduleTitle = QLabel()
        scheduleTitle.setFixedWidth(150)
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        scheduleTitle.setFont(font)
        scheduleTitle.setText("Schedule")
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        scheduleRowLayout.addWidget(spacer)
        scheduleRowLayout.addWidget(scheduleTitle)
        self.mainScheduleLayout.addLayout(scheduleRowLayout)

        scheduleRowLayout = QHBoxLayout()
        spacer = QWidget()
        spacer.setFixedHeight(20)
        scheduleRowLayout.addWidget(spacer)
        scheduleLayout.addLayout(scheduleRowLayout)

        scheduleRowLayout = QHBoxLayout()
        scheduleRowLayout.setSpacing(0)
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        scheduleRowLayout.addWidget(spacer)

        spacer = QWidget()
        spacer.setFixedSize(50, 30)
        scheduleRowLayout.addWidget(spacer)
        # header of the grid
        timeStart = 8
        for i in range(WIDTH):
            timeSlotLabel = QLabel()
            timeSlotLabel.setFixedSize(50, 30)
            timeSlotLabel.setAlignment(Qt.AlignCenter)
            scheduleRowLayout.addWidget(timeSlotLabel)
            timeSlotLabel.setStyleSheet("border: 1px solid black; background-color: white;")
            timeSlotLabel.setText(str(timeStart) + ":00")
            timeStart = timeStart + 1

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        scheduleRowLayout.addWidget(spacer)
        scheduleLayout.addLayout(scheduleRowLayout)

        # side of the grid
        daysOfTheWeek = ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"]

        for h in range(HEIGHT):
            scheduleRowLayout = QHBoxLayout()
            scheduleRowLayout.setSpacing(0)
            spacer = QWidget()
            spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
            scheduleRowLayout.addWidget(spacer)
            dayCell = QLabel()
            dayCell.setFixedSize(50, 30)
            dayCell.setText(daysOfTheWeek[h])
            dayCell.setStyleSheet("border: 1px solid black; background-color: white;")
            scheduleRowLayout.addWidget(dayCell)
            for w in range(WIDTH):
                timeSlotButton = QPushButton()
                timeSlotButton.setFixedSize(50, 30)
                scheduleRowLayout.addWidget(timeSlotButton)
                timeSlotButton.setStyleSheet("border: 1px solid black; background-color: white;")
                self.timeSlotButtonList[h][w] = timeSlotButton
                timeSlotButton.setEnabled(False)
            spacer = QWidget()
            spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
            scheduleRowLayout.addWidget(spacer)
            scheduleLayout.addLayout(scheduleRowLayout)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        scheduleLayout.addWidget(spacer)

        self.mainScheduleLayout.addWidget(self.scheduleWidget)

    def generateUpcomingAppointments(self):

        self.upcomingAppointmentWidget = QWidget()
        self.upcomingAppointmentWidget.setStyleSheet("background-color: transparent;")
        self.upcomingAppointmentLayout = QVBoxLayout(self.upcomingAppointmentWidget)
        self.upcomingAppointmentLayout.setSpacing(0)

        spacer = QWidget()
        spacer.setFixedWidth(40)
        self.upcomingAppointmentTitle = QLabel()
        self.upcomingAppointmentTitle.setFixedSize(415, 50)
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.upcomingAppointmentTitle.setFont(font)
        self.upcomingAppointmentTitle.setText("Upcoming Appointment")
        headerRow = QHBoxLayout()
        headerRow.addWidget(spacer)
        headerRow.addWidget(self.upcomingAppointmentTitle)

        self.upcomingAppointmentLayout.addLayout(headerRow)
        self.upcomingAppointmentLayout.setContentsMargins(20, 20, 20, 20)

        #get 4 upcoming appointment here

        appointmentList = AppointmentRepository.getDoctorDashboardAppointments(self.doctor.getDoctorID())

        fourAppointments = appointmentList[:4]

        buttonFont = QFont()
        buttonFont.setFamily("Montserrat")
        buttonFont.setPointSize(12)

        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-appointment-50.png")
        appointmentButtonIcon = QIcon(filepath)

        if len(fourAppointments) == 0:
            emptyAppointment = QLabel()
            emptyAppointment.setFont(buttonFont)
            emptyAppointment.setAlignment(Qt.AlignCenter)
            emptyAppointment.setText("No Appointment")
            emptyAppointment.setObjectName("emptyAppointment")
            emptyAppointment.setFixedSize(440,470)
            emptyAppointment.setStyleSheet("""QWidget#emptyAppointment {background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                                stop: 0 rgba(25, 4, 130, 255), 
                                                                stop: 1 rgba(119, 82, 254, 255)
                                                            );
                                                            border-radius: 10px;
                                                            text-align: center;
                                                            color: white;
                                                        }""")
            self.upcomingAppointmentLayout.addWidget(emptyAppointment)
        else:
            for count, appointment in enumerate(fourAppointments):
                buttonRow = QHBoxLayout()
                spacer = QWidget()
                spacer.setFixedSize(60, 120)
                buttonRow.addWidget(spacer)
                self.appointmentButton = QPushButton()
                self.appointmentButton.setText(f"{appointment.getAppointmentID()} - {appointment.getStartTime()}")
                self.appointmentButton.setObjectName("appointmentButton")
                self.appointmentButton.setStyleSheet("""QPushButton#appointmentButton {
                                                                            background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                                                stop: 0 rgba(10, 2, 85, 255), 
                                                                                stop: 1 rgba(59, 41, 168, 255)
                                                                            );
                                                                            border-radius: 10px; color: white;
                                                                        }
                                                                        QPushButton#appointmentButton:hover
                                                                        {
                                                                          background-color: #7752FE;}""")
                self.appointmentButton.setFont(buttonFont)
                self.appointmentButton.setFixedSize(QSize(350, 100))
                self.appointmentButton.setIcon(appointmentButtonIcon)
                self.appointmentButton.setIconSize(QSize(30, 30))
                self.appointmentButton.clicked.connect(
                    lambda checked, appointment=appointment: self.appointmentButtonFunction(appointment, self.doctor))

                buttonRow.addWidget(self.appointmentButton)
                self.upcomingAppointmentLayout.addLayout(buttonRow)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.upcomingAppointmentLayout.addWidget(spacer)

    def appointmentButtonFunction(self, appointment, doctor):
        self.doctorAppointmentDetails = DoctorAppointmentDetails(appointment, doctor)
        self.doctorAppointmentDetails.setMode(appointment.getAppointmentStatus())

        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.frameLayout.addWidget(self.doctorAppointmentDetails)
        self.frameLayoutManager.add(self.frameLayout.count()-1)
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    def generateMapWidget(self):

        self.mainMapWidget = QWidget()
        self.mainMapLayout = QVBoxLayout(self.mainMapWidget)

        self.mapWidget = QWidget()
        self.mapWidget.setObjectName("mapWidget")
        self.mapWidget.setStyleSheet("""QWidget#mapWidget {background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                                        stop: 0 rgba(25, 4, 130, 255), 
                                                                        stop: 1 rgba(119, 82, 254, 255)
                                                                    );
                                                                    border-radius: 10px;
                                                                    text-align: center;
                                                                    color: white;
                                                                }""")
        self.mapWidgetLayout = QVBoxLayout(self.mapWidget)

        self.widgetTitle = QLabel()
        self.widgetTitle.setFixedSize(80, 40)
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.widgetTitle.setFont(font)
        self.widgetTitle.setText("Map")

        headerRow = QHBoxLayout()
        spacer = QWidget()
        spacer.setFixedSize(500,1)
        headerRow.addWidget(spacer)
        headerRow.addWidget(self.widgetTitle)

        self.mapWidgetLayout.setContentsMargins(20, 20, 20, 20)

        self.mainMapLayout.addLayout(headerRow)

        print(self.currLocation)

        if self.currLocation == ('',''):
            #Center of world
            map = geoHelper.showMap((32.7502,114.7655))
        else:
            map = geoHelper.showMap(self.currLocation)  # Return Folium Map

            geoHelper.addMarker(map, self.currLocation, 'We are here!', 'red', 'star')  # Current Loc
            map = self.generatePatientMarkers(map=map)

        data = io.BytesIO()
        map.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())

        self.mapWidgetLayout.addWidget(webView)
        self.mainMapLayout.addWidget(self.mapWidget)

    def generatePatientMarkers(self,map):
        patientsWeekly =  AppointmentRepository.getPatientLocations(self.clinic.getClinicID())
        for patients in patientsWeekly:
            geoHelper.addMarker(map,(patients.getPatientLat(),patients.getPatientLon()),patients.getPatientAddress()
                                ,'lightblue','home')
        return map

    def patientButtonFunction(self, patient, doctor):
        # update the clinic details page here according to button click

        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.patientHistoryWindow = DoctorPatientHistoryWindow(patient, doctor)
        self.frameLayout.addWidget(self.patientHistoryWindow)
        self.frameLayoutManager.add(self.frameLayout.count() - 1)
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())