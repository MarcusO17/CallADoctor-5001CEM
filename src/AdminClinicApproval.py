import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize, QPoint
from PyQt5.QtGui import QFont, QPixmap, QIcon, QImage, QBrush, QColor
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QMessageBox, QHBoxLayout, QApplication, \
    QScrollArea, QGraphicsDropShadowEffect
from PyQt5 import QtWidgets
from .model import Clinic
from .PageManager import PageManager



class AdminClinicApprovalWindow(QMainWindow):

    def __init__(self, clinicTemp, adminID):
        super().__init__()
        #set the information here
        self.pageManager = PageManager()
        self.clinic = clinicTemp
        self.adminID = adminID
        self.setWindowTitle("Clinic Details")
        self.setFixedWidth(1280)
        self.setFixedHeight(720)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("clinic_details")
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

        # this is the header (logo, title, my back button
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.setAutoFillBackground(True)
        palette = self.palette()
        gradient = "qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(208, 191, 255, 255), stop:1 rgba(113, 58, 190, 255));"
        palette.setBrush(self.backgroundRole(), QBrush(QColor(0, 0, 0, 0)))
        self.setPalette(palette)
        self.setStyleSheet(f"QWidget#centralWidget {{background: {gradient}}};")

        # header (probably reused in most files)
        self.headerTitle = QLabel(self.centralWidget)
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(28)
        self.headerTitle.setFont(font)
        self.headerTitle.setText(self.clinic.getClinicName())
        self.headerTitle.setObjectName("headerTitle")
        self.headerTitle.setFrameShape(QtWidgets.QFrame.Box)
        self.headerTitle.setGeometry(QRect(230, 40, 800, 70))
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
        self.backButton = QPushButton(self.centralWidget)
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

        # Making a container for the Clinic Details, this will also inlcude
        # the Approval & Disapproval Button 

        self.adminClinicApprovalContainer = QLabel(self.centralWidget)
        self.adminClinicApprovalContainer.setFixedSize(1000,500)
        self.adminClinicApprovalContainer.setFrameShape(QtWidgets.QFrame.Box)
        self.adminClinicApprovalContainer.setObjectName("approvalDetailsContainer")
        self.adminClinicApprovalContainer.setStyleSheet("""QLabel#approvalDetailsContainer {
                                                            background: #D0BFFF;
                                                            border-radius: 10px;
                                                            }""")
        
        # Created to display the Description title
        
        self.adminClinicApprovalDescriptionTitle = QLabel(self.centralWidget)
        self.adminClinicApprovalDescriptionTitle.setGeometry(QRect(180, 190, 150, 40))
        self.adminClinicApprovalDescriptionTitle.setText("Clinic Description: ")

        # Below QLabel is created to display the description of the clniic - ID, Name, and the Stutus
        self.adminClinicApprovalDescriptionLabel = QLabel(self.centralWidget)
        self.adminClinicApprovalDescriptionLabel.setGeometry(QRect(180, 220, 400, 200))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.adminClinicApprovalDescriptionLabel.setFont(font)
        self.adminClinicApprovalDescriptionLabel.setText(f"Clinic ID: {self.clinic.getClinicID()} \nClinic Name: {self.clinic.getClinicName()} \nClinic Status: {self.clinic.getClinicStatus()}")
        self.adminClinicApprovalDescriptionLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.adminClinicApprovalDescriptionLabel.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.adminClinicApprovalDescriptionLabel.setWordWrap(True)
        self.adminClinicApprovalDescriptionLabel.setStyleSheet("""QLabel {
                                                                border-radius: 10px;
                                                                border: 1px solid black;
                                                                background: white;
                                                                }""")
        
        # Creatied to display the Certificaction Title
        self.adminGetClinicCertificationTitle = QLabel(self.centralWidget)
        self.adminGetClinicCertificationTitle.setGeometry(QRect(730, 190, 150, 40))
        self.adminGetClinicCertificationTitle.setText("Clinic Certification: ")

        # Qlabel to display the Certificate or the attachment to be displayed. 
        
        self.adminGetClinicCertificationLabel = QLabel(self.centralWidget)
        self.adminGetClinicCertificationLabel.setGeometry(QRect(730, 220, 375, 200))
        self.adminGetClinicCertificationLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.adminGetClinicCertificationIcon = QPixmap.fromImage(QImage.fromData(self.clinic.getCertification()))
        self.adminGetClinicCertificationIcon = self.adminGetClinicCertificationIcon.scaled(375, 200)
        self.adminGetClinicCertificationLabel.setPixmap(self.adminGetClinicCertificationIcon)
        self.adminGetClinicCertificationLabel.setStyleSheet("""QLabel {
                                                                border-radius: 10px;
                                                                border: 1px solid black;
                                                                background: white;
                                                                }""")

        # Created to Display the Address title
        self.adminClinicApprovalAddressTitle = QLabel(self.centralWidget)
        self.adminClinicApprovalAddressTitle.setGeometry(QRect(180, 420, 150, 40))
        self.adminClinicApprovalAddressTitle.setText("Clinic Address: ")


        # QLabel to display the Clinic's Address
        self.adminClinicApprovalAddressLabel = QLabel(self.centralWidget)
        self.adminClinicApprovalAddressLabel.setGeometry(QRect(180, 450, 350, 200))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.adminClinicApprovalAddressLabel.setFont(font)
        self.adminClinicApprovalAddressLabel.setText(self.clinic.getClinicAddress())
        self.adminClinicApprovalAddressLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.adminClinicApprovalAddressLabel.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.adminClinicApprovalAddressLabel.setWordWrap(True)
        self.adminClinicApprovalAddressLabel.setStyleSheet("""QLabel {
                                                                border-radius: 10px;
                                                                border: 1px solid black;
                                                                background: white;
                                                                }""")

        # QPushButton for Approving the Clinic, connecting it to a method 
        # which approves the Clinic. 
        self.adminApproveClinicButton = QPushButton(self.centralWidget)
        self.adminApproveClinicButton.setGeometry(QRect(710, 450, 375, 100))
        font = QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.adminApproveClinicButton.setFont(font)
        self.adminApproveClinicButton.setLayoutDirection(Qt.LeftToRight)
        self.adminApproveClinicButton.setText("Approve Clinic")
        self.adminApproveClinicButton.clicked.connect(self.adminApproveClinicFunction)
        self.adminApproveClinicButton.setStyleSheet("""QPushButton {
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
        self.adminApproveClinicButton.raise_()


        # Code for showing the icon on the button
        self.adminApproveClinicLabel = QLabel(self.centralWidget)
        self.adminApproveClinicLabel.setGeometry(QRect(730, 475, 50, 50))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-good-quality-50.png")
        self.adminApproveClinicIcon = QPixmap(filepath)
        self.adminApproveClinicIcon = self.adminApproveClinicIcon.scaled(50, 50)
        self.adminApproveClinicLabel.setPixmap(self.adminApproveClinicIcon)
        
        # QPushButton for Disapproving the Clinic. Connected to a method 
        # which disapproves the clinic
        self.adminDisapproveClinicButton = QPushButton(self.centralWidget)
        self.adminDisapproveClinicButton.setGeometry(QRect(710, 565, 375, 100))
        self.adminDisapproveClinicButton.setFont(font)
        self.adminDisapproveClinicButton.setLayoutDirection(Qt.LeftToRight)
        self.adminDisapproveClinicButton.setText(" Disapprove Clinic")
        self.adminDisapproveClinicButton.clicked.connect(self.adminDisapproveClinicFunction)
        self.adminDisapproveClinicButton.setStyleSheet("""QPushButton {
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
        self.adminDisapproveClinicButton.raise_()


        # Qlabel used for showing the icon on the button 

        self.adminDisapproveClinicIconLabel = QLabel(self.centralWidget)
        self.adminDisapproveClinicIconLabel.setGeometry(QRect(730, 590, 50, 50))
        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-dislike-or-disagree-thumbs-down-symbol-under-circle-24.png")
        self.adminDisapproveClinicButtonIcon = QPixmap(filepath)
        self.adminDisapproveClinicButtonIcon = self.adminDisapproveClinicButtonIcon.scaled(50, 50)
        self.adminDisapproveClinicIconLabel.setPixmap(self.adminDisapproveClinicButtonIcon)

        # Spacers are used to move the position of things in the layout 
        topSpacer = QWidget()
        topSpacer.setFixedHeight(150)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(topSpacer)
        mainLayout.addWidget(self.adminClinicApprovalContainer)
        mainLayout.setAlignment(Qt.AlignHCenter)

        self.centralWidget.setLayout(mainLayout)
        MainWindow.setCentralWidget(self.centralWidget)

        QMetaObject.connectSlotsByName(MainWindow)


    # Method to Approve the Clinic, displays message box for confirmation

    def adminApproveClinicFunction(self):
        adminApproveClinicDialogBox = QMessageBox.question(self.centralWidget, "Approval Confirmation", 
                                                          "Are you sure you want to Approve this Clinic?",
                                               QMessageBox.Yes | QMessageBox.No)
        if adminApproveClinicDialogBox == QMessageBox.Yes:
            self.clinic.approve()
            print(self.clinic.getClinicStatus())
            self.pageManager.getPreviousPage().generateViewApprovalButtons()
            self.pageManager.goBack()

    # Method to Disapprove the clinic, displays message box for Confirmation. 

    def adminDisapproveClinicFunction(self):
        adminDisapproveClinicDialogBox = QMessageBox.question(self.centralWidget, "Disapproval Confirmation",
                                                          "Are you sure you want to disapprove this Clinic?",
                                                          QMessageBox.Yes | QMessageBox.No)
        if adminDisapproveClinicDialogBox == QMessageBox.Yes:
            self.clinic.cancel()
            self.pageManager.getPreviousPage().generateViewApprovalButtons()
            print(self.clinic.getClinicStatus())
            self.pageManager.goBack()

    def backButtonFunction(self):
        self.pageManager.goBack()