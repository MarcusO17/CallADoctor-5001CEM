import os
import sys

from .model import Clinic
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize, QPoint
from PyQt5.QtGui import QFont, QPixmap, QIcon, QBrush, QColor, QLinearGradient
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QApplication, QMessageBox, QGraphicsDropShadowEffect
from PyQt5 import QtWidgets
from .ClinicManageSchedule import ClinicManageSchedule
from .AdminViewApprovals import AdminViewApprovalsWindow
from .AdminViewClinics import AdminViewClinicsWindow
from .PageManager import PageManager



class AdminHomepageWindow(QMainWindow):
    def __init__(self, sessionID):
        super().__init__()
        self.adminID = sessionID

        self.pageManager = PageManager()
        self.setWindowTitle("Homepage")
        self.setFixedWidth(1280)
        self.setFixedHeight(720)

        self.setupUi(self)

    def goToViewClinics(self):
        self.viewClinics = AdminViewClinicsWindow(self.adminID)
        self.pageManager.add(self.viewClinics)

    def goToViewApprovals(self):
        self.viewApprovals = AdminViewApprovalsWindow(self.adminID)
        self.pageManager.add(self.viewApprovals)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Homepage (Admin)")

        stylesheet = """
                            QPushButton
                            {
                               background-color: #610C9F;
                               border-radius: 10px;
                               color: white;
                               text-align: centre; 
                               padding-left: 10px;
                            }
                            
                            QPushButton:hover
                            {
                              background-color: #7752FE;
                            }
                            """

        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.setAutoFillBackground(True)
        palette = self.palette()
        gradient = "qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(208, 191, 255, 255), stop:1 rgba(113, 58, 190, 255));"
        palette.setBrush(self.backgroundRole(), QBrush(QColor(0, 0, 0, 0)))
        self.setPalette(palette)
        self.setStyleSheet(f"QWidget#centralwidget {{background: {gradient}}};")

        self.viewClinicsButton = QPushButton(self.centralwidget)
        self.viewClinicsButton.setGeometry(QRect(150, 200, 400, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.viewClinicsButton.setFont(font)
        self.viewClinicsButton.setText("View Clinics")
        self.viewClinicsButton.clicked.connect(self.goToViewClinics)
        self.viewClinicsButton.setStyleSheet(stylesheet)
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        self.viewClinicsButton.setGraphicsEffect(effect)

        self.viewClinicsLabel = QLabel(self.centralwidget)
        self.viewClinicsLabel.setGeometry(QRect(170, 225, 50, 50))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-clinic-50.png")
        self.viewClinicsIcon = QPixmap(filepath)
        self.viewClinicsIcon = self.viewClinicsIcon.scaled(50, 50)
        self.viewClinicsLabel.setPixmap(self.viewClinicsIcon)


        self.viewApprovalsButton = QPushButton(self.centralwidget)
        self.viewApprovalsButton.setGeometry(QRect(700, 200, 400, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.viewApprovalsButton.setFont(font)
        self.viewApprovalsButton.setText("View Approvals")
        self.viewApprovalsButton.clicked.connect(self.goToViewApprovals)
        self.viewApprovalsButton.setStyleSheet(stylesheet)
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        self.viewApprovalsButton.setGraphicsEffect(effect)

        self.viewApprovalsLabel = QLabel(self.centralwidget)
        self.viewApprovalsLabel.setGeometry(QRect(720, 225, 50, 50))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-view-32.png")
        self.viewApprovalsIcon = QPixmap(filepath)
        self.viewApprovalsIcon = self.viewApprovalsIcon.scaled(50, 50)
        self.viewApprovalsLabel.setPixmap(self.viewApprovalsIcon)


        self.topLeftLogo = QLabel(self.centralwidget)
        self.topLeftLogo.setGeometry(QRect(5, 0, 200, 200))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\logo.png")
        self.topLeftLogoIcon = QPixmap(filepath)
        self.topLeftLogoIcon = self.topLeftLogoIcon.scaled(200, 200)
        self.topLeftLogo.setPixmap(self.topLeftLogoIcon)

        self.homepageTitle = QLabel(self.centralwidget)
        self.homepageTitle.setGeometry(QRect(200, 40, 800, 70))
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.homepageTitle.setFont(font)
        self.homepageTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.homepageTitle.setText("Welcome Admin!")
        self.homepageTitle.setObjectName("headerTitle") 
        self.homepageTitle.setAlignment(Qt.AlignCenter)

        effect = QGraphicsDropShadowEffect(offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855"))
        self.homepageTitle.setGraphicsEffect(effect)
        self.homepageTitle.setStyleSheet("""QLabel#headerTitle {
                                                background: #D0BFFF;
                                                border-radius: 10px;
                                            }""")

        self.logoutButton = QPushButton(self.centralwidget)
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-logout-64.png")
        self.logoutIcon = QIcon(filepath)
        self.logoutButton.setGeometry(QRect(1050, 40, 200, 70))
        self.logoutButton.setIconSize(QSize(50, 50))
        logoutFont = QFont()
        logoutFont.setFamily("Arial")
        logoutFont.setPointSize(20)
        self.logoutButton.setFont(logoutFont)
        self.logoutButton.setText("Log Out")
        self.logoutButton.setStyleSheet(stylesheet)
        self.logoutButton.setIcon(self.logoutIcon)
        self.logoutButton.clicked.connect(self.logout)
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        self.logoutButton.setGraphicsEffect(effect)


        MainWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(MainWindow)

    def logout(self):

        logoutDialogBox = QMessageBox.question(self.centralwidget, "Logout Confirmation", "Are you sure you want to logout",
                                               QMessageBox.Yes | QMessageBox.No)
        if logoutDialogBox == QMessageBox.Yes:
            self.pageManager.goBack()