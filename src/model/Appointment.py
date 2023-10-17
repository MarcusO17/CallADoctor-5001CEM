class Appointment:
    def __init__(self,appointmentID, doctorID, patientID, appointmentStatus, startTime, endTime, appointmentDate, visitReason):
        self.appointmentID = appointmentID
        self.doctorID = doctorID
        self.patientID = patientID
        self.appointmentStatus = appointmentStatus
        self.startTime = startTime
        self.endTime = endTime
        self.appointmentDate = appointmentDate
        self.visitReason = visitReason

    def getAppointmentID(self):
        return self.appointmentID

    def setAppointmentID(self, appointmentID):
        self.appointmentID = appointmentID

    def getDoctorID(self):
        return self.doctorID

    def setDoctorID(self, doctorID):
        self.doctorID = doctorID

    def getPatientID(self):
        return self.patientID

    def setPatientID(self, patientID):
        self.patientID = patientID

    def getAppointmentStatus(self):
        return self.appointmentStatus

    def setAppointmentStatus(self, appointmentStatus):
        self.appointmentStatus = appointmentStatus

    def getStartTime(self):
        return self.startTime

    def setStartTime(self, startTime):
        self.startTime = startTime

    def getEndTime(self):
        return self.endTime

    def setEndTime(self, endTime):
        self.endTime = endTime

    def getAppointmentDate(self):
        return self.appointmentDate

    def setAppointmentDate(self, appointmentDate):
        self.appointmentDate = appointmentDate

    def getVisitReason(self):
        return self.visitReason

    def setVisitReason(self, visitReason):
        self.visitReason = visitReason