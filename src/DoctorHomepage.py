import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QCoreApplication, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore

from DoctorScheduleWindow import DoctorScheduleWindow


class DoctorHomepage(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Doctor Homepage")
        self.setFixedWidth(1280)
        self.setFixedHeight(720)
        self.setupUi(self)

    def gotoSchedule(self):
        self.doctorScheduleWindow = DoctorScheduleWindow()
        self.doctorScheduleWindow.show()
        self.close()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("DoctorHomepage")
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        
#Push Button 1 (Schedule Button)
        self.ScheduleButton = QtWidgets.QPushButton(self.centralwidget)
        self.ScheduleButton.setGeometry(QtCore.QRect(50, 150, 400, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.ScheduleButton.setFont(font)
        self.ScheduleButton.setObjectName("schedule")
        self.ScheduleButton.setText("Schedule")
        self.ScheduleButton.clicked.connect(self.gotoSchedule)


#Push button_2 (Patient Record)
        self.PatientRecordButton = QtWidgets.QPushButton(self.centralwidget)
        self.PatientRecordButton.setGeometry(QtCore.QRect(430, 150, 400, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.PatientRecordButton.setFont(font)
        self.PatientRecordButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.PatientRecordButton.setObjectName("PatientRecord")
        self.PatientRecordButton.setText("Patient Record")


#Icon for Schedule - set as label 1
        self.Schedulelabel = QtWidgets.QLabel(self.centralwidget)
        self.Schedulelabel.setGeometry(QtCore.QRect(70, 170, 51, 51))
        self.Schedulelabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.ScheduleIcon = QPixmap(filepath)
        self.ScheduleIcon = self.ScheduleIcon.scaled(50, 50)
        self.Schedulelabel.setPixmap(self.ScheduleIcon)


#icon for Patient Record - set as label 2        
        self.PatientRecordLabel = QtWidgets.QLabel(self.centralwidget)
        self.PatientRecordLabel.setGeometry(QtCore.QRect(450, 170, 51, 51))
        self.PatientRecordLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.PatientRecordIcon = QPixmap(filepath)
        self.PatientRecordIcon = self.PatientRecordIcon.scaled(50, 50)
        self.PatientRecordLabel.setPixmap(self.PatientRecordIcon)


#Push Button 3 (My Appointments)
        self.DocMyAppointmentsButton = QtWidgets.QPushButton(self.centralwidget)
        self.DocMyAppointmentsButton.setGeometry(QtCore.QRect(50, 310, 400, 100))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.DocMyAppointmentsButton.setFont(font)
        self.DocMyAppointmentsButton.setObjectName("DocMyAppointments")
        self.DocMyAppointmentsButton.setLayoutDirection(Qt.LeftToRight)
        self.DocMyAppointmentsButton.setText("My Appointments")


#icon for My Appointments - set as label 3
        self.DocMyAppointmentsLabel = QtWidgets.QLabel(self.centralwidget)
        self.DocMyAppointmentsLabel.setGeometry(QtCore.QRect(70, 330, 51, 51))
        self.DocMyAppointmentsLabel.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.DocMyAppointmentsIcon = QPixmap(filepath)
        self.DocMyAppointmentsIcon = self.DocMyAppointmentsIcon.scaled(50, 50)
        self.DocMyAppointmentsLabel.setPixmap(self.DocMyAppointmentsIcon)


#icon for the mainpage LOGO - set as Label 4
        self.DocPageLogo = QtWidgets.QLabel(self.centralwidget)
        self.DocPageLogo.setGeometry(QtCore.QRect(20, 10, 60, 60))
        self.DocPageLogo.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.DocPageLogoIcon = QPixmap(filepath)
        self.DocPageLogoIcon = self.DocPageLogoIcon.scaled(50, 50)
        self.DocPageLogo.setPixmap(self.DocPageLogoIcon)


#Main Page Title - Set as Label 5
        self.DocMainTitle = QtWidgets.QLabel(self.centralwidget)
        self.DocMainTitle.setGeometry(QtCore.QRect(130, 40, 441, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.DocMainTitle.setFont(font)
        self.DocMainTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.DocMainTitle.setText("Welcome! Dr [Name]")
        self.DocMainTitle.setAlignment(Qt.AlignCenter)


#Push Button 4 (My Account)
        self.DocMyAccountButton = QtWidgets.QPushButton(self.centralwidget)
        self.DocMyAccountButton.setGeometry(QtCore.QRect(720, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.DocMyAccountIcon = QIcon(filepath)
        self.DocMyAccountButton.setIconSize(QSize(70,70))
        self.DocMyAccountButton.setIcon(self.DocMyAccountIcon)


#Push Button 5 (Log Out)
        self.DocLogoutButton = QtWidgets.QPushButton(self.centralwidget)
        self.DocLogoutButton.setGeometry(QtCore.QRect(1150, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.DocLogoutIcon = QIcon(filepath)
        self.DocLogoutButton.setIconSize(QSize(70, 70))
        self.DocLogoutButton.setIcon(self.DocLogoutIcon)


        MainWindow.setCentralWidget(self.centralwidget)


        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
def runthiswindow():
    app = QApplication(sys.argv)
    window = DoctorHomepage()
    window.show()
    sys.exit(app.exec_())

runthiswindow()