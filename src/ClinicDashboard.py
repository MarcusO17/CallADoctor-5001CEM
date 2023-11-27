import os
from PyQt5.QtCore import QSize, QDate, Qt, QPoint
from PyQt5.QtGui import QFont, QIcon, QPixmap, QImage, QColor
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, \
    QHBoxLayout, QSizePolicy, QGraphicsDropShadowEffect

from .AccountPage import AccountPage
from .ClinicDetailedSchedule import ClinicDetailedSchedule
from .ClinicRequestDetails import ClinicRequestDetails
from .DoctorAppointmentDetails import DoctorAppointmentDetails
from .DoctorPatientHistory import DoctorPatientHistoryWindow
from .model import Appointment, AppointmentRepo, Patient
from .model.AppointmentRepo import AppointmentRepository
from .PageManager import PageManager, FrameLayoutManager
from .model.DoctorRepo import DoctorRepository
from .model.graphs import graphGen


class ClinicDashboard(QWidget):
    def __init__(self, clinic):
        super().__init__()
        self.clinic = clinic
        self.setupUi()

    def setupUi(self):
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        self.mainLayout = QHBoxLayout()
        self.rightLayout = QVBoxLayout()
        self.leftLayout = QVBoxLayout()
        self.doctorList = list()
        self.unassignedAppointmentList = list()
        self.requestReviewButtons = QVBoxLayout()
        self.doctorWidgetsRow = QHBoxLayout()

        self.generateDoctorWidgets()

        self.generateRequestButtons()

        self.generateGraphWidget()

        self.leftLayout.addWidget(self.doctorWidgets, 3)
        spacer = QWidget()
        spacer.setFixedHeight(25)
        self.leftLayout.addWidget(spacer)
        self.leftLayout.addWidget(self.graphWidget, 7)

        self.userInfoLayout = QHBoxLayout()
        spacer = QWidget()
        spacer.setFixedWidth(180)
        self.userInfoLayout.addWidget(spacer)
        self.userInfoWidget = QLabel(f"{self.clinic.getClinicName()}")
        self.userInfoWidget.setObjectName("userInfoWidget")
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(15)
        self.userInfoWidget.setFont(font)
        self.userInfoWidget.setAlignment(Qt.AlignCenter)
        self.userInfoWidget.setFixedSize(220,75)
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
        spacer.setFixedHeight(20)
        spacer.setFixedWidth(0)
        self.rightLayout.addWidget(spacer)
        #self.requestReviewWidget.setFixedWidth(500)
        self.rightLayout.addWidget(self.requestReviewWidget)

        self.mainLayout.addLayout(self.leftLayout, 10)
        self.mainLayout.addLayout(self.rightLayout, 5)

        self.setLayout(self.mainLayout)

    def generateDoctorWidgets(self):

        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        self.doctorWidgets = QWidget()
        self.doctorWidgets.setStyleSheet("background-color: transparent;")
        doctorWidgetsLayout = QVBoxLayout(self.doctorWidgets)

        while self.doctorWidgetsRow.count():
            item = self.doctorWidgetsRow.takeAt(0)
            widget = item.widget()
            if widget:
                self.doctorWidgetsRow.removeItem(item)
                widget.deleteLater()

        self.doctorList.clear()

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.doctorTitle = QLabel()
        self.doctorTitle.setFixedWidth(140)
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(20)
        font.setWeight(75)
        self.doctorTitle.setFont(font)
        self.doctorTitle.setText("Doctors")
        headerRow = QHBoxLayout()
        headerRow.addWidget(spacer)
        headerRow.addWidget(self.doctorTitle)

        doctorWidgetsLayout.addLayout(headerRow)


        self.doctorList = DoctorRepository.getDoctorListClinic(self.clinic.getClinicID())

        threeDoctorList = self.doctorList[:3]

        buttonFont = QFont()
        buttonFont.setFamily("Montserrat")
        buttonFont.setPointSize(20)

        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-doctor-64.png")
        doctorIcon = QIcon(filepath)

        if len(threeDoctorList) == 0:
            print("trigger no doctor label")
            emptyDoctor = QLabel()
            emptyDoctor.setFont(buttonFont)
            emptyDoctor.setAlignment(Qt.AlignCenter)
            emptyDoctor.setText("No Doctors")
            emptyDoctor.setObjectName("emptyDoctor")
            emptyDoctor.setFixedSize(450, 100)
            emptyDoctor.setStyleSheet("""QLabel#emptyDoctor {background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                                                            stop: 0 rgba(25, 4, 130, 255), 
                                                                                            stop: 1 rgba(119, 82, 254, 255)
                                                                                        );
                                                                                        border-radius: 10px;
                                                                                        text-align: center;
                                                                                        color: white;
                                                                                    }""")
            self.doctorWidgetsRow.addWidget(emptyDoctor)

        else:
            for count, doctor in enumerate(threeDoctorList):
                doctorButton = QPushButton()
                doctorButton.setFixedSize(QSize(100, 100))
                doctorButton.setIconSize(QSize(45, 45))
                doctorButton.setIcon(doctorIcon)
                doctorButton.clicked.connect(lambda checked, doctor=doctor: self.doctorButtonFunction(doctor, self.clinic))

                font = QFont()
                font.setFamily("Montserrat")
                font.setPointSize(12)

                doctorLabel = QLabel()
                doctorLabel.setFont(font)
                doctorNameSliced = doctor.getDoctorName()[:8]
                doctorLabel.setText(f"{doctorNameSliced}..")
                doctorLabel.setStyleSheet("color: white;")

                doctorWidget = QWidget()
                effect = QGraphicsDropShadowEffect(
                    offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
                )
                doctorWidget.setGraphicsEffect(effect)
                doctorWidget.setFixedSize(125, 125)
                doctorWidget.setObjectName("doctorButton")
                doctorWidget.setStyleSheet("""QWidget#doctorButton {
                                                background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                    stop: 0 rgba(10, 2, 85, 255), 
                                                    stop: 1 rgba(59, 41, 168, 255)
                                                );
                                                border-radius: 10px; padding-left: 5px; padding-bottom: 10px;
                                            }
                                            QWidget#doctorButton:hover
                                                {
                                                  background-color: #7752FE;
                                                  text-align: left; 
                                                  padding-left: 20px;}""")
                doctorLayout = QVBoxLayout(doctorWidget)
                doctorLayout.addWidget(doctorButton)
                doctorLayout.addWidget(doctorLabel)

                self.doctorWidgetsRow.addWidget(doctorWidget)

        doctorWidgetsLayout.addLayout(self.doctorWidgetsRow)

    def doctorButtonFunction(self, doctor, clinic):
        self.doctorSchedule = ClinicDetailedSchedule(doctor, clinic)

        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.frameLayout.addWidget(self.doctorSchedule)
        self.frameLayoutManager.add(self.frameLayout.count() - 1)
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())


    def generateRequestButtons(self):

        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        self.requestReviewWidget = QWidget()
        self.requestReviewWidget.setStyleSheet("background-color: transparent;")
        self.requestReviewLayout = QVBoxLayout(self.requestReviewWidget)
        self.requestReviewLayout.setSpacing(0)

        for i in range(self.requestReviewButtons.count()):
            widget = self.requestReviewButtons.itemAt(0).widget()
            self.requestReviewButtons.removeWidget(widget)
            print("in the loop request review ", i)
            if widget is not None:
                widget.deleteLater()
                print("deleting 1 widget request review")

        self.unassignedAppointmentList.clear()

        spacer = QWidget()
        spacer.setFixedWidth(110)
        self.requestReviewTitle = QLabel()
        self.requestReviewTitle.setFixedSize(270,50)
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(20)
        font.setWeight(75)
        self.requestReviewTitle.setFont(font)
        self.requestReviewTitle.setText("Request Review")
        headerRow = QHBoxLayout()
        headerRow.addWidget(spacer)
        headerRow.addWidget(self.requestReviewTitle)

        self.requestReviewLayout.addLayout(headerRow)
        self.requestReviewLayout.setContentsMargins(20, 20, 20, 20)

        self.unassignedAppointmentList.clear()

        #get 3 reviews here
        buttonFont = QFont()
        buttonFont.setFamily("Montserrat")
        buttonFont.setPointSize(12)

        self.unassignedAppointmentList = AppointmentRepository.getAppointmentsPending(self.clinic.getClinicID())

        threeAppointments = self.unassignedAppointmentList[:3]

        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-document-60.png")

        requestIcon = QIcon(filepath)

        if len(threeAppointments) == 0:
            emptyReviews = QLabel()
            emptyReviews.setFont(buttonFont)
            emptyReviews.setAlignment(Qt.AlignCenter)
            emptyReviews.setText("Empty Reviews")
            emptyReviews.setObjectName("emptyReviews")
            emptyReviews.setFixedSize(440, 470)
            emptyReviews.setStyleSheet("""QWidget#emptyReviews {background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                                            stop: 0 rgba(25, 4, 130, 255), 
                                                                            stop: 1 rgba(119, 82, 254, 255)
                                                                        );
                                                                        border-radius: 10px;
                                                                        text-align: center;
                                                                        color: white;
                                                                    }""")

            self.requestReviewButtons.addWidget(emptyReviews)
        else:
            for count, request in enumerate(threeAppointments):

                buttonRowWidget = QWidget()
                buttonRow = QHBoxLayout(buttonRowWidget)
                spacer = QWidget()
                spacer.setFixedWidth(0)
                spacer.setFixedHeight(120)
                buttonRow.addWidget(spacer)
                self.requestButton = QPushButton()
                self.requestButton.setText(request.getAppointmentID() + " - " + request.getAppointmentStatus())
                self.requestButton.setObjectName("requestButton")
                self.requestButton.setStyleSheet("""QPushButton#requestButton {
                                                            background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                                stop: 0 rgba(10, 2, 85, 255), 
                                                                stop: 1 rgba(59, 41, 168, 255)
                                                            );
                                                            border-radius: 10px; color: white;
                                                        }
                                                        QPushButton#requestButton:hover
                                                        {
                                                          background-color: #7752FE;}""")
                self.requestButton.setFont(buttonFont)
                self.requestButton.setFixedSize(QSize(250, 100))
                self.requestButton.setIcon(requestIcon)
                self.requestButton.setIconSize(QSize(30, 30))
                self.requestButton.clicked.connect(
                    lambda checked, request=request: self.requestButtonFunction(request, self.clinic))

                effect = QGraphicsDropShadowEffect(
                    offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
                )
                self.requestButton.setGraphicsEffect(effect)

                buttonRow.addWidget(self.requestButton)
                self.requestReviewButtons.addWidget(buttonRowWidget)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.requestReviewButtons.addWidget(spacer)

        self.requestReviewLayout.addLayout(self.requestReviewButtons)

    def requestButtonFunction(self, request, clinic):
        # update the clinic details page here according to button click
        self.clinicRequestDetails = ClinicRequestDetails(request, clinic)

        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.frameLayout.addWidget(self.clinicRequestDetails)
        self.frameLayoutManager.add(self.frameLayout.count() - 1)
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    def generateGraphWidget(self):

        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
        self.graphWidget = QWidget()
        self.graphWidget.setStyleSheet("background-color: transparent;")
        self.graphWidgetLayout = QVBoxLayout(self.graphWidget)

        self.widgetTitle = QLabel()
        self.widgetTitle.setFixedWidth(225)
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(20)
        font.setWeight(75)
        self.widgetTitle.setFont(font)
        self.widgetTitle.setText("Clinic Activity")

        headerRow = QHBoxLayout()
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        headerRow.addWidget(spacer)
        headerRow.addWidget(self.widgetTitle)

        self.graphWidgetLayout.addLayout(headerRow)
        self.graphWidgetLayout.setContentsMargins(20, 20, 20, 20)

        #generate your graph here

        self.graphLabel = QLabel()
        self.graphLabel.setFixedSize(600,350)
        graphImage = graphGen.generateGraph()
        QgraphImage = QImage(graphImage.tobytes(),graphImage.width,graphImage.height, QImage.Format_RGBA8888)
        graphPixmap = QPixmap.fromImage(QgraphImage)
        self.graphLabel.setPixmap(graphPixmap)

        self.graphWidgetLayout.addWidget(self.graphLabel)
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.graphWidgetLayout.addWidget(spacer)