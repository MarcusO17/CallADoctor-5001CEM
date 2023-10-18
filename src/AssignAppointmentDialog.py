from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton, QScrollArea, QHBoxLayout
from PyQt5.QtCore import Qt


class AssignAppointmentDialog(QDialog):
    def __init__(self, requestList, doctor):
        super(AssignAppointmentDialog, self).__init__()
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowCloseButtonHint)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle("")
        self.setFixedSize(600,600)
        self.layout = QVBoxLayout()
        self.appointmentList = requestList
        self.doctor = doctor

        self.requestButtonLayout = QVBoxLayout()
        self.confirmationButtonLayout = QHBoxLayout()
        boxScrollArea = QScrollArea()
        boxScrollArea.setWidgetResizable(True)

        self.requestButtonList = list()
        self.selectedAppointment = None
        self.selectedButtonIndex = ""

        for count, appointment in enumerate(self.appointmentList):
            print("Creating 1 button here")
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
        #make the changes here
        self.requestList[self.selectedButtonIndex].setDoctorID("")

        self.close()

    def cancelButtonFunction(self):
        self.close()
