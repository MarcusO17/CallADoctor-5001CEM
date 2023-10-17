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
        MainWindow.setObjectName("Doctor Schedule")
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
        HEIGHT = 5
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
        self.homepageTitle.setText("Doctor Schedule")
        self.homepageTitle.setAlignment(Qt.AlignCenter)

        self.myAccountButton = QPushButton(self.centralwidget)
        self.myAccountButton.setGeometry(QRect(1050, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.myAccountIcon = QIcon(filepath)
        self.myAccountButton.setIconSize(QSize(70,70))
        self.myAccountButton.setIcon(self.myAccountIcon)

        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setGeometry(QRect(1150, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo-placeholder-image.png")
        self.backIcon = QIcon(filepath)
        self.backButton.setIconSize(QSize(70, 70))
        self.backButton.setIcon(self.backIcon)

        self.timeSlotButtonList = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

        # header of the grid
        timeStart = 9
        timeSlotLabelXStart = 300
        for i in range(WIDTH):
            timeStart = timeStart + 1
            timeEnd = timeStart + 1
            timeSlotLabel = QLabel(self.centralwidget)
            timeSlotLabel.setGeometry(QRect(timeSlotLabelXStart,150,100,60))
            timeSlotLabel.setStyleSheet("border: 1px solid black;")
            timeSlotLabel.setText(str(timeStart) + ":00 - " + str(timeEnd)+ ":00")
            timeSlotLabelXStart = timeSlotLabelXStart + 100

        dayCellYStart = 210
        # side of the grid
        daysOfTheWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        for i in range(HEIGHT):
            dayCell = QLabel(self.centralwidget)
            dayCell.setGeometry(QRect(200, dayCellYStart, 100, 60))
            dayCell.setStyleSheet("border: 1px solid black;")
            dayCell.setText(daysOfTheWeek[i])
            dayCellYStart = dayCellYStart + 60

        tempButtonYStart = 150
        for h in range(HEIGHT):
            tempButtonXStart = 300
            tempButtonYStart = tempButtonYStart + 60
            for w in range(WIDTH):
                timeSlotButton = QPushButton(self.centralwidget)
                timeSlotButton.setGeometry(QRect(tempButtonXStart, tempButtonYStart, 100, 60))
                timeSlotButton.setStyleSheet("border: 1px solid black;")
                timeSlotButton.setText(str(h+1) + ", " + str(w+1))
                timeSlotButton.clicked.connect(lambda checked, h=h, w=w: self.timeSlotButtonFunction(h+1, w+1))
                tempButtonXStart = tempButtonXStart + 100
                self.timeSlotButtonList[h][w] = timeSlotButton

        self.clearButton = QPushButton(self.centralwidget)
        self.clearButton.setGeometry(QRect(1050, 600, 90, 90))
        self.clearButton.setText("Clear")
        self.clearButton.setStyleSheet("background-color: blue;")
        self.clearButton.clicked.connect(lambda: self.clearButtonFunction(row=1, col=3))

        MainWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(MainWindow)

    def timeSlotButtonFunction(self, row, col):
        print(row, col)

    def clearButtonFunction(self, row, col):
        self.timeSlotButtonList[row][col].setText("")

def runthiswindow():
    app = QApplication(sys.argv)
    window = DoctorScheduleWindow()
    window.show()
    sys.exit(app.exec_())

runthiswindow()
