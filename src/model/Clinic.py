import requests

class Clinic:
    def __init__(self,clinicID, clinicName, clinicContact, clinicAddress, approvalStatus):
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

    def getClinicDescription(self):
        return self.clinicDescription

    def setClinicDescription(self, clinicDescription):
        self.clinicDescription = clinicDescription

    def getClinicAddress(self):
        return self.clinicAddress

    def setClinicAddress(self, clinicAddress):
        self.clinicAddress = clinicAddress

    @classmethod
    def getClinicfromID(self,clinicID):
        try:
            response = requests.get(f'http://127.0.0.1:5000/clinics/{clinicID}')
            clinic = response.json()[0]
        except Exception as e:
            print(e)
            return Clinic("","","","","")
        
        return Clinic(
            clinic['clinicID'],
            clinic['clinicName'],
            clinic['clinicContact'],
            clinic['clinicAddress'],
            clinic['approvalStatus'],
        )
        