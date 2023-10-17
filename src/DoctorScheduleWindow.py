import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QApplication, QGridLayout, QVBoxLayout
from PyQt5 import QtWidgets

from PatientClinicsNearbyWindow import PatientClinicsNearbyWindow



class DoctorScheduleWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Homepage")
        self.setFixedWidth(1280)
        self.setFixedHeight(720)

        self.setupUi(self)

    def goToClinicsNearby(self):
        self.nearbyClinicWindow = PatientClinicsNearbyWindow()
        self.nearbyClinicWindow.show()
        self.close()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Homepage")
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
        HEIGHT = 6
        WIDTH = 8

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.topLeftLogo = QLabel(self.centralwidget)
        self.topLeftLogo.setGeometry(QRect(20, 10, 60, 60))
        self.topLeftLogo.setFrameShape(QtWidgets.QFrame.Box)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.topLeftLogoIcon = QPixmap(filepath)
        self.topLeftLogoIcon = self.topLeftLogoIcon.scaled(60, 60)
        self.topLeftLogo.setPixmap(self.topLeftLogoIcon)

        self.homepageTitle = QLabel(self.centralwidget)
        self.homepageTitle.setGeometry(QRect(200, 40, 800, 70))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.homepageTitle.setFont(font)
        self.homepageTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.homepageTitle.setText("Welcome! [name]")
        self.homepageTitle.setAlignment(Qt.AlignCenter)

        self.myAccountButton = QPushButton(self.centralwidget)
        self.myAccountButton.setGeometry(QRect(1050, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.myAccountIcon = QIcon(filepath)
        self.myAccountButton.setIconSize(QSize(70,70))
        self.myAccountButton.setIcon(self.myAccountIcon)

        # Push Button 5 (Log Out)
        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setGeometry(QRect(1150, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.backIcon = QIcon(filepath)
        self.backButton.setIconSize(QSize(70, 70))
        self.backButton.setIcon(self.backIcon)

        self.scheduleGridBox = QGridLayout()

        for h in range(HEIGHT):
            for w in range(WIDTH):
                cellLayout = QVBoxLayout()
                temptext = QLabel()
                temptext.setFixedSize(50,50)
                temptext.setStyleSheet("background-color: red;")
                temptext.setText(str(h) + ", " + str(w))
                cellLayout.addWidget(temptext)
                self.scheduleGridBox.addLayout(cellLayout, h, w)

        self.clearButton = QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QRect(1050, 600, 90, 90))
        self.clearButton.setText("Clear")
        self.clearButton.setStyleSheet("background-color: blue;")
        self.clearButton.clicked.connect(self.clearButtonFunction)


        mainLayout = QVBoxLayout()
        mainLayout.addLayout(self.scheduleGridBox)

        self.centralwidget.setLayout(mainLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(MainWindow)

    def clearButtonFunction(self):
        HEIGHT = 6
        WIDTH = 8
        row = 2
        col = 3

        cell_layout = self.scheduleGridBox.itemAtPosition(row, col)

        if cell_layout is not None:
            widget = cell_layout.widget()
            if widget is not None:
                #cell_layout.removeItem(widget)
                widget.deleteLater()

def runthiswindow():
    app = QApplication(sys.argv)
    window = DoctorScheduleWindow()
    window.show()
    sys.exit(app.exec_())

runthiswindow()
