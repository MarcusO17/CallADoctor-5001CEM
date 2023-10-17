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
        self.homepageTitle.setText("Welcome! [name]")
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

        self.scheduleGridBox = QGridLayout()

        # header of the grid
        tempTimeStart = 9
        for i in range(WIDTH):
            tempTimeStart = tempTimeStart + 1
            tempTimeEnd = tempTimeStart + 1
            cellLayout = QVBoxLayout()
            timeSlotLabel = QLabel()
            timeSlotLabel.setFixedSize(100,60)
            timeSlotLabel.setText(str(tempTimeStart) + ":00 - " + str(tempTimeEnd)+ ":00")
            cellLayout.addWidget(timeSlotLabel)

            self.scheduleGridBox.addLayout(cellLayout, 0, i+1)

        # side of the grid
        daysOfTheWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        for i in range(HEIGHT):
            cellLayout = QVBoxLayout()
            dayCell = QLabel()
            dayCell.setFixedSize(100, 60)
            dayCell.setText(daysOfTheWeek[i])
            cellLayout.addWidget(dayCell)

            self.scheduleGridBox.addLayout(cellLayout, i+1, 0)


        for h in range(HEIGHT):
            for w in range(WIDTH):
                cellLayout = QVBoxLayout()
                tempButton = QPushButton()
                tempButton.setFixedSize(100,60)
                tempButton.setStyleSheet("background-color: red;border: 10px solid black;")
                tempButton.setText(str(h+1) + ", " + str(w+1))
                tempButton.clicked.connect(lambda checked, h=h, w=w: self.gridLayoutCellButton(h+1, w+1))
                cellLayout.addWidget(tempButton)

                self.scheduleGridBox.addLayout(cellLayout, h+1, w+1)

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
        row = 2
        col = 3
        layoutTemp = self.scheduleGridBox.itemAtPosition(row, col)
        if layoutTemp is not None:
            widgetTemp = layoutTemp.itemAt(0).widget()
            widgetTemp.setStyleSheet("background-color: green;")

    def gridLayoutCellButton(self, row, col):
        print(row, col)

def runthiswindow():
    app = QApplication(sys.argv)
    window = DoctorScheduleWindow()
    window.show()
    sys.exit(app.exec_())

runthiswindow()
