import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize, QPoint
from PyQt5.QtGui import QFont, QPixmap, QIcon, QColor
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea, QSizePolicy, QGraphicsDropShadowEffect
from PyQt5 import QtWidgets

from .AccountPage import AccountPage
from .model import Prescription, PrescriptionRepo
from .PatientPrescriptionDetails import PatientPrescriptionDetailsWindow
from .PageManager import PageManager, FrameLayoutManager
from datetime import datetime

class PatientPrescriptionWindow(QWidget):
    def __init__(self, patient):
        super().__init__()
        self.patient = patient
        self.setupUi()

    def setupUi(self):

        # this is the header (logo, title, my back button
        self.centralwidget = QWidget()


        self.headerTitle = QLabel(self.centralwidget)
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(28)
        self.headerTitle.setFont(font)
        self.headerTitle.setText("My Prescriptions")
        self.headerTitle.setObjectName("headerTitle")
        self.headerTitle.setFrameShape(QtWidgets.QFrame.Box)
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

        self.buttonContainer = QWidget()
        self.buttonContainer.setObjectName("buttonContainer")
        self.buttonContainer.setStyleSheet("""QWidget#buttonContainer {
                                                            background: #D0BFFF;
                                                            border-radius: 10px;
                                                            margin-left: 100px;
                                                            }""")
        buttonLayout = QVBoxLayout(self.buttonContainer)
        self.buttonContainer.setContentsMargins(20,20,20,20)
        buttonLayout.setSpacing(20)

        boxScrollArea = QScrollArea()
        boxScrollArea.setObjectName("scrollArea")

        boxScrollArea.setWidgetResizable(True)
        boxScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        boxScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)


        self.generatePrescription()

        boxScrollArea.setWidget(self.buttonContainer)
        boxScrollArea.setFixedSize(900,500)
        boxScrollArea.setStyleSheet("""QScrollArea#scrollArea {
                                                    background: #D0BFFF;
                                                    border-radius: 10px;
                                                    margin-left: 80px;
                                                    }""")
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        boxScrollArea.setGraphicsEffect(effect)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.centralwidget)
        mainLayout.addWidget(boxScrollArea)
        spacer = QWidget()
        spacer.setFixedHeight(30)
        mainLayout.addWidget(spacer)

        self.setLayout(mainLayout)

    def prescriptionButtonFunction(self, prescription, patient):
        # update the clinic details page here according to button click
        self.prescriptionDetailsWindow = PatientPrescriptionDetailsWindow(prescription, patient)

        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()

        self.frameLayout.addWidget(self.prescriptionDetailsWindow)
        self.frameLayoutManager.add(self.frameLayout.count() - 1)
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    def generatePrescription(self):

        for i in range(self.buttonContainer.layout().count()):
            widget = self.buttonContainer.layout().itemAt(0).widget()
            self.buttonContainer.layout().removeWidget(widget)
            print("in the loop ", i)
            if widget is not None:
                widget.deleteLater()
                print("deleting 1 widget")

        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        prescriptionList = PrescriptionRepo.PrescriptionRepository.getPrescriptionListByPatient(
            self.patient.getPatientID())

        buttonFont = QFont()
        buttonFont.setFamily("Arial")
        buttonFont.setPointSize(25)
        buttonFont.setBold(True)
        buttonFont.setWeight(75)

        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-prescription-50.png")
        prescriptionIcon = QIcon(filepath)

        for count, prescription in enumerate(prescriptionList):
            self.prescriptionButton = QPushButton()
            date = datetime.strptime(prescription.getExpiryDate(), '%a, %d %b %Y %H:%M:%S %Z')
            formattedDate = date.strftime('%d/%m/%Y')
            self.prescriptionButton.setText(prescription.getPrescriptionID() + " - " + formattedDate)
            self.prescriptionButton.setFont(buttonFont)
            self.prescriptionButton.setIconSize(QSize(80, 80))
            self.prescriptionButton.setFixedSize(QSize(750, 100))
            self.prescriptionButton.setIcon(prescriptionIcon)
            self.prescriptionButton.setStyleSheet("""QPushButton {
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
            self.prescriptionButton.setGraphicsEffect(effect)
            self.prescriptionButton.clicked.connect(
                lambda checked, prescription=prescription: self.prescriptionButtonFunction(prescription, self.patient))
            self.buttonContainer.layout().addWidget(self.prescriptionButton)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.buttonContainer.layout().addWidget(spacer)

