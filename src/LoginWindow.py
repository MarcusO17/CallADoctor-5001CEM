from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap, QPalette, QColor, QBrush
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QVBoxLayout,QHBoxLayout, QWidget, QMessageBox, QApplication, \
QFrame
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
        self.setObjectName("LoginWindow")
        self.pageManager = PageManager()
        self.setWindowTitle("Login")
        self.setFixedWidth(800)
        self.setFixedHeight(600)
        self.initUI()
        self.pageManager.add(self)

    def initUI(self):

        self.setAutoFillBackground(True)
        palette = self.palette()
        gradient = "qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(208, 191, 255, 255), stop:1 rgba(113, 58, 190, 255));"
        palette.setBrush(self.backgroundRole(), QBrush(QColor(0, 0, 0, 0)))  # Make the window background transparent
        self.setPalette(palette)
        self.setStyleSheet(f"QWidget#LoginWindow {{background: {gradient}}};")

        self.borderFrame = QFrame(self)
        self.borderFrame.setGeometry(-10, 65, 310, 450)  # Adjust the geometry as needed
        self.borderFrame.setFrameShape(QFrame.StyledPanel)
        self.borderFrame.setLineWidth(2)
        self.borderFrame.setStyleSheet("border: 2px dashed #000000; background: transparent;")

        self.logoLabel = QLabel(self)

        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
        filename = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")

        try:
            logoPixmap = QPixmap(filename)
            logoPixmap = logoPixmap.scaled(200,200)
            self.logoLabel.setPixmap(logoPixmap)
            self.logoLabel.setGeometry(90, 50, 200, 200)


        except Exception as e:
            print(e)



        labelFont = QFont()
        labelFont.setFamily("Poppins")
        labelFont.setPointSize(12)

        self.emailLabel = QLabel("Email:", self)
        self.emailLabel.setFont(labelFont)
        self.emailLabel.setGeometry(80, 220, 100, 30)

        self.emailInput = QLineEdit(self)
        self.emailInput.setFixedSize(200, 30)
        self.emailInput.setGeometry(80, 250, 200, 30)

        self.passwordLabel = QLabel("Password:", self)
        self.passwordLabel.setFont(labelFont)
        self.passwordLabel.setGeometry(80, 300, 100, 30)

        self.passwordInput = QLineEdit(self)
        self.passwordInput.setEchoMode(QLineEdit.Password)
        self.passwordInput.setFixedSize(200, 30)
        self.passwordInput.setGeometry(80, 330, 200, 30)



        self.loginButton = QPushButton("Login", self)
        self.loginButton.setDefault(True)
        self.loginButton.clicked.connect(self.loginAuthorization)
        self.loginButton.setFixedSize(150, 40) 
        self.loginButton.setGeometry(105, 400, 200, 40)


        self.goToRegistrationButton = QPushButton("Register Account", self)
        self.goToRegistrationButton.setDefault(True)
        self.goToRegistrationButton.clicked.connect(self.selectRegisterPageFunction)
        self.goToRegistrationButton.setFixedSize(150, 40)
        self.goToRegistrationButton.setGeometry(105, 450, 200, 40)


        self.show()


    def selectRegisterPageFunction(self):
        self.messageBox = QMessageBox()
        self.messageBox.setWindowTitle("Registration options")
        self.messageBox.setText("Choose Which Registration Page")
        clinicButton = self.messageBox.addButton("Clinic", QMessageBox.ActionRole)
        patientButton = self.messageBox.addButton("Patient", QMessageBox.ActionRole)
        doctorButton = self.messageBox.addButton("Doctor", QMessageBox.ActionRole)
        cancelButton = self.messageBox.addButton("Cancel", QMessageBox.RejectRole)
        self.messageBox.exec_()

        if self.messageBox.clickedButton() == cancelButton:
           self.messageBox.done(QMessageBox.Accepted) 
        elif self.messageBox.clickedButton() == clinicButton:
            self.openClinicRegisterWindow()
        elif self.messageBox.clickedButton() == patientButton:
            self.openPatientRegisterWindow()
        elif self.messageBox.clickedButton() == doctorButton:
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




