from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox
from PyQt5 import QtCore
from .PageManager import PageManager
from .model import Login
from .model import Clinic
from .PatientHomepage import PatientHomepage
from .DoctorHomepage import DoctorHomepage
from .ClinicHomepage import ClinicHomepage
from .PatientRegister import PatientRegisterWindow
from .ClinicRegister import ClinicRegisterWindow
from .DoctorRegister import DoctorRegisterWindow
from .DoctorMyAppointment import DoctorMyAppointmentWindow
import os

from .PageManager import PageManager


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.pageManager = PageManager()
        self.setWindowTitle("Login")
        self.setFixedWidth(350)
        self.setFixedHeight(500)
        self.initUI()
        self.pageManager.add(self)

    def initUI(self):
        loginFormLayout = QVBoxLayout()
        loginFormLayout.setSpacing(0)
        loginFormLayout.setContentsMargins(20, 20, 20, 20)

        self.logoLabel = QLabel()

        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
        filename = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")

        try:
            logoPixmap = QPixmap(filename)
            logoPixmap = logoPixmap.scaled(200,200)
            self.logoLabel.setPixmap(logoPixmap)
            self.logoLabel.setContentsMargins(45,0,0,0)

        except Exception as e:
            print(e)

        field1Layout = QVBoxLayout()
        field2Layout = QVBoxLayout()

        labelFont = QFont()
        labelFont.setFamily("Poppins")
        labelFont.setPointSize(12)

        self.emailLabel = QLabel("Email:")
        self.emailLabel.setFont(labelFont)
        self.emailInput = QLineEdit()
        field1Layout.addWidget(self.emailLabel)
        field1Layout.addWidget(self.emailInput)
        field1Layout.setContentsMargins(0,30,0,20)

        self.passwordLabel = QLabel("Password:")
        self.passwordLabel.setFont(labelFont)
        self.passwordInput = QLineEdit()
        self.passwordInput.setEchoMode(QLineEdit.Password)

        field2Layout.addWidget(self.passwordLabel)
        field2Layout.addWidget(self.passwordInput)
        field2Layout.setContentsMargins(0, 0, 0, 40)

        self.loginButton = QPushButton("Login")
        self.loginButton.setDefault(True)
        self.loginButton.clicked.connect(self.loginAuthorization)

        self.goToRegistrationButton = QPushButton("Register Account")
        self.goToRegistrationButton.setDefault(True)
        self.goToRegistrationButton.clicked.connect(self.selectRegisterPageFunction)

        loginFormLayout.addWidget(self.logoLabel)
        loginFormLayout.addLayout(field1Layout)
        loginFormLayout.addLayout(field2Layout)
        loginFormLayout.addWidget(self.loginButton)
        loginFormLayout.addWidget(self.goToRegistrationButton)
        loginFormLayout.setContentsMargins(30,30,30,60)

        self.setLayout(loginFormLayout)

    def selectRegisterPageFunction(self):
        message_box = QMessageBox()
        message_box.setText("Choose Which Registration Page")
        clinicButton = message_box.addButton("Clinic", QMessageBox.ActionRole)
        patientButton = message_box.addButton("Patient", QMessageBox.ActionRole)
        doctorButton = message_box.addButton("Doctor", QMessageBox.ActionRole)
        message_box.exec_()

        if message_box.clickedButton() == clinicButton:
            self.openClinicRegisterWindow()
        elif message_box.clickedButton() == patientButton:
            self.openPatientRegisterWindow()
        elif message_box.clickedButton() == doctorButton:
            self.openDoctorRegisterWindow()
        
    def openClinicRegisterWindow(self):
        self.clinicRegister = ClinicRegisterWindow()
        self.pageManager.add(self.clinicRegister)

    def openPatientRegisterWindow(self):
        self.patientRegister = PatientRegisterWindow()
        self.pageManager.add(self.patientRegister)

    def openDoctorRegisterWindow(self):
        self.DoctorRegister = DoctorRegisterWindow()
        self.pageManager.add(self.DoctorRegister)

    # for each of the login here, please pass in the id of the patient, doctor or clinic when creating the homepage

    def patientLogin(self,sessionID):
        self.patientHomepage = PatientHomepage(sessionID)
        self.pageManager.add(self.patientHomepage)


    def doctorLogin(self,sessionID):
        self.doctorHomepage = DoctorHomepage(sessionID)
        self.pageManager.add(self.doctorHomepage)

    def clinicLogin(self,sessionID):
        self.clinicHomepage = ClinicHomepage(sessionID)
        self.pageManager.add(self.clinicHomepage)

    def loginAuthorization(self):
        email = self.emailInput.text()
        password = self.passwordInput.text()

        loginJSON = {
            "email" : email,
            "password" : password
        }

        sessionInfo,isValid = Login.userValidLogin(credentials=loginJSON)

        if isValid:
            sessionID = sessionInfo['ID']
            role = sessionInfo['role']
            if role == "patient":
                self.patientLogin(sessionID)
            elif role == "doctor":
                self.doctorLogin(sessionID)
            elif role == "clinic":
                self.clinicLogin(sessionID)

        else:
            print("login failed")




