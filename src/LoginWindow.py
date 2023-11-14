from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QFont, QPixmap, QPalette, QColor, QBrush, QLinearGradient, QMovie
from PyQt5.QtWidgets import QLabel, QLineEdit, QPushButton, QVBoxLayout,QHBoxLayout, QWidget, QMessageBox, QApplication, \
QFrame, QAction, QSpacerItem, QSizePolicy
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
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        titleFont = QFont()
        titleFont.setFamily("Poppins")
        titleFont.setPointSize(40)

        self.titleLabel = QLabel("Call-A-Doctor Application", self)
        self.titleLabel.setStyleSheet("color: Black;")
        self.titleLabel.setFont(titleFont)
        self.titleLabel.setGeometry(110, 10, 700, 65)

        subTitleFont = QFont()
        subTitleFont.setFamily("Poppins")
        subTitleFont.setPointSize(25)

        self.subTitleLabel = QLabel("Can't go to the hospital? Call them at your doorstep!", self)
        self.subTitleLabel.setStyleSheet("color: White;")
        self.subTitleLabel.setFont(subTitleFont)
        self.subTitleLabel.setGeometry(20, 530, 790, 65)

        self.setAutoFillBackground(True)
        palette = self.palette()
        gradient = "qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(208, 191, 255, 255), stop:1 rgba(113, 58, 190, 255));"
        palette.setBrush(self.backgroundRole(), QBrush(QColor(0, 0, 0, 0)))
        self.setPalette(palette)
        self.setStyleSheet(f"QWidget#LoginWindow {{background: {gradient}}};")

        self.borderFrame = QFrame(self)
        self.borderFrame.setGeometry(-10, 75, 310, 450)  # Adjusted geometry
        self.borderFrame.setFrameShape(QFrame.StyledPanel)
        self.borderFrame.setLineWidth(2)

        gradient = QLinearGradient(0, 0, 0, self.borderFrame.height())
        gradient.setColorAt(0, QColor(25, 4, 130))
        gradient.setColorAt(1, QColor(119, 82, 254))

        self.borderFrame.setStyleSheet("""
            QFrame {
                border: 2px dashed ;
                border-radius: 15px;  /* Adjust the radius as needed */
                background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1,
                                            stop: 0 rgba(25, 4, 130, 255),
                                            stop: 1 rgba(119, 82, 254, 255)
                                            );
            }
        """)
        
        
        gifViewer = QLabel(self)

        gifPath = os.path.join(CURRENT_DIRECTORY, "resources\\running-doctor1.gif")

        movie = QMovie(gifPath)
        gifViewer.setMovie(movie)

        movie.start()

        gifViewer.setScaledContents(True)
        gifViewer.setFixedSize(400,400)


        mainLayout=QVBoxLayout(self)

        spacerItem = QWidget()
        spacerItem.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        spacerItem.setFixedWidth(300)
        horizontal_spacer_item = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        mainLayout.addItem(horizontal_spacer_item)
        gifViewer.setGeometry(QRect(50, 60, 200, 200))
        
        mainLayout.addWidget(spacerItem)
        mainLayout.addWidget(gifViewer)


        self.logoLabel = QLabel(self)

        filename = os.path.join(CURRENT_DIRECTORY, "resources\\CaD-Logo.png")

        try:
            logoPixmap = QPixmap(filename)
            logoPixmap = logoPixmap.scaled(200,200)
            self.logoLabel.setPixmap(logoPixmap)
            self.logoLabel.setGeometry(QRect(50, 60, 200, 200))


        except Exception as e:
            print(e)



        labelFont = QFont()
        labelFont.setFamily("Poppins")
        labelFont.setPointSize(12)

        self.emailLabel = QLabel("Email:", self)
        self.emailLabel.setStyleSheet("color: white;")
        self.emailLabel.setFont(labelFont)
        self.emailLabel.setGeometry(QRect(50, 230, 100, 30))
        
        self.emailInput = QLineEdit(self)
        self.emailInput.setGeometry(QRect(50, 260, 220, 30))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\email.png")

        emailIcon = QPixmap(filepath)
        emailIcon = emailIcon.scaled(30, 30)
        iconLabel = QLabel(self)
        iconLabel.setPixmap(emailIcon)
        iconLabel.setGeometry(QRect(20, 260, 30, 30))        

        self.passwordLabel = QLabel("Password:", self)
        self.passwordLabel.setStyleSheet("color: white;")
        self.passwordLabel.setFont(labelFont)
        self.passwordLabel.setGeometry(QRect(50, 310, 100, 30))

        self.passwordInput = QLineEdit(self)
        self.passwordInput.setEchoMode(QLineEdit.Password)
        self.passwordInput.setGeometry(QRect(50, 340, 220, 30))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\password.png")

        passwordIcon = QPixmap(filepath)
        passwordIcon = passwordIcon.scaled(30, 30)
        icon2Label = QLabel(self)
        icon2Label.setPixmap(passwordIcon)
        icon2Label.setGeometry(QRect(20, 340, 30, 30))

        self.loginButton = QPushButton("Login", self)
        self.loginButton.setDefault(True)
        self.loginButton.clicked.connect(self.loginAuthorization)
        self.loginButton.setFixedSize(150, 40) 
        self.loginButton.setGeometry(QRect(75, 410, 200, 40))


        self.goToRegistrationButton = QPushButton("Register Account", self)
        self.goToRegistrationButton.setDefault(True)
        self.goToRegistrationButton.clicked.connect(self.selectRegisterPageFunction)
        self.goToRegistrationButton.setFixedSize(150, 40)
        self.goToRegistrationButton.setGeometry(QRect(75, 460, 200, 40))


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