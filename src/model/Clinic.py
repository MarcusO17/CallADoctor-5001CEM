class Clinic:
    def __init__(self,clinicID, clinicName, clinicDescription, clinicAddress):
        self.clinicID = clinicID
        self.clinicName = clinicName
        self.clinicDescription = clinicDescription
        self.clinicAddress = clinicAddress

    def getClinicID(self):
        return self.clinicID

    def setClinicID(self, clinicID):
        self.clinicID = clinicID

    def getClinicName(self):
        return self.clinicName

    def setClinicName(self, clinicName):
        self.clinicName = clinicName

    def getClinicDescription(self):
        return self.clinicDescription

    def setClinicDescription(self, clinicDescription):
        self.clinicDescription = clinicDescription

    def getClinicAddress(self):
        return self.clinicAddress

    def setClinicAddress(self, clinicAddress):
        self.clinicAddress = clinicAddress        