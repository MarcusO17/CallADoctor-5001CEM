class Doctor:
    def __init__(self,doctorID, doctorName, clinicID, status):
        self.doctorID = doctorID
        self.doctorName = doctorName
        self.clinicID = clinicID
        self.status = status

    def getDoctorID(self):
        return self.doctorID

    def setDoctorID(self, doctorID):
        self.doctorID = doctorID

    def getDoctorName(self):
        return self.doctorName

    def setDoctorName(self, doctorName):
        self.doctorName = doctorName

    def getClinicID(self):
        return self.clinicID

    def setClinicID(self, clinicID):
        self.clinicID = clinicID

    def getStatus(self):
        return self.status

    def setStatus(self, status):
        self.status = status