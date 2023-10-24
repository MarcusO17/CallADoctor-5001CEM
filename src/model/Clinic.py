import requests

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

    @classmethod
    def getClinicfromID(self,clinicID):
        try:
            response = requests.get(f'http://127.0.0.1:5000/clinics/{clinicID}')
            clinic = response.json()[0]
        except Exception as e:
            print(e)
            return Clinic("","","","","")
        
        if len(clinic) == 0:
            return Clinic("","","","","")
        
        return Clinic(
            clinic['clinicID'],
            clinic['clinicName'],
            clinic['clinicContact'],
            clinic['address'],
            clinic['governmentApproved'],
        )
