import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize, QPoint
from PyQt5.QtGui import QFont, QPixmap, QIcon, QImage, QBrush, QColor
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QHBoxLayout, QApplication, \
    QScrollArea, QGraphicsDropShadowEffect
from PyQt5 import QtWidgets
from .model import Clinic
from .PageManager import PageManager



class AdminViewClinicDetailsWindow(QMainWindow):

    def __init__(self, clinicTemp, adminID):
        super().__init__()
        #set the information here
        self.pageManager = PageManager()
        self.clinic = clinicTemp
        self.adminID = adminID
        print(self.clinic.getClinicID(), self.clinic.getClinicName(), self.clinic.getClinicAddress(), self.clinic.getClinicContact())
        self.setWindowTitle("Clinic Details")
        self.setFixedWidth(1280)
        self.setFixedHeight(720)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("clinic_details")
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        # this is the header (logo, title, my back button
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.setAutoFillBackground(True)
        palette = self.palette()
        gradient = "qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(208, 191, 255, 255), stop:1 rgba(113, 58, 190, 255));"
        palette.setBrush(self.backgroundRole(), QBrush(QColor(0, 0, 0, 0)))
        self.setPalette(palette)
        self.setStyleSheet(f"QWidget#centralwidget {{background: {gradient}}};")

        # header (probably reused in most files)
        self.headerTitle = QLabel(self.centralwidget)
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.headerTitle.setFont(font)
        self.headerTitle.setText(self.clinic.getClinicName())
        self.headerTitle.setObjectName("headerTitle")
        self.headerTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.headerTitle.setGeometry(QRect(225, 40, 800, 70))
        self.headerTitle.setAlignment(Qt.AlignCenter)
        self.headerTitle.setStyleSheet("""QLabel#headerTitle {
                                                            background: #D0BFFF;
                                                            border-radius: 10px;
                                                            }""")
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        self.headerTitle.setGraphicsEffect(effect)


        # Push Button 5 (Log Out)
        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setFixedSize(70, 70)
        self.backButton.setGeometry(QRect(1150, 40, 70, 70))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-back-64.png")
        self.backIcon = QIcon(filepath)
        self.backButton.setIconSize(QSize(70, 70))
        self.backButton.setIcon(self.backIcon)
        self.backButton.setObjectName("backButton")
        self.backButton.clicked.connect(self.backButtonFunction)
        self.backButton.setStyleSheet("""QPushButton#backButton {
                                                        background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                                                stop: 0 rgba(10, 2, 85, 255), 
                                                                                stop: 1 rgba(59, 41, 168, 255));
                                                        border-radius: 10px; color: white;

                                                        }
                                                        QPushButton#backButton:hover
                                                        {
                                                          background-color: #7752FE;
                                                        }""")

        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        self.backButton.setGraphicsEffect(effect)

        
        self.adminClinicDetailsContainer = QLabel(self.centralwidget)
        self.adminClinicDetailsContainer.setFixedSize(1000,500)
        self.adminClinicDetailsContainer.setFrameShape(QtWidgets.QFrame.Box)
        self.adminClinicDetailsContainer.setObjectName("detailsContainer")
        self.adminClinicDetailsContainer.setStyleSheet("""QLabel#detailsContainer {
                                                            background: #D0BFFF;
                                                            border-radius: 10px;
                                                            }""")

        self.adminClinicDetailsDescriptionTitle = QLabel(self.centralwidget)
        self.adminClinicDetailsDescriptionTitle.setGeometry(QRect(180, 190, 150, 40))
        self.adminClinicDetailsDescriptionTitle.setText("Clinic Description: ")

        self.adminClinicDetailsDescriptionLabel = QLabel(self.centralwidget)
        self.adminClinicDetailsDescriptionLabel.setGeometry(QRect(180, 220, 400, 200))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.adminClinicDetailsDescriptionLabel.setFont(font)
        self.adminClinicDetailsDescriptionLabel.setText(f"Clinic ID: {self.clinic.getClinicID()} \n Clinic Name: {self.clinic.getClinicName()} \n Clinic Status: {self.clinic.getClinicStatus()}")
        self.adminClinicDetailsDescriptionLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.adminClinicDetailsDescriptionLabel.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.adminClinicDetailsDescriptionLabel.setStyleSheet("""QLabel {
                                                                border-radius: 10px;
                                                                border: 1px solid black;
                                                                background: white;
                                                                }""")
        
        self.adminClinicDetailsAddressTitle = QLabel(self.centralwidget)
        self.adminClinicDetailsAddressTitle.setGeometry(QRect(180, 420, 150, 40))
        self.adminClinicDetailsAddressTitle.setText("Clinic Address: ")

        self.adminClinicDetailsAddressLabel = QLabel(self.centralwidget)
        self.adminClinicDetailsAddressLabel.setGeometry(QRect(180, 450, 350, 200))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.adminClinicDetailsAddressLabel.setFont(font)
        self.adminClinicDetailsAddressLabel.setText(self.clinic.getClinicAddress())
        self.adminClinicDetailsAddressLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.adminClinicDetailsAddressLabel.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.adminClinicDetailsAddressLabel.setStyleSheet("""QLabel {
                                                                border-radius: 10px;
                                                                border: 1px solid black;
                                                                background: white;
                                                                }""")

        self.adminRemoveClinicButton = QPushButton(self.centralwidget)
        self.adminRemoveClinicButton.setGeometry(QRect(710, 545, 375, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.adminRemoveClinicButton.setFont(font)
        self.adminRemoveClinicButton.setLayoutDirection(Qt.LeftToRight)
        self.adminRemoveClinicButton.setText("Remove Clinic")
        self.adminRemoveClinicButton.clicked.connect(self.adminRemoveClinicFunction)
        self.adminRemoveClinicButton.setStyleSheet("""QPushButton {
                                                        background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                                                stop: 0 rgba(10, 2, 85, 255), 
                                                                                stop: 1 rgba(59, 41, 168, 255));
                                                        border-radius: 10px; color: white;
                                                        text-align: center; 
                                                        color:white;
                                                        }
                                                        QPushButton:hover
                                                        {
                                                          background-color: #7752FE;
                                                          text-align: center; 
                                                          color:white;
                                                        }""")
        self.adminRemoveClinicButton.raise_()

        self.adminRemoveClinicLabel = QLabel(self.centralwidget)
        self.adminRemoveClinicLabel.setGeometry(QRect(730, 570, 50, 50))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-remove-64.png")
        self.adminRemoveClinicIcon = QPixmap(filepath)
        self.adminRemoveClinicIcon = self.adminRemoveClinicIcon.scaled(50, 50)
        self.adminRemoveClinicLabel.setPixmap(self.adminRemoveClinicIcon)

        topSpacer = QWidget()
        topSpacer.setFixedHeight(150)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(topSpacer)
        mainLayout.addWidget(self.adminClinicDetailsContainer)
        mainLayout.setAlignment(Qt.AlignHCenter)

        self.centralwidget.setLayout(mainLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(MainWindow)

    def adminRemoveClinicFunction(self):
        adminClinicRemoveDialogBox = QMessageBox.question(self.centralwidget, "Removal Confirmation", 
                                                          "Are you sure you want to remove this Clinic?",
                                               QMessageBox.Yes | QMessageBox.No)
        if adminClinicRemoveDialogBox == QMessageBox.Yes:
            self.pageManager.goBack()

    def backButtonFunction(self):
        self.pageManager.goBack()