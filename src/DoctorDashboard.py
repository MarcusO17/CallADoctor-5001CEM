from PyQt5.QtCore import QSize, QDate
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import  QWidget, QLabel, QPushButton, QVBoxLayout, \
    QHBoxLayout,QSizePolicy

from .AccountPage import AccountPage
from .DoctorAppointmentDetails import DoctorAppointmentDetails
from .DoctorPatientHistory import DoctorPatientHistoryWindow
from .model import Appointment, AppointmentRepo, Patient
from .model.AppointmentRepo import AppointmentRepository
from .PageManager import PageManager, FrameLayoutManager


class DoctorDashboard(QWidget):
    def __init__(self, doctor):
        super().__init__()
        self.doctor = doctor
        self.setupUi()

    def setupUi(self):

        self.mainLayout = QHBoxLayout()
        self.rightLayout = QVBoxLayout()
        self.leftLayout = QVBoxLayout()

        self.generateSchedule()

        self.appointmentList = AppointmentRepository.getAppointmentsWeekly(self.doctor.getDoctorID())

        self.setSchedule()

        self.generateUpcomingAppointments()

        self.generateRecentPatients()

        self.leftLayout.addWidget(self.scheduleWidget, 3)
        spacer = QWidget()
        spacer.setFixedHeight(50)
        self.leftLayout.addWidget(spacer)
        self.upcomingAppointmentWidget.setFixedWidth(500)
        self.leftLayout.addWidget(self.upcomingAppointmentWidget, 7)

        self.dateLayout = QHBoxLayout()
        spacer = QWidget()
        spacer.setFixedWidth(230)
        self.dateLayout.addWidget(spacer)
        self.dateWidget = QLabel(f"Date: {QDate.currentDate().toString('dd-MM-yyyy')}")
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        self.dateWidget.setFont(font)
        self.dateWidget.setFixedSize(220,75)
        self.dateWidget.setStyleSheet("background-color: #BCCAE0; border-radius: 10px;")
        self.dateWidget.setContentsMargins(10, 10, 10, 10)

        self.dateLayout.addWidget(self.dateWidget)

        self.rightLayout.addLayout(self.dateLayout)

        spacer = QWidget()
        spacer.setFixedHeight(100)
        self.rightLayout.addWidget(spacer)
        self.rightLayout.addLayout(self.recentPatientSpacerLayout)

        self.mainLayout.addLayout(self.leftLayout, 7)
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

            row = date.weekday() + 1
            if endTime - startTime >= 1:
                duration = endTime - startTime
                col = startTime - 7
                for i in range(duration):
                    self.timeSlotButtonList[row][col + (i - 1)].setText("Appointment")
                    self.timeSlotButtonList[row][col + (i - 1)].setStyleSheet("background-color: green;")
                    self.timeSlotButtonList[row][col + (i - 1)].setEnabled(True)

    def generateSchedule(self):

        HEIGHT = 7
        WIDTH = 8

        self.timeSlotButtonList = [[QPushButton() for _ in range(WIDTH)] for _ in range(HEIGHT)]

        self.scheduleWidget = QWidget()
        self.scheduleWidget.setStyleSheet("background-color: #BCCAE0; border-radius: 10px;")
        scheduleLayout = QVBoxLayout(self.scheduleWidget)
        scheduleLayout.setSpacing(0)

        scheduleRowLayout = QHBoxLayout()
        scheduleTitle = QLabel()
        scheduleTitle.setFixedWidth(150)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        scheduleTitle.setFont(font)
        scheduleTitle.setText("Schedule")
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        scheduleRowLayout.addWidget(spacer)
        scheduleRowLayout.addWidget(scheduleTitle)
        scheduleLayout.addLayout(scheduleRowLayout)

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
            scheduleRowLayout.addWidget(timeSlotLabel)
            timeSlotLabel.setStyleSheet("border: 1px solid black; background-color: white;")
            timeSlotLabel.setText(str(timeStart) + ":00")
            timeStart = timeStart + 1

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        scheduleRowLayout.addWidget(spacer)
        scheduleLayout.addLayout(scheduleRowLayout)

        # side of the grid
        daysOfTheWeek = ["Sun", "Mon", "Tues", "Wed", "Thurs", "Fri", "Sat"]

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

    def generateUpcomingAppointments(self):

        self.upcomingAppointmentWidget = QWidget()
        self.upcomingAppointmentWidget.setStyleSheet("background-color: #BCCAE0; border-radius: 10px;")
        self.upcomingAppointmentLayout = QVBoxLayout(self.upcomingAppointmentWidget)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.upcomingAppointmentTitle = QLabel()
        self.upcomingAppointmentTitle.setFixedWidth(380)
        font = QFont()
        font.setFamily("Arial")
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

        #get 3 upcoming appointment here

        appointmentList = list()

        appointment1 = Appointment("A0001", "D00001", "C0001", "P0001", "Approved", "8:00", "9:00", "appointmentDate",
                                   "visitReason")
        appointment2 = Appointment("A0002", "D00002", "C0002", "P0002", "Completed", "8:00", "9:00", "appointmentDate",
                                   "visitReason")
        appointment3 = Appointment("A0003", "D00003", "C0003", "P0003", "Approved", "8:00", "9:00", "appointmentDate",
                                   "visitReason")

        appointmentList.append(appointment1)
        appointmentList.append(appointment2)
        appointmentList.append(appointment3)

        buttonFont = QFont()
        buttonFont.setFamily("Arial")
        buttonFont.setPointSize(20)
        buttonFont.setBold(True)
        buttonFont.setWeight(75)

        for count, appointment in enumerate(appointmentList):
            self.appointmentButton = QPushButton()
            self.appointmentButton.setText(f"{appointment.getAppointmentID()} - {appointment.getStartTime()}")
            self.appointmentButton.setStyleSheet("background-color: white; border-radius: 10px;")
            self.appointmentButton.setFont(buttonFont)
            self.appointmentButton.setFixedSize(QSize(300,70))
            self.appointmentButton.clicked.connect(
                lambda checked, appointment=appointment: self.appointmentButtonFunction(appointment, self.doctor))
            self.upcomingAppointmentLayout.addWidget(self.appointmentButton)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.upcomingAppointmentLayout.addWidget(spacer)

    def appointmentButtonFunction(self, appointment, doctor):
        self.doctorAppointmentDetails = DoctorAppointmentDetails(appointment, doctor)
        self.doctorAppointmentDetails.setMode(appointment.getAppointmentStatus())

        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        print(self.frameLayout.count())
        print(self.frameLayoutManager.size())
        self.frameLayout.addWidget(self.doctorAppointmentDetails)
        self.frameLayoutManager.add(self.frameLayout.count()-1)
        print(self.frameLayout.count())
        print(self.frameLayoutManager.size())
        print("top",self.frameLayoutManager.top())
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    def generateRecentPatients(self):

        self.recentPatientSpacerLayout = QHBoxLayout()
        spacer = QWidget()
        spacer.setFixedWidth(100)
        self.recentPatientSpacerLayout.addWidget(spacer)
        self.recentPatientWidget = QWidget()
        self.recentPatientWidget.setStyleSheet("background-color: #BCCAE0; border-radius: 10px;")
        self.recentPatientLayout = QVBoxLayout(self.recentPatientWidget)

        self.recentPatientSpacerLayout.addWidget(self.recentPatientWidget)

        self.recentPatientTitle = QLabel()
        self.recentPatientTitle.setFixedWidth(380)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.recentPatientTitle.setFont(font)
        self.recentPatientTitle.setText("Recent Patients")

        headerRow = QHBoxLayout()
        spacer = QWidget()
        spacer.setFixedWidth(200)
        headerRow.addWidget(spacer)
        headerRow.addWidget(self.recentPatientTitle)

        self.recentPatientLayout.addLayout(headerRow)
        self.recentPatientLayout.setContentsMargins(20, 20, 20, 20)

        # get 3 upcoming patient here
        patientList = list()

        patient1 = Patient("P0001", "patientname1", "patientAddress", "patientDOB", "patientBlood", "patientRace")
        patient2 = Patient("P0002", "patientname2", "patientAddress", "patientDOB", "patientBlood", "patientRace")
        patient3 = Patient("P0003", "patientname3", "patientAddress", "patientDOB", "patientBlood", "patientRace")

        patientList.append(patient1)
        patientList.append(patient2)
        patientList.append(patient3)

        buttonFont = QFont()
        buttonFont.setFamily("Arial")
        buttonFont.setPointSize(20)
        buttonFont.setBold(True)
        buttonFont.setWeight(75)

        for count, patient in enumerate(patientList):
            self.patientButton = QPushButton()
            self.patientButton.setText(patient.getPatientName())
            self.patientButton.setFont(buttonFont)
            self.patientButton.setStyleSheet("background-color: white; border-radius: 10px;")
            self.patientButton.setFixedSize(QSize(300, 70))
            self.patientButton.clicked.connect(lambda checked, patient=patient: self.patientButtonFunction(patient, self.doctor))
            self.recentPatientLayout.addWidget(self.patientButton)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.recentPatientLayout.addWidget(spacer)

    def patientButtonFunction(self, patient, doctor):
        # update the clinic details page here according to button click

        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.patientHistoryWindow = DoctorPatientHistoryWindow(patient, doctor)
        self.frameLayout.addWidget(self.patientHistoryWindow)
        self.frameLayoutManager.add(self.frameLayout.count() - 1)
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())