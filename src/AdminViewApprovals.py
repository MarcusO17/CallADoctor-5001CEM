import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize, QPoint
from PyQt5.QtGui import QFont, QPixmap, QIcon, QColor, QBrush
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea, QSizePolicy, QGraphicsDropShadowEffect
from PyQt5 import QtWidgets
from .AdminClinicApproval import AdminClinicApprovalWindow
from .model.Clinic import Clinic
from .model.ClinicRepo import ClinicRepository
from .PageManager import PageManager



class AdminViewApprovalsWindow(QMainWindow):
    def __init__(self, adminID):
        super().__init__()
        self.adminID = adminID
        self.pageManager = PageManager()
        self.setWindowTitle("View Clinics waiting for Approval")
        self.setFixedWidth(1280)
        self.setFixedHeight(720)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("AdminViewApprovals")
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
        self.headerTitle.setText("Clinics waiting approval")
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

        self.buttonContainer = QWidget()
        self.buttonContainer.setObjectName("buttonContainer")
        self.buttonContainer.setStyleSheet("""QWidget#buttonContainer {
                                                            background: #D0BFFF;
                                                            border-radius: 10px;
                                                            }""")
        buttonLayout = QVBoxLayout(self.buttonContainer)
        buttonLayout.setSpacing(20)
        self.buttonContainer.setContentsMargins(20,20,20,20)
        boxScrollArea = QScrollArea()
        boxScrollArea.setObjectName("scrollArea")
        boxScrollArea.setWidgetResizable(True)
        boxScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        

        self.clinicList = ClinicRepository.getClinicUnapprovedList()

        self.generateViewApprovalButtons()

        boxScrollArea.setWidget(self.buttonContainer)
        boxScrollArea.setFixedSize(1000,500)
        boxScrollArea.setStyleSheet("""QScrollArea#scrollArea {
                                                    background: #D0BFFF;
                                                    border-radius: 10px;
                                                    }""")
        topSpacer = QWidget()
        topSpacer.setFixedHeight(150)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(topSpacer)
        mainLayout.addWidget(boxScrollArea)
        mainLayout.setAlignment(Qt.AlignHCenter)

        self.centralwidget.setLayout(mainLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        QMetaObject.connectSlotsByName(MainWindow)

    def approvalClinicButtonFunction(self, clinic, adminID):

        self.AdminClinicApproval = AdminClinicApprovalWindow(clinic, adminID)
        self.pageManager.add(self.AdminClinicApproval)

    def backButtonFunction(self):
        self.pageManager.goBack()
    
    def generateViewApprovalButtons(self):

        for i in range(self.buttonContainer.layout().count()):
            widget = self.buttonContainer.layout().itemAt(0).widget()
            self.buttonContainer.layout().removeWidget(widget)
            if widget is not None:
                widget.deleteLater()

        self.clinicList.clear()
        
        #Get Clinics with disapprove status
        self.clinicList = ClinicRepository.getClinicUnapprovedList()

        buttonFont = QFont()
        buttonFont.setFamily("Arial")
        buttonFont.setPointSize(28)
        buttonFont.setBold(True)
        buttonFont.setWeight(75)

        #Insert All the Clinics 
        for count, clinic in enumerate(self.clinicList):
            self.approvalClinicButton = QPushButton()
            self.approvalClinicButton.setText(f"{clinic.getClinicID()} - {clinic.getClinicName()} - {clinic.getClinicStatus()}")
            self.approvalClinicButton.setFont(buttonFont)
            self.approvalClinicButton.setFixedSize(QSize(900,150))
            self.approvalClinicButton.clicked.connect(lambda checked, clinic=clinic: self.approvalClinicButtonFunction(clinic, self.adminID))
            self.buttonContainer.layout().addWidget(self.approvalClinicButton)
            self.approvalClinicButton.setStyleSheet("""QPushButton {
                                                    background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                                            stop: 0 rgba(10, 2, 85, 255), 
                                                                            stop: 1 rgba(59, 41, 168, 255));
                                                    border-radius: 10px; color: white;
                                                    text-align: center; 
                                                    padding-left: 20px;
                                                    }
                                                    QPushButton:hover
                                                    {
                                                      background-color: #7752FE;
                                                      text-align: center; 
                                                      padding-left: 20px;
                                                    }""")

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.buttonContainer.layout().addWidget(spacer)