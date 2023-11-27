import io
import os

from PyQt5.QtCore import QSize, QDate, QPoint, Qt
from PyQt5.QtGui import QFont, QIcon, QColor
from PyQt5.QtWidgets import  QWidget, QLabel, QPushButton, QVBoxLayout, \
    QHBoxLayout,QSizePolicy, QGraphicsDropShadowEffect
from PyQt5.QtWebEngineWidgets import QWebEngineView

from .AccountPage import AccountPage
from .DoctorAppointmentDetails import DoctorAppointmentDetails
from .DoctorPatientHistory import DoctorPatientHistoryWindow
from .PatientAppointmentDetails import PatientAppointmentDetailsWindow
from .PatientPrescriptionDetails import PatientPrescriptionDetailsWindow
from .model import Appointment, AppointmentRepo, Patient, PrescriptionRepo, Clinic, geoHelper
from .model.ClinicRepo import ClinicRepository
from .model.AppointmentRepo import AppointmentRepository
from .PageManager import PageManager, FrameLayoutManager


class PatientDashboard(QWidget):
    def __init__(self, patient):
        super().__init__()
        self.patient = patient
        self.currLocation = (self.patient.getPatientLat(), self.patient.getPatientLon())

        self.setupUi()

    def setupUi(self):

        self.mainLayout = QHBoxLayout()
        self.rightLayout = QVBoxLayout()
        self.leftLayout = QVBoxLayout()
        self.upcomingAppointmentButtons = QVBoxLayout()
        self.prescriptionButtons = QVBoxLayout()

        self.generateWelcomeText()

        self.generateUpcomingAppointments()

        clinicList = ClinicRepository.getClinicList()
        self.generateMapWidget(clinicList)


        self.generatePrescription()

        self.leftLayout.addWidget(self.welcomeTextWidget, 3)
        spacer = QWidget()
        spacer.setFixedHeight(30)
        self.leftLayout.addWidget(spacer)
        self.leftLayout.addWidget(self.mapWidget, 7)

        self.dateLayout = QHBoxLayout()
        spacer = QWidget()
        spacer.setFixedWidth(230)
        self.dateLayout.addWidget(spacer)
        self.dateWidget = QLabel(f"Date: {QDate.currentDate().toString('dd-MM-yyyy')}")
        self.dateWidget.setObjectName("dateWidget")
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(15)
        self.dateWidget.setFont(font)
        self.dateWidget.setAlignment(Qt.AlignCenter)
        self.dateWidget.setFixedSize(220,75)
        self.dateWidget.setStyleSheet("""QLabel#dateWidget {background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
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
        self.dateWidget.setGraphicsEffect(effect)
        self.dateWidget.setContentsMargins(10, 10, 10, 10)

        self.dateLayout.addWidget(self.dateWidget)

        self.rightLayout.addLayout(self.dateLayout)

        spacer = QWidget()
        spacer.setFixedHeight(50)
        self.rightLayout.addWidget(spacer)
        self.upcomingAppointmentWidget.setFixedWidth(500)
        self.rightLayout.addWidget(self.upcomingAppointmentWidget, 5)
        self.rightLayout.addWidget(self.prescriptionWidget, 5)

        self.mainLayout.addLayout(self.leftLayout, 7)
        self.mainLayout.addLayout(self.rightLayout, 5)


        self.setLayout(self.mainLayout)

    def generatePrescription(self):
        self.prescriptionWidget = QWidget()
        self.prescriptionWidget.setObjectName("prescriptionWidget")
        self.prescriptionWidget.setStyleSheet("background-color: transparent;")
        self.prescriptionLayout = QVBoxLayout(self.prescriptionWidget)

        for i in range(self.prescriptionButtons.count()):
            item = self.prescriptionButtons.itemAt(0)
            self.prescriptionButtons.removeItem(item)
            widget = item.widget()
            print("in the loop prescription ", i)
            if widget is not None:
                widget.deleteLater()
                print("deleting 1 widget prescription prescription")

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.prescriptionTitle = QLabel()
        self.prescriptionTitle.setFixedWidth(200)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.prescriptionTitle.setFont(font)
        self.prescriptionTitle.setText("Prescription")
        self.prescriptionTitle.setStyleSheet("color: black;")
        headerRow = QHBoxLayout()
        headerRow.addWidget(spacer)
        headerRow.addWidget(self.prescriptionTitle)

        self.prescriptionLayout.addLayout(headerRow)
        self.prescriptionLayout.setContentsMargins(20, 20, 20, 20)

        prescriptionList = PrescriptionRepo.PrescriptionRepository.getPrescriptionListByPatient(self.patient.getPatientID())
        twoPrescriptionList = prescriptionList[:1]

        buttonFont = QFont()
        buttonFont.setFamily("Arial")
        buttonFont.setPointSize(20)

        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-pills-64.png")
        self.prescriptionButtonIcon = QIcon(filepath)

        if len(twoPrescriptionList) == 0:
            emptyPrescription = QLabel()
            emptyPrescription.setFont(buttonFont)
            emptyPrescription.setAlignment(Qt.AlignCenter)
            emptyPrescription.setText("No Prescriptions")
            emptyPrescription.setObjectName("emptyPrescription")
            emptyPrescription.setFixedSize(440, 250)
            emptyPrescription.setStyleSheet("""QWidget#emptyPrescription {background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                                stop: 0 rgba(25, 4, 130, 255), 
                                                                stop: 1 rgba(119, 82, 254, 255)
                                                            );
                                                            border-radius: 10px;
                                                            text-align: center;
                                                            color: white;
                                                        }""")
            self.prescriptionButtons.addWidget(emptyPrescription)
        else:
            for count, prescription in enumerate(twoPrescriptionList):
                buttonRow = QHBoxLayout()
                spacer = QWidget()
                spacer.setFixedSize(60, 120)
                buttonRow.addWidget(spacer)
                prescriptionButton = QPushButton()
                prescriptionButton.setObjectName("prescriptionButton")
                prescriptionButton.setText(f"{prescription.getPrescriptionID()}")
                prescriptionButton.setStyleSheet("""QPushButton#prescriptionButton {
                                                                                background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                                                    stop: 0 rgba(10, 2, 85, 255), 
                                                                                    stop: 1 rgba(59, 41, 168, 255)
                                                                                );
                                                                                border-radius: 10px; color: white;
                                                                            }
                                                                            QPushButton#prescriptionButton:hover
                                                                            {
                                                                            background-color: #7752FE;}""")
                effect = QGraphicsDropShadowEffect(
                offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
                )
                prescriptionButton.setGraphicsEffect(effect)
                prescriptionButton.setFont(buttonFont)
                prescriptionButton.setFixedSize(QSize(350, 100))
                prescriptionButton.setIconSize(QSize(30, 30))
                prescriptionButton.setIcon(self.prescriptionButtonIcon)
                prescriptionButton.clicked.connect(
                    lambda checked, prescription=prescription: self.prescriptionButtonFunction(prescription, self.patient))
                buttonRow.addWidget(prescriptionButton)
                self.prescriptionButtons.addLayout(buttonRow)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.prescriptionButtons.addWidget(spacer)
        self.prescriptionLayout.addLayout(self.prescriptionButtons)

    def prescriptionButtonFunction(self, prescription, patient):
        self.prescriptionDetails = PatientPrescriptionDetailsWindow(prescription, patient)

        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.frameLayout.addWidget(self.prescriptionDetails)
        self.frameLayoutManager.add(self.frameLayout.count()-1)
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())


    def generateWelcomeText(self):

        self.welcomeTextWidget = QWidget()
        self.welcomeTextWidget.setObjectName("welcomeTextWidget")
        self.welcomeTextWidget.setStyleSheet("""QWidget#welcomeTextWidget {background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
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
        self.welcomeTextWidget.setGraphicsEffect(effect)
        self.welcomeTextLayout = QVBoxLayout(self.welcomeTextWidget)

        welcomeTextLabel = QLabel()
        welcomeTextLabel.setText(f"Welcome {self.patient.getPatientName()}!")
        welcomeTextLabel.setStyleSheet("color: white; padding-left: 30px;")
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)

        welcomeTextLabel.setFont(font)

        self.welcomeTextLayout.addWidget(welcomeTextLabel)

        self.welcomeTextWidget.setFixedHeight(75)
        self.welcomeTextWidget.setFixedWidth(700)
        # Center the content vertically and horizontally
        self.welcomeTextLayout.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

    def generateUpcomingAppointments(self):

        self.upcomingAppointmentWidget = QWidget()
        self.upcomingAppointmentWidget.setObjectName("upcomingAppointmentWidget")
        self.upcomingAppointmentWidget.setStyleSheet("background-color: transparent;")
        self.upcomingAppointmentLayout = QVBoxLayout(self.upcomingAppointmentWidget)

        for i in range(self.upcomingAppointmentButtons.count()):
            item = self.upcomingAppointmentButtons.itemAt(0)
            self.upcomingAppointmentButtons.removeItem(item)
            widget = item.widget()
            print("in the loop upcoming appointment ", i)
            if widget is not None:
                widget.deleteLater()
                print("deleting 1 widget upcoming appointment")

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
        self.upcomingAppointmentTitle.setStyleSheet("color: black;")
        headerRow = QHBoxLayout()
        headerRow.addWidget(spacer)
        headerRow.addWidget(self.upcomingAppointmentTitle)

        self.upcomingAppointmentLayout.addLayout(headerRow)
        self.upcomingAppointmentLayout.setContentsMargins(20, 20, 20, 20)

        appointmentList = AppointmentRepo.AppointmentRepository.getPatientDashboardAppointments(self.patient.getPatientID())
        appointmentList = [appointments for appointments in appointmentList if appointments.getAppointmentStatus() != 'Completed']
        twoAppointmentList = appointmentList[:1]

        buttonFont = QFont()
        buttonFont.setFamily("Arial")
        buttonFont.setPointSize(20)

        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-appointment-64.png")
        self.appointmentButtonIcon = QIcon(filepath)

        if len(twoAppointmentList) == 0:
            emptyAppointment = QLabel()
            emptyAppointment.setFont(buttonFont)
            emptyAppointment.setAlignment(Qt.AlignCenter)
            emptyAppointment.setText("No Appointment")
            emptyAppointment.setObjectName("emptyAppointment")
            emptyAppointment.setFixedSize(440, 140)
            emptyAppointment.setStyleSheet("""QLabel#emptyAppointment {background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                                stop: 0 rgba(25, 4, 130, 255), 
                                                                stop: 1 rgba(119, 82, 254, 255)
                                                            );
                                                            border-radius: 10px;
                                                            text-align: center;
                                                            color: white;
                                                        }""")
            self.upcomingAppointmentButtons.addWidget(emptyAppointment)
        else:
            for count, appointment in enumerate(twoAppointmentList):
                buttonRow = QHBoxLayout()
                spacer = QWidget()
                spacer.setFixedSize(0, 120)
                buttonRow.addWidget(spacer)
                appointmentButton = QPushButton()
                appointmentButton.setObjectName("appointmentButton")
                appointmentButton.setText(f"{appointment.getAppointmentID()} - {appointment.getStartTime()}")
                appointmentButton.setStyleSheet("""QPushButton#appointmentButton {
                                                                                background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                                                    stop: 0 rgba(10, 2, 85, 255), 
                                                                                    stop: 1 rgba(59, 41, 168, 255)
                                                                                );
                                                                                border-radius: 10px; color: white;
                                                                            }
                                                                            QPushButton#appointmentButton:hover
                                                                            {
                                                                            background-color: #7752FE;}""")
                effect = QGraphicsDropShadowEffect(
                offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
                )
                appointmentButton.setGraphicsEffect(effect)
                appointmentButton.setFont(buttonFont)
                appointmentButton.setFixedSize(QSize(350, 100))
                appointmentButton.setIconSize(QSize(30, 30))
                appointmentButton.setIcon(self.appointmentButtonIcon)
                appointmentButton.clicked.connect(
                    lambda checked, appointment=appointment: self.appointmentButtonFunction(appointment, self.patient))
                buttonRow.addWidget(appointmentButton)
                self.upcomingAppointmentLayout.addLayout(buttonRow)

            spacer = QWidget()
            spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
            self.upcomingAppointmentButtons.addWidget(spacer)
                
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.upcomingAppointmentButtons.addWidget(spacer)
        self.upcomingAppointmentLayout.addLayout(self.upcomingAppointmentButtons)


    def appointmentButtonFunction(self, appointment, patient):
        self.patientAppointmentDetails = PatientAppointmentDetailsWindow(appointment, patient)
        self.patientAppointmentDetails.setMode(appointment.getAppointmentStatus())

        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.frameLayout.addWidget(self.patientAppointmentDetails)
        self.frameLayoutManager.add(self.frameLayout.count()-1)
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    def generateMapWidget(self, clinicList):

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
        font.setFamily("Arial")
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

        map = geoHelper.showMap(self.currLocation)  # Return Folium Map

        geoHelper.addMarker(map, self.currLocation, 'We are here!', 'red', 'star')  # Current Loc
        map = self.generateClinicMarkers(map,clinicList)

        data = io.BytesIO()
        map.save(data, close_file=False)

        webView = QWebEngineView()
        webView.setHtml(data.getvalue().decode())

        self.mapWidgetLayout.addWidget(webView)
        self.mainMapLayout.addWidget(self.mapWidget)

    def generateClinicMarkers(self,map,clinicList):
        for clinics in clinicList:
            geoHelper.addMarker(map,(clinics.getClinicLat(),clinics.getClinicLon()),clinics.getClinicName()
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