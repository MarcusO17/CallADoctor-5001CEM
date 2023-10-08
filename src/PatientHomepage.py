import os
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QGridLayout


class PatientHomepage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Homepage")
        self.setFixedWidth(1280)
        self.setFixedHeight(720)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Homepage")
        self.setGeometry(100, 100, 400, 300)
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        headerFont = QFont()
        headerFont.setFamily("Poppins")
        headerFont.setBold(True)
        headerFont.setPointSize(36)

        patientHomepageLayout = QVBoxLayout()
        headerButtonLayout = QHBoxLayout()
        headerLayout = QVBoxLayout()
        buttonGridLayout = QGridLayout()

        headerLayout.setSpacing(0)

        title = QLabel("Welcome!")
        title.setFont(headerFont)
        title.setFixedSize(500,50)
        title.setContentsMargins(50,100,0,0)

        logoButton = QPushButton()
        filename = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        logoButton.setIcon(QIcon(filename))
        logoButton.setFixedSize(70,70)

        logoutButton = QPushButton()
        logoutButton.setText("Log Out")
        logoutButton.setFixedSize(70,70)

        myAccountButton = QPushButton()
        myAccountButton.setText("My Account")
        myAccountButton.setFixedSize(70,70)

        headerButtonLayout.addWidget(logoButton, alignment=Qt.AlignTop | Qt.AlignLeft)
        headerButtonRightLayout = QHBoxLayout()
        headerButtonRightLayout.addWidget(logoutButton, alignment=Qt.AlignTop)
        headerButtonRightLayout.addWidget(myAccountButton, alignment=Qt.AlignTop)

        headerButtonLayout.addLayout(headerButtonRightLayout)
        headerButtonLayout.setSizeConstraint(QHBoxLayout.SetMinimumSize)

        headerLayout.addLayout(headerButtonLayout)
        headerLayout.addWidget(title, alignment=Qt.AlignTop | Qt.AlignHCenter)
        headerLayout.setSizeConstraint(QVBoxLayout.SetMinimumSize)

        clinicButton = QPushButton()
        clinicButton.setStyleSheet("border: 1px solid #000000; border-radius: 5px; background-color: #f5f5f5;")

        #get clinic icon
        filename = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        clinicButton.setIcon(QIcon(filename))
        clinicButton.setText("Clinics Nearby")
        #implement the function
        #clinicButton.clicked.connect(gotoClinicsNearby)

        myPrescriptionButton = QPushButton()
        myPrescriptionButton.setStyleSheet("border: 1px solid #000000; border-radius: 5px; background-color: #f5f5f5;")

        # get clinic icon
        filename = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        myPrescriptionButton.setIcon(QIcon(filename))
        myPrescriptionButton.setText("My Prescription")
        # implement the function
        #myPrescriptionButton.clicked.connect(gotoMyPrescription)

        myAppointmentsButton = QPushButton()
        myAppointmentsButton.setStyleSheet("border: 1px solid #000000; border-radius: 5px; background-color: #f5f5f5;")

        # get clinic icon
        filename = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        myAppointmentsButton.setIcon(QIcon(filename))
        myAppointmentsButton.setText("My Appointments")
        # implement the function
        # myAppointmentsButton.clicked.connect(gotoMyPrescription)

        clinicButton.setFixedSize(300,100)
        myPrescriptionButton.setFixedSize(300, 100)
        myAppointmentsButton.setFixedSize(300, 100)

        buttonGridLayout.addWidget(clinicButton, 0, 0)
        buttonGridLayout.addWidget(myPrescriptionButton, 0, 1)
        buttonGridLayout.addWidget(myAppointmentsButton, 1, 0)


        patientHomepageLayout.addLayout(headerLayout)
        patientHomepageLayout.addLayout(buttonGridLayout)
        central_widget = QWidget()
        central_widget.setLayout(patientHomepageLayout)
        self.setCentralWidget(central_widget)

# for debugging please remove when done
def runHomepage():
    app = QApplication(sys.argv)
    loginWindow = PatientHomepage()
    loginWindow.show()
    sys.exit(app.exec_())

runHomepage()