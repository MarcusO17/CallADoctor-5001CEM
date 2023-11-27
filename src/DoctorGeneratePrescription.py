import os
import sys
from PyQt5.QtCore import Qt, QRect, QMetaObject, QSize, QDateTime, QDate, QPoint
from PyQt5.QtGui import QFont, QPixmap, QIcon, QColor
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QApplication, \
    QScrollArea, QLineEdit, QMessageBox, QDialog, QDateEdit, QGraphicsDropShadowEffect
from PyQt5 import QtWidgets

from .AccountPage import AccountPage
from .model import PrescriptionDetails
from .model import Prescription, PrescriptionRepo
from .PageManager import PageManager, FrameLayoutManager


class DoctorGeneratePrescription(QWidget):

    def __init__(self, patient, appointment, doctor):
        super().__init__()

        #set the information here
        self.patient = patient
        self.appointment = appointment
        self.doctor = doctor

        self.frameLayoutManager = FrameLayoutManager()
        self.frameLayout = self.frameLayoutManager.getFrameLayout()
        self.setupUi()

    def setupUi(self):
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
        # this is the header (logo, title, my back button
        self.centralwidget = QWidget()

        self.headerTitle = QLabel(self.centralwidget)
        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(16)
        self.headerTitle.setFont(font)
        self.headerTitle.setText(f"{self.patient.getPatientName()} - Prescription Details")
        self.headerTitle.setObjectName("headerTitle")
        self.headerTitle.setGeometry(QRect(80, 40, 700, 70))
        self.headerTitle.setAlignment(Qt.AlignCenter)
        self.headerTitle.setStyleSheet("""QLabel#headerTitle {
                                        background: #D0BFFF;
                                        border-radius: 10px;
                                        }""")
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        self.headerTitle.setGraphicsEffect(effect)

        self.backButton = QPushButton(self.centralwidget)
        self.backButton.setGeometry(QRect(800, 40, 70, 70))
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

        self.rowContainer = QWidget()
        self.rowContainer.setObjectName("rowContainer")
        self.rowContainer.setStyleSheet("""QWidget#rowContainer {
                                                background: #D0BFFF;
                                                border-radius: 10px;
                                                margin-left: 50px;
                                                }""")
        rowLayout = QVBoxLayout(self.rowContainer)
        self.rowContainer.setContentsMargins(20, 20, 20, 20)
        boxScrollArea = QScrollArea()
        boxScrollArea.setObjectName("scrollArea")
        boxScrollArea.setWidgetResizable(True)
        boxScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        boxScrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.addNewRowButton = QPushButton(self.centralwidget)
        self.addNewRowButton.setGeometry(QRect(140, 120, 150, 50))
        self.addNewRowButton.setText("Add New Row")
        self.addNewRowButton.clicked.connect(self.addNewRow)
        self.addNewRowButton.setStyleSheet("""QPushButton {
                                                background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                                        stop: 0 rgba(10, 2, 85, 255), 
                                                                        stop: 1 rgba(59, 41, 168, 255));
                                                border-radius: 10px; color: white;
                                                text-align: center; 

                                                }
                                                QPushButton:hover
                                                {
                                                  background-color: #7752FE;
                                                  text-align: center; 
                                                }""")

        self.completePrescriptionButton = QPushButton(self.centralwidget)
        self.completePrescriptionButton.setGeometry(QRect(600, 120, 150, 50))
        self.completePrescriptionButton.setText("Complete Prescription")
        self.completePrescriptionButton.clicked.connect(self.completePrescription)
        self.completePrescriptionButton.setStyleSheet("""QPushButton {
                                                        background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                                                stop: 0 rgba(10, 2, 85, 255), 
                                                                                stop: 1 rgba(59, 41, 168, 255));
                                                        border-radius: 10px; color: white;
                                                        text-align: center; 

                                                        }
                                                        QPushButton:hover
                                                        {
                                                          background-color: #7752FE;
                                                          text-align: center; 
                                                        }""")

        boxScrollArea.setWidget(self.rowContainer)
        boxScrollArea.setFixedSize(900, 500)
        boxScrollArea.setStyleSheet("""QScrollArea#scrollArea {
                                    background: #D0BFFF;
                                    border-radius: 10px;
                                    margin-left: 30px;
                                    }""")
        effect = QGraphicsDropShadowEffect(
            offset=QPoint(3, 3), blurRadius=17, color=QColor("#120855")
        )
        boxScrollArea.setGraphicsEffect(effect)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.centralwidget)
        mainLayout.addWidget(boxScrollArea)

        self.setLayout(mainLayout)

    def backButtonFunction(self):
        backConfirmationDialog = QMessageBox.question(self.centralwidget, "Back Confirmation",
                                               "Do you want to discard this prescription",
                                               QMessageBox.Yes | QMessageBox.No)
        if backConfirmationDialog == QMessageBox.Yes:
            self.frameLayoutManager.back()
            self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    def completePrescription(self):
        self.expiryDateDialog = QDialog(self)

        self.expiryDateDialog.move(300,200)
        self.expiryDateDialog.setStyleSheet("""QDialog {background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                stop: 0 rgba(25, 4, 130, 255), 
                                                stop: 1 rgba(119, 82, 254, 255)
                                            );
                                            border-radius: 10px;
                                            }""")
        self.expiryDateDialog.setFixedSize(400, 400)

        self.expiryDateDialog.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)  # Remove close button
        self.expiryDateDialog.setWindowFlag(Qt.FramelessWindowHint)
        self.expiryDateDialog.setWindowTitle("Select An Expiry Date")

        font = QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)

        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)

        titleFont = QFont()
        titleFont.setFamily("Montserrat")
        titleFont.setPointSize(10)

        self.expiryDateTitle = QLabel()
        self.expiryDateTitle.setText("Set Expiry Date:")
        self.expiryDateTitle.setFont(titleFont)
        self.expiryDateTitle.setStyleSheet("QLabel {color: white}")
        self.expiryDateTitle.setFixedSize(150, 30)
        self.layout.addWidget(self.expiryDateTitle)

        self.expiryDateDateEdit = QDateEdit()
        self.expiryDateDateEdit.setCalendarPopup(True)
        self.expiryDateDateEdit.setFont(font)
        self.expiryDateDateEdit.setFixedHeight(80)
        self.expiryDateDateEdit.setDateTime(QDateTime.currentDateTime())
        self.expiryDateDateEdit.setMinimumDate(QDate.currentDate())
        self.expiryDateDateEdit.setStyleSheet("background-color: white; border-radius: 10px;")
        self.layout.addWidget(self.expiryDateDateEdit)

        confirmationButtonLayout = QHBoxLayout()


        cancelButton = QPushButton()
        cancelButton.setText("Cancel")
        cancelButton.setFont(font)
        cancelButton.setFixedSize(150,50)
        cancelButton.clicked.connect(lambda checked: self.expiryDateDialog.close())
        cancelButton.setStyleSheet("""QPushButton {
                                                        background: white;
                                                        border-radius: 10px;
                                                        text-align: center; 

                                                        }
                                                        QPushButton:hover
                                                        {
                                                          background-color: #E8E8E8;
                                                          text-align: center; 
                                                        }""")
        confirmationButtonLayout.addWidget(cancelButton)

        confirmationButton = QPushButton()
        confirmationButton.setText("Confirm")
        confirmationButton.setFont(font)
        confirmationButton.setFixedSize(150, 50)
        confirmationButton.clicked.connect(lambda checked: self.completeButtonConfirmationFunction(self.expiryDateDateEdit.date().toString("yyyy-MM-dd")))
        confirmationButton.setStyleSheet("""QPushButton {
                                            background: white;
                                            border-radius: 10px;
                                            text-align: center; 

                                            }
                                            QPushButton:hover
                                            {
                                              background-color: #E8E8E8;
                                              text-align: center; 
                                            }""")
        confirmationButtonLayout.addWidget(confirmationButton)

        spacer = QWidget()
        spacer.setFixedHeight(100)
        self.layout.addWidget(spacer)

        self.layout.addLayout(confirmationButtonLayout)
        self.expiryDateDialog.setLayout(self.layout)
        self.expiryDateDialog.exec_()

    def completeButtonConfirmationFunction(self, date):
        # marcus you do your thing here
        prescription = Prescription(None,self.appointment.getAppointmentID(),None)
        for i in range(self.rowContainer.layout().count()):
            row = self.rowContainer.layout().itemAt(i).widget()

            medicationName = row.layout().itemAt(0).widget().text()
            dosage = row.layout().itemAt(1).widget().text()
            pillsPerDay = row.layout().itemAt(2).widget().text()
            food = row.layout().itemAt(3).widget().text()

            prescriptionDetails = PrescriptionDetails(medicationName, int(pillsPerDay), food, dosage)
            prescription.setPrescriptionDetails(prescriptionDetails)
         
            print(f"{prescriptionDetails.getMedicationName()} \n {prescriptionDetails.getDosage()}")
        #print(prescription.getExpiryDate())

        prescription.setExpiryDate(date)

        #POSTING
        PrescriptionRepo.PrescriptionRepository.postPrescription(prescription)

        self.expiryDateDialog.close()
        self.frameLayoutManager.back()
        self.frameLayout.widget(self.frameLayoutManager.top()).completePrescription()
        self.frameLayout.setCurrentIndex(self.frameLayoutManager.top())

    def addNewRow(self):

        row = QWidget()
        rowLayout = QHBoxLayout(row)

        prescriptionMedicationName = QLineEdit()
        prescriptionMedicationName.setFixedSize(300, 50)
        prescriptionMedicationName.setPlaceholderText("  Medication Name")
        prescriptionMedicationName.setStyleSheet("""QLineEdit {
                                                    border-radius: 10px;
                                                    border: 1px solid black;
                                                    background: white;
                                                    }""")

        prescriptionDosage = QLineEdit()
        prescriptionDosage.setFixedSize(130, 50)
        prescriptionDosage.setPlaceholderText(" Dosage")
        prescriptionDosage.setStyleSheet("""QLineEdit {
                                            border-radius: 10px;
                                            border: 1px solid black;
                                            background: white;
                                            }""")

        prescriptionPillsPerDay = QLineEdit()
        prescriptionPillsPerDay.setFixedSize(100, 50)
        prescriptionPillsPerDay.setPlaceholderText(" Pills Per Day")
        prescriptionPillsPerDay.setStyleSheet("""QLineEdit {
                                            border-radius: 10px;
                                            border: 1px solid black;
                                            background: white;
                                            }""")

        prescriptionFood = QLineEdit()
        prescriptionFood.setFixedSize(150, 50)
        prescriptionFood.setPlaceholderText(" Before or After eating")
        prescriptionFood.setStyleSheet("""QLineEdit {
                                        border-radius: 10px;
                                        border: 1px solid black;
                                        background: white;
                                        }""")

        removeRowButton = QPushButton()
        removeRowButton.setFixedSize(40,40)
        filepath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "resources\\icons8-remove-50.png")
        removeRowIcon = QIcon(filepath)
        removeRowButton.setIconSize(QSize(40, 40))
        removeRowButton.setIcon(removeRowIcon)
        removeRowButton.setStyleSheet("QPushButton {background: transparent;}")
        removeRowButton.clicked.connect(lambda checked, row=row: self.removeRow(row))

        row.setFixedSize(790,100)
        row.layout().addWidget(prescriptionMedicationName)
        row.layout().addWidget(prescriptionDosage)
        row.layout().addWidget(prescriptionPillsPerDay)
        row.layout().addWidget(prescriptionFood)
        row.layout().addWidget(removeRowButton)

        self.rowContainer.layout().addWidget(row)

    def removeRow(self, row):
        self.rowContainer.layout().removeWidget(row)

        for i in range(row.layout().count()):
            widget = row.layout().itemAt(0).widget()
            row.layout().removeWidget(widget)
            if widget is not None:
                widget.deleteLater()


