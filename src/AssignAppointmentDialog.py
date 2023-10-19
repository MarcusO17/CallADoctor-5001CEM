from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton, QScrollArea, QHBoxLayout
from PyQt5.QtCore import Qt

from model import Appointment


class AssignAppointmentDialog(QDialog):
    def __init__(self, parent=None):
        super(AssignAppointmentDialog, self).__init__(parent)
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)  # Remove close button
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle("Assign An Appointment")
        self.doctor = None
        print(self.doctor)

        self.setFixedSize(600, 600)
        self.layout = QVBoxLayout()
        appointment1 = Appointment("appointment1", "", "patient1", "approved", 12, 13, "19-10-2023",
                                   "light fever")
        self.unassignedAppointmentList = list()

        self.unassignedAppointmentList.append(appointment1)

        self.requestButtonLayout = QVBoxLayout()
        self.confirmationButtonLayout = QHBoxLayout()
        boxScrollArea = QScrollArea()
        boxScrollArea.setWidgetResizable(True)

        self.requestButtonList = list()
        self.selectedAppointment = None
        self.selectedButtonIndex = ""

        for count, appointment in enumerate(self.unassignedAppointmentList):
            button = QPushButton()
            button.clicked.connect(lambda checked, index=count: self.buttonClicked(index))
            button.setCheckable(True)
            button.setText(appointment.getAppointmentID())
            self.requestButtonList.append(button)
            self.requestButtonLayout.addWidget(button)

        boxScrollArea.setLayout(self.requestButtonLayout)
        boxScrollArea.setFixedSize(600, 500)

        self.confirmButton = QPushButton()
        self.confirmButton.setText("Confirm")
        self.confirmButton.clicked.connect(self.confirmButtonFunction)

        self.cancelButton = QPushButton()
        self.cancelButton.setText("Cancel")
        self.cancelButton.clicked.connect(self.cancelButtonFunction)

        self.confirmationButtonLayout.addWidget(self.cancelButton)
        self.confirmationButtonLayout.addWidget(self.confirmButton)

        self.layout.addWidget(boxScrollArea)
        self.layout.addLayout(self.confirmationButtonLayout)

        self.setLayout(self.layout)

        print("Finished creating assignAppointmentDialog")

    def buttonClicked(self, index):
        # logic so the user can only select one of the request
        if self.selectedAppointment == None:
            self.selectedButtonIndex = index
            self.selectedAppointment = self.sender()
            self.selectedAppointment.setChecked(True)
            self.selectedAppointment.setStyleSheet("border: 1px solid red;")
        elif self.selectedAppointment == self.sender():
            pass
        else:
            # return the previous selected to its default style
            self.selectedButtonIndex = index
            self.selectedAppointment.setStyleSheet("")
            self.selectedAppointment.setChecked(False)
            # setting new selected
            self.selectedAppointment = self.sender()
            self.selectedAppointment.setStyleSheet("border: 1px solid red;")
            self.selectedAppointment.setChecked(True)

    def confirmButtonFunction(self):
        # make the changes here
        self.close()

    def cancelButtonFunction(self):
        self.close()

    def setDoctor(self, doctor):
        self.doctor = doctor

        print(doctor)