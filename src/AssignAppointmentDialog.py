from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton, QScrollArea, QHBoxLayout


class AssignAppointmentDialog(QDialog):
    def __init__(self, requestList, doctor):
        super().__init__()
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

        self.cancelButton = QPushButton()
        self.cancelButton.setText("Confirm")

        self.confirmationButtonLayout.addWidget(self.confirmButton)
        self.confirmationButtonLayout.addWidget(self.cancelButton)

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
        self.requestList[self.selectedButtonIndex].setDoctorID("")

    def cancelButtonFunction(self):
        self.close()
