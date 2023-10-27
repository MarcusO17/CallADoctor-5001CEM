import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QGridLayout
from src.AccountPage import AccountPage
from src.DoctorAppointmentDetails import DoctorAppointmentDetails
from src.PageManager import PageManager
from src.model import Doctor
from src.model.AppointmentRepo import AppointmentRepository


class DoctorDashboard(QWidget):
    def __init__(self, doctor):
        super().__init__()
        self.doctor = doctor
        self.pageManager = PageManager()
        self.setupUi()

    def setupUi(self):
        mainLayout = QVBoxLayout(self)
        scheduleLayout = QGridLayout()
        mainLayout.addLayout(scheduleLayout)
        mainLayout.addStretch(1)  # Add stretch to push the schedule to the top

        HEIGHT = 7
        WIDTH = 8

        self.timeSlotButtonList = [[QPushButton() for _ in range(WIDTH)] for _ in range(HEIGHT)]

        # header of the grid
        timeStart = 8
        for i in range(WIDTH):
            timeSlotLabel = QLabel(f"{timeStart:02d}:00")
            scheduleLayout.addWidget(timeSlotLabel, 0, i)
            timeStart += 1

        daysOfTheWeek = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        for i in range(HEIGHT):
            dayCell = QLabel(daysOfTheWeek[i])
            scheduleLayout.addWidget(dayCell, i + 1, 0)

        appointmentList = AppointmentRepository.getAppointmentsWeekly(self.doctor.getDoctorID())
        self.setSchedule(appointmentList, scheduleLayout)

    def setSchedule(self, appointmentList, scheduleLayout):
        for appointment in appointmentList:
            date = appointment.getAppointmentDate()
            start_time = appointment.getStartTime()
            end_time = appointment.getEndTime()

            row = date.weekday() + 1
            start_hour = int(start_time.split(":")[0])
            end_hour = int(end_time.split(":")[0])

            if end_hour - start_hour >= 1:
                for hour in range(start_hour, end_hour):
                    button = self.timeSlotButtonList[row][hour - 7]
                    button.setText("Appointment")
                    button.setStyleSheet("background-color: green;")
                    button.setEnabled(True)
                    button.clicked.connect(
                        lambda checked, appointment=appointment: self.gotoAppointment(appointment, self.doctor))

    def gotoAppointment(self, appointment, doctor):
        self.doctorAppointmentDetails = DoctorAppointmentDetails(appointment, doctor)
        self.doctorAppointmentDetails.setMode(appointment.getAppointmentStatus())
        self.pageManager.add(self.doctorAppointmentDetails)


def main():
    app = QApplication(sys.argv)
    doctor = Doctor("D0001", "doctor name", "C0001", "status", "doctortype", "doctorContact", "ICNUmber", 5)
    doctor_dashboard = DoctorDashboard(doctor)
    doctor_dashboard.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
