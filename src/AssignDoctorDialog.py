import os

from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton, QScrollArea, QHBoxLayout, QWidget, QSizePolicy, QLabel
from PyQt5.QtCore import Qt, QSize

from .model import Doctor
from .model.DoctorRepo import DoctorRepository


class AssignDoctorDialog(QDialog):
    def __init__(self, parent=None):
        super(AssignDoctorDialog, self).__init__(parent)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)  # Remove close button
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle("Assign An Appointment")
        self.setStyleSheet("""QDialog {border-radius: 5px;
                                        background-color: #A08BDD;}""")
        self.request = None

        self.setFixedSize(600, 600)
        self.layout = QVBoxLayout()

        self.doctorList = list()

        self.doctorButtonLayout = QWidget()
        self.doctorButtonLayout.setFixedSize(550, 460)
        self.doctorButtonLayout.setObjectName("buttonContainer")
        self.doctorButtonLayout.setStyleSheet("""QWidget#buttonContainer {
                                                    background: #D0BFFF;
                                                    border-radius: 10px;
                                                    }""")
        button_layout = QVBoxLayout(self.doctorButtonLayout)

        self.confirmationButtonLayout = QHBoxLayout()
        boxScrollArea = QScrollArea()
        boxScrollArea.setObjectName("scrollArea")
        boxScrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        boxScrollArea.setWidgetResizable(True)
        boxScrollArea.setStyleSheet("""QScrollArea#scrollArea {
                                            background: #D0BFFF;
                                            border-radius: 10px;
                                            }""")

        self.doctorButtonList = list()
        self.selectedDoctor = None
        self.selectedButtonIndex = 0

        boxScrollArea.setWidget(self.doctorButtonLayout)
        boxScrollArea.setFixedSize(580, 480)

        buttonFont = QFont()
        buttonFont.setFamily("Montserrat")
        buttonFont.setPointSize(10)

        self.confirmButton = QPushButton()
        self.confirmButton.setText("Confirm")
        self.confirmButton.setFixedSize(250, 50)
        self.confirmButton.setFont(buttonFont)
        self.confirmButton.clicked.connect(self.confirmButtonFunction)
        self.confirmButton.setStyleSheet("""QPushButton {
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

        self.cancelButton = QPushButton()
        self.cancelButton.setText("Cancel")
        self.cancelButton.setFont(buttonFont)
        self.cancelButton.setFixedSize(250, 50)
        self.cancelButton.clicked.connect(self.cancelButtonFunction)
        self.cancelButton.setStyleSheet("""QPushButton {
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

        self.confirmationButtonLayout.addWidget(self.cancelButton)
        self.confirmationButtonLayout.addWidget(self.confirmButton)

        self.title = QLabel()
        self.title.setFont(buttonFont)
        self.title.setText("  Select a Doctor to Assign: ")
        self.title.setStyleSheet("""QLabel {
                                    background: #D0BFFF;
                                    border-radius: 5px;
                                    }""")

        self.layout.addWidget(self.title)
        self.layout.addWidget(boxScrollArea)
        self.layout.addLayout(self.confirmationButtonLayout)

        self.setLayout(self.layout)

        print("Finished creating assign doctor dialog")

    def buttonClicked(self, index):
        # logic so the user can only select one of the request
        if self.selectedDoctor == None:
            self.selectedButtonIndex = index
            self.selectedDoctor = self.sender()
            self.selectedDoctor.setChecked(True)
            self.selectedDoctor.setStyleSheet("""QPushButton {
                                                background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                                        stop: 0 rgba(10, 2, 85, 255), 
                                                                        stop: 1 rgba(59, 41, 168, 255));
                                                border-radius: 10px; color: white;
                                                text-align: left; 
                                                padding-left: 20px;
                                                border: 5px solid white;
                                                }
                                                QPushButton:hover
                                                {
                                                  background-color: #7752FE;
                                                  border: 5px solid white;
                                                  text-align: left; 
                                                  padding-left: 20px;""")
        elif self.selectedDoctor == self.sender():
            pass
        else:
            # return the previous selected to its default style
            self.selectedButtonIndex = index
            self.selectedDoctor.setChecked(False)
            # setting new selected
            self.selectedDoctor.setStyleSheet("""QPushButton {
                                    background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                            stop: 0 rgba(10, 2, 85, 255), 
                                                            stop: 1 rgba(59, 41, 168, 255));
                                    border-radius: 10px; color: white;
                                    text-align: left; 
                                    padding-left: 20px;
                                    border: none;
                                    }
                                    QPushButton:hover
                                    {
                                      background-color: #7752FE;
                                      text-align: left; 
                                      padding-left: 20px;
                                      border: none;
                                    }""")
            self.selectedDoctor = self.sender()
            self.selectedDoctor.setChecked(True)
            self.selectedDoctor.setStyleSheet("""QPushButton {
                                                background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                                        stop: 0 rgba(10, 2, 85, 255), 
                                                                        stop: 1 rgba(59, 41, 168, 255));
                                                border-radius: 10px; color: white;
                                                text-align: left; 
                                                padding-left: 20px;
                                                border: 5px solid white;
                                                }
                                                QPushButton:hover
                                                {
                                                  background-color: #7752FE;
                                                  border: 5px solid white;
                                                  text-align: left; 
                                                  padding-left: 20px;""")

    def confirmButtonFunction(self):
        # make the changes here
        self.request.setDoctorID(self.doctorList[self.selectedButtonIndex].getDoctorID())
        self.close()

    def cancelButtonFunction(self):
        print("CANCEL BUTTON TRIGGERED")
        self.close()

    def setData(self, request):
        CURRENT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
        self.request = request
        self.doctorList = DoctorRepository.getAvailableDoctorList(DoctorRepository,request.getAppointmentID(),request.getClinicID())

        buttonFont = QFont()
        buttonFont.setFamily("Montserrat")
        buttonFont.setPointSize(14)

        filepath = os.path.join(CURRENT_DIRECTORY, "resources\\icons8-doctor-64.png")
        doctorIcon = QIcon(filepath)

        for count, doctor in enumerate(self.doctorList):
            button = QPushButton()
            button.clicked.connect(lambda checked, index=count: self.buttonClicked(index))
            button.setCheckable(True)
            button.setText(f"   {doctor.getDoctorName()}")
            button.setFont(buttonFont)
            button.setIconSize(QSize(80, 80))
            button.setIcon(doctorIcon)
            button.setFixedSize(500, 100)
            button.setStyleSheet("""QPushButton {
                                    background: qlineargradient(spread: pad, x1: 0, y1: 0, x2: 0, y2: 1, 
                                                            stop: 0 rgba(10, 2, 85, 255), 
                                                            stop: 1 rgba(59, 41, 168, 255));
                                    border-radius: 10px; color: white;
                                    text-align: left; 
                                    padding-left: 20px;
                                    }
                                    QPushButton:hover
                                    {
                                      background-color: #7752FE;
                                      text-align: left; 
                                      padding-left: 20px;
                                    }""")
            self.doctorButtonList.append(button)
            self.doctorButtonLayout.layout().addWidget(button)

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.doctorButtonLayout.layout().addWidget(spacer)
