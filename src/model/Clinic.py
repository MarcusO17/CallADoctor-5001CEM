class Clinic:
    def __init__(self,clinicID, clinicName,clinicContact 
                 ,clinicAddress,approvalStatus):
        self.clinicID = clinicID
        self.clinicName = clinicName
        self.clinicContact = clinicContact
        self.clinicAddress = clinicAddress
        self.approvalStatus = approvalStatus

    def getClinicID(self):
        return self.clinicID

    def setClinicID(self, clinicID):
        self.clinicID = clinicID

    def getClinicName(self):
        return self.clinicName

    def setClinicName(self, clinicName):
        self.clinicName = clinicName

    def getClinicContact (self):
        return self.clinicContact

    def setClinicContact (self, clinicContact ):
        self.cliniContact  = clinicContact 

    def getClinicAddress(self):
        return self.clinicAddress

    def setClinicAddress(self, clinicAddress):
        self.clinicAddress = clinicAddress    

    def getClinicStatus(self):
        return self.approvalStatus

    def setClinicStatus(self, approvalStatus ):
        self.approvalStatus = approvalStatus
