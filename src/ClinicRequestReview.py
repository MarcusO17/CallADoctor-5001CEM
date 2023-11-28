import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize, QPoint
from PyQt5.QtGui import QFont, QPixmap, QIcon, QColor
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea, QSizePolicy, QStackedWidget, QGraphicsDropShadowEffect
from PyQt5 import QtWidgets

from .AccountPage import AccountPage
from .ClinicCancellationDetails import ClinicCancellationDetails
from .ClinicRequestDetails import ClinicRequestDetails
from .model import Appointment, Request
from .model.AppointmentRepo import AppointmentRepository
from .PatientPrescriptionDetails import PatientPrescriptionDetailsWindow
from .PageManager import PageManager, FrameLayoutManager


class ClinicRequestReview(QWidget):
    def __init__(self, clinic):
        super().__init__()
        self.clinic = clinic
        self.setupUi()
        self.state = "Request Review"

    def setupUi(self):
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        # this is the header (logo, title, my back button
        self.centralwidget = QWidget()
        # stacked widget containing 2 QScrollArea
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setStyleSheet(f"QStackedWidget {{background-color: transparent;}}")
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        self.stackedWidget.setGraphicsEffect(effect)

        self.stackedWidget.setGeometry(QRect(80, 200, 800, 470))

        self.headerTitle = QLabel(self.centralwidget)
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(28)
        self.headerTitle.setFont(font)
        self.headerTitle.setText("Request Review")
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

        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(20)

        self.appointmentCancellationButton = QPushButton(self.centralwidget)
        self.appointmentCancellationButton.setGeometry(QRect(70, 120, 400, 70))
        self.appointmentCancellationButton.setText("Cancellation Request")
        self.appointmentCancellationButton.setFont(font)
        self.appointmentCancellationButton.clicked.connect(self.appointmentCancellationFunction)
        self.appointmentCancellationButton.setStyleSheet("""QPushButton {
                                                background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                                        stop: 0 rgba(10, 2, 85, 255), 
                                                                        stop: 1 rgba(59, 41, 168, 255));
                                                border-radius: 10px; color: white;
                                                text-align: center; 

                                                }
                                                QPushButton:hover
                                                {
                                                  background-color: #7752FE;
                                                  text-align: center; 
                                                }""")

        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        self.appointmentCancellationButton.setGraphicsEffect(effect)

        self.requestReviewButton = QPushButton(self.centralwidget)
        self.requestReviewButton.setGeometry(QRect(500, 120, 400, 70))
        self.requestReviewButton.setFont(font)
        self.requestReviewButton.setText("Request Review")
        self.requestReviewButton.clicked.connect(self.requestReviewFunction)
        self.requestReviewButton.setStyleSheet("""QPushButton {
                                                background-color: #7752FE; border-radius: 10px; 
                                                text-align: center; padding-left: 10px; 
                                                color: white;

                                                }
                                                QPushButton:hover
                                                {
                                                  background-color: #7752FE;
                                                  text-align: center; 
                                                }""")

        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        self.requestReviewButton.setGraphicsEffect(effect)

        self.buttonContainer = QWidget()
        self.buttonContainer.setContentsMargins(20, 20, 20, 20)
        self.buttonContainer.setObjectName("buttonContainer")
        self.buttonContainer.setStyleSheet("""QWidget#buttonContainer {
                                                background: #D0BFFF;
                                                border-radius: 10px;
                                                border: none;
                                                }""")

        buttonLayout = QVBoxLayout(self.buttonContainer)
        buttonLayout.setSpacing(20)
        self.boxScrollArea = QScrollArea()
        self.boxScrollArea.setStyleSheet("""QScrollArea#scrollArea {
                                            background: #D0BFFF;
                                            border-radius: 10px;
                                            border: none;
                                            }""")
        self.boxScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.boxScrollArea.setWidgetResizable(True)
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        self.boxScrollArea.setGraphicsEffect(effect)

        self.appointmentCancellationButtonContainer = QWidget()
        self.appointmentCancellationButtonContainer.setContentsMargins(20, 20, 20, 20)
        self.appointmentCancellationButtonContainer.setObjectName("appointmentCancellationButtonContainer")
        self.appointmentCancellationButtonContainer.setStyleSheet("""QWidget#appointmentCancellationButtonContainer {
                                                                    background: #D0BFFF;
                                                                    border-radius: 10px;
                                                                    border: none;
                                                                    }""")
        appointmentCancellationButtonLayout = QVBoxLayout(self.appointmentCancellationButtonContainer)
        appointmentCancellationButtonLayout.setSpacing(20)
        self.appointmentCancellationboxScrollArea = QScrollArea()
        self.appointmentCancellationboxScrollArea.setStyleSheet("""QScrollArea#scrollArea {
                                                                    background: #D0BFFF;
                                                                    border-radius: 10px;
                                                                    border: none;
                                                                    }""")
        self.appointmentCancellationboxScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.appointmentCancellationboxScrollArea.setWidgetResizable(True)
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        self.appointmentCancellationboxScrollArea.setGraphicsEffect(effect)

        self.unassignedAppointmentList = AppointmentRepository.getAppointmentsPending(self.clinic.getClinicID())
        self.cancellationList = list()

        self.generateRequestButtons()
        self.generateCancellationButtons()

        self.boxScrollArea.setWidget(self.buttonContainer)
        self.boxScrollArea.setFixedSize(800, 470)
        self.appointmentCancellationboxScrollArea.setWidget(self.appointmentCancellationButtonContainer)
        self.appointmentCancellationboxScrollArea.setFixedSize(800, 470)

        self.highlightButtonList = list()
        self.highlightButtonList.append(self.requestReviewButton)
        self.highlightButtonList.append(self.appointmentCancellationButton)

        self.stackedWidget.addWidget(self.boxScrollArea) # index 0
        self.stackedWidget.addWidget(self.appointmentCancellationboxScrollArea)  # index 1

        stackedWidgetLayout = QVBoxLayout()
        stackedWidgetLayout.addWidget(self.stackedWidget, Qt.AlignCenter)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.centralwidget)
        #mainLayout.addLayout(stackedWidgetLayout)

        self.setLayout(mainLayout)

        self.stackedWidget.setCurrentIndex(0)

    # this method is for changing the stacked widget to display the correct QScrollArea
    def appointmentCancellationFunction(self):
        if self.state == "Request Cancellation":
            pass
        else:
            self.state = "Request Cancellation"
            print(self.state)
            self.stackedWidget.setCurrentIndex(1)
            self.setButtonHighlight(self.appointmentCancellationButton)
    # this method is for changing the stacked widget to display the correct QScrollArea
    def requestReviewFunction(self):
        if self.state == "Request Review":
            pass
        else:
            self.state = "Request Review"
            print(self.state)
            self.stackedWidget.setCurrentIndex(0)
            self.setButtonHighlight(self.requestReviewButton)

    # this method is triggered when any of the request button is clicked
    def requestButtonFunction(self, request, clinic):
        # update the clinic details page here according to button click
        self.clinicRequestDetails = ClinicRequestDetails(request, clinic)

        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.frameLayout.addWidget(self.clinicRequestDetails)
        self.frameLayoutManager.add(self.frameLayout.count() - 1)
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    # this method is triggered to generate request buttons
    # this method can be recalled to regenerate the request buttons
    def generateRequestButtons(self):

        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        for i in range(self.buttonContainer.layout().count()):
            widget = self.buttonContainer.layout().itemAt(0).widget()
            self.buttonContainer.layout().removeWidget(widget)
            if widget is not None:
                widget.deleteLater()

        self.unassignedAppointmentList.clear()

        buttonFont = QFont()
        buttonFont.setFamily("Montserrat")
        buttonFont.setPointSize(20)

        self.unassignedAppointmentList = AppointmentRepository.getAppointmentsPending(self.clinic.getClinicID())

        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-document-60.png")
        requestIcon = QIcon(filepath)

        for count, request in enumerate(self.unassignedAppointmentList):
            print("generate request", count)
            self.requestButton = QPushButton()
            self.requestButton.setText(request.getAppointmentID() + " - " + request.getAppointmentStatus())
            self.requestButton.setFont(buttonFont)
            self.requestButton.setIconSize(QSize(80, 80))
            self.requestButton.setFixedSize(QSize(700, 100))
            self.requestButton.setIcon(requestIcon)
            self.requestButton.clicked.connect(
                lambda checked, request=request: self.requestButtonFunction(request, self.clinic))
            self.requestButton.setStyleSheet("""QPushButton {
                                                    background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                                            stop: 0 rgba(10, 2, 85, 255), 
                                                                            stop: 1 rgba(59, 41, 168, 255));
                                                    border-radius: 10px; color: white;
                                                    text-align: left; 
                                                    padding-left: 20px;
                                                    }
                                                    QPushButton:hover
                                                    {
                                                      background-color: #7752FE;
                                                      text-align: left; 
                                                      padding-left: 20px;
                                                    }""")

            effect = QGraphicsDropShadowEffect(
                offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
            )
            self.requestButton.setGraphicsEffect(effect)

            self.buttonContainer.layout().addWidget(self.requestButton)


        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.buttonContainer.layout().addWidget(spacer)

    # this method is triggered when any of the cancellation request button is clicked
    def cancellationButtonFunction(self, request, clinic):
        # update the clinic details page here according to button click
        self.clinicCancellationDetails = ClinicCancellationDetails(request, clinic)

        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.frameLayout.addWidget(self.clinicCancellationDetails)
        self.frameLayoutManager.add(self.frameLayout.count() - 1)
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    # this method is triggered to generate cancellation request buttons
    # this method can be recalled to regenerate the cancellation request buttons
    def generateCancellationButtons(self):

        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        for i in range(self.appointmentCancellationButtonContainer.layout().count()):
            widget = self.appointmentCancellationButtonContainer.layout().itemAt(0).widget()
            self.appointmentCancellationButtonContainer.layout().removeWidget(widget)
            if widget is not None:
                widget.deleteLater()

        self.cancellationList.clear()

        buttonFont = QFont()
        buttonFont.setFamily("Montserrat")
        buttonFont.setPointSize(20)

        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-document-60.png")
        requestIcon = QIcon(filepath)

        self.cancellationList = Request.getRequests(self.clinic.getClinicID())

        for count, request in enumerate(self.cancellationList):
            self.cancellationButton = QPushButton()
            self.cancellationButton.setText(request.getRequestID() + " - " + request.getApprovalStatus())
            self.cancellationButton.setFont(buttonFont)
            self.cancellationButton.setIconSize(QSize(80, 80))
            self.cancellationButton.setFixedSize(QSize(700, 100))
            self.cancellationButton.setIcon(requestIcon)
            self.cancellationButton.clicked.connect(
                lambda checked, request=request: self.cancellationButtonFunction(request, self.clinic))

            self.cancellationButton.setStyleSheet("""QPushButton {
                                                        background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                                                stop: 0 rgba(10, 2, 85, 255), 
                                                                                stop: 1 rgba(59, 41, 168, 255));
                                                        border-radius: 10px; color: white;
                                                        text-align: left; 
                                                        padding-left: 20px;
                                                        }
                                                        QPushButton:hover
                                                        {
                                                          background-color: #7752FE;
                                                          text-align: left; 
                                                          padding-left: 20px;
                                                        }""")

            effect = QGraphicsDropShadowEffect(
                offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
            )
            self.cancellationButton.setGraphicsEffect(effect)

            self.appointmentCancellationButtonContainer.layout().addWidget(self.cancellationButton)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.appointmentCancellationButtonContainer.layout().addWidget(spacer)

    # method to highlight the button the user is currently in
    def setButtonHighlight(self, button):
        for buttonTemp in self.highlightButtonList:
            if buttonTemp == button:
                button.setStyleSheet("background-color: #7752FE; border-radius: 10px; text-align: center; padding-left: 10px; color: white;")
            else:
                buttonTemp.setStyleSheet("""
                    QPushButton
                    {
                       background-color: #190482;
                       border-radius: 10px;
                       color: white;
                       text-align: center; 
                       padding-left: 10px;
                    }
                    QPushButton:pressed
                    {
                      background-color: #190482;    
                      text-align: center; 
                      padding-left: 10px; 
                    }
                    QPushButton:hover
                    {
                      background-color: #7752FE;
                      text-align: center; 
                    }
                    """)




