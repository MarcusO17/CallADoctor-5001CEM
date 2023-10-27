import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize, QDateTime, QDate
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea, QLineEdit, QMessageBox, QDialog, QDateEdit
from PyQt5 import QtWidgets

from .AccountPage import AccountPage
from .model import PrescriptionDetails
from .model import Prescription
from .PageManager import PageManager


class DoctorGeneratePrescription(QMainWindow):

    def __init__(self, patient, appointment, doctor):
        super().__init__()

        #set the information here
        self.patient = patient
        self.appointment = appointment
        self.doctor = doctor

        self.pageManager = PageManager()
        self.setWindowTitle("Generate Prescription")
        self.setFixedWidth(1280)
        self.setFixedHeight(720)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
        # this is the header (logo, title, my back button
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # header (probably reused in most files)
        self.topLeftLogo = QLabel(self.centralwidget)
        self.topLeftLogo.setFrameShape(QtWidgets.QFrame.Box)
        self.topLeftLogo.setGeometry(QRect(20, 10, 60, 60))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.topLeftLogoIcon = QPixmap(filepath)
        self.topLeftLogoIcon = self.topLeftLogoIcon.scaled(60, 60)
        self.topLeftLogo.setPixmap(self.topLeftLogoIcon)

        self.headerTitle = QLabel(self.centralwidget)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.headerTitle.setFont(font)
        self.headerTitle.setText(f"{self.patient.getPatientName()} - Generate Prescription")
        self.headerTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.headerTitle.setGeometry(QRect(200, 40, 800, 70))
        self.headerTitle.setAlignment(Qt.AlignCenter)
        self.headerTitle.setStyleSheet("margin-left: 20px; margin-right: 20px")

        self.myAccountButton = QPushButton(self.centralwidget)
        self.myAccountButton.setGeometry(QRect(1050, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.myAccountIcon = QIcon(filepath)
        self.myAccountButton.setIconSize(QSize(70, 70))
        self.myAccountButton.setIcon(self.myAccountIcon)
        self.myAccountButton.clicked.connect(self.goToAccountPage)

        # Push Button 5 (Log Out)
        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setFixedSize(70, 70)
        self.backButton.setGeometry(QRect(1150, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\backbutton.png")
        self.backIcon = QIcon(filepath)
        self.backButton.setIconSize(QSize(70, 70))
        self.backButton.setIcon(self.backIcon)
        self.backButton.clicked.connect(self.backButtonFunction)


        self.rowContainer = QWidget()
        rowLayout = QVBoxLayout(self.rowContainer)
        self.rowContainer.setContentsMargins(20, 20, 20, 20)
        boxScrollArea = QScrollArea()
        boxScrollArea.setWidgetResizable(True)
        boxScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.addNewRowButton = QPushButton(self.centralwidget)
        self.addNewRowButton.setGeometry(QRect(190, 130, 200, 50))
        self.addNewRowButton.setText("Add New Row")
        self.addNewRowButton.clicked.connect(self.addNewRow)

        self.completePrescriptionButton = QPushButton(self.centralwidget)
        self.completePrescriptionButton.setGeometry(QRect(900, 130, 200, 50))
        self.completePrescriptionButton.setText("Complete Prescription")
        self.completePrescriptionButton.clicked.connect(self.completePrescription)

        boxScrollArea.setWidget(self.rowContainer)
        boxScrollArea.setFixedSize(1000, 500)
        topSpacer = QWidget()
        topSpacer.setFixedHeight(150)
        topSpacer.setFixedWidth(20)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(topSpacer)
        mainLayout.addWidget(boxScrollArea)
        mainLayout.setAlignment(Qt.AlignHCenter)

        self.centralwidget.setLayout(mainLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(MainWindow)

    def backButtonFunction(self):
        backConfirmationDialog = QMessageBox.question(self.centralwidget, "Back Confirmation",
                                               "Do you want to discard this prescription",
                                               QMessageBox.Yes | QMessageBox.No)
        if backConfirmationDialog == QMessageBox.Yes:
            self.pageManager.goBack()

    def completePrescription(self):
        self.expiryDateDialog = QDialog(self)
        self.expiryDateDialog.setFixedSize(400, 400)

        self.expiryDateDialog.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)  # Remove close button
        self.expiryDateDialog.setWindowFlag(Qt.FramelessWindowHint)
        self.expiryDateDialog.setWindowTitle("Select An Expiry Date")

        self.layout = QVBoxLayout()

        self.expiryDateDateEdit = QDateEdit()
        self.expiryDateDateEdit.setCalendarPopup(True)
        self.expiryDateDateEdit.setDateTime(QDateTime.currentDateTime())
        self.expiryDateDateEdit.setMinimumDate(QDate.currentDate())
        self.layout.addWidget(self.expiryDateDateEdit)

        confirmationButtonLayout = QHBoxLayout()

        cancelButton = QPushButton()
        cancelButton.setText("Cancel")
        cancelButton.clicked.connect(lambda checked: self.expiryDateDialog.close())
        confirmationButtonLayout.addWidget(cancelButton)

        confirmationButton = QPushButton()
        confirmationButton.setText("Confirm")
        confirmationButton.clicked.connect(lambda checked: self.completeButtonConfirmationFunction(self.expiryDateDateEdit.date().toString("yyyy-MM-dd")))
        confirmationButtonLayout.addWidget(confirmationButton)

        self.layout.addLayout(confirmationButtonLayout)
        self.expiryDateDialog.setLayout(self.layout)
        self.expiryDateDialog.exec_()

    def completeButtonConfirmationFunction(self, date):
        # marcus you do your thing here

        prescription = Prescription("PR0001", self.appointment.getAppointmentID(), date)
        for i in range(self.rowContainer.layout().count()):
            row = self.rowContainer.layout().itemAt(i).widget()

            medicationName = row.layout().itemAt(0).widget().text()
            dosage = row.layout().itemAt(1).widget().text()
            pillsPerDay = row.layout().itemAt(2).widget().text()
            food = row.layout().itemAt(3).widget().text()

            prescriptionDetails = PrescriptionDetails(medicationName, int(pillsPerDay), food, dosage)
            prescription.setPrescriptionDetails(prescriptionDetails)

            print(f"{prescriptionDetails.getMedicationName()} \n {prescriptionDetails.getDosage()}")

        print(prescription.getExpiryDate())

        self.expiryDateDialog.close()
        self.pageManager.goBack()

    def addNewRow(self):

        row = QWidget()
        rowLayout = QHBoxLayout(row)

        prescriptionMedicationName = QLineEdit()
        prescriptionMedicationName.setFixedSize(300, 50)
        prescriptionMedicationName.setPlaceholderText("Medication Name")

        prescriptionDosage = QLineEdit()
        prescriptionDosage.setFixedSize(150, 50)
        prescriptionDosage.setPlaceholderText("Dosage")

        prescriptionPillsPerDay = QLineEdit()
        prescriptionPillsPerDay.setFixedSize(150, 50)
        prescriptionPillsPerDay.setPlaceholderText("Pills Per Day")

        prescriptionFood = QLineEdit()
        prescriptionFood.setFixedSize(150, 50)
        prescriptionFood.setPlaceholderText("Before or After eating")

        removeRowButton = QPushButton()
        removeRowButton.setFixedSize(50,50)
        filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "resources\\logo-placeholder-image.png")
        removeRowIcon = QIcon(filepath)
        removeRowButton.setIconSize(QSize(70, 70))
        removeRowButton.setIcon(removeRowIcon)
        removeRowButton.clicked.connect(lambda checked, row=row: self.removeRow(row))

        row.setFixedSize(900,100)
        row.layout().addWidget(prescriptionMedicationName)
        row.layout().addWidget(prescriptionDosage)
        row.layout().addWidget(prescriptionPillsPerDay)
        row.layout().addWidget(prescriptionFood)
        row.layout().addWidget(removeRowButton)

        self.rowContainer.layout().addWidget(row)

    def removeRow(self, row):
        self.rowContainer.layout().removeWidget(row)

        for i in range(row.layout().count()):
            widget = row.layout().itemAt(0).widget()
            row.layout().removeWidget(widget)
            if widget is not None:
                widget.deleteLater()

    def goToAccountPage(self):
        self.accountPage = AccountPage()
        self.accountPage.setUser("Doctor", self.doctor)
        self.pageManager.add(self.accountPage)

