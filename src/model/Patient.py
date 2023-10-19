import requests
class Patient:
    def __init__(self, patientID, patientName, patientAddress, patientDOB, patientBlood, patientRace):
        self.patientID = patientID
        self.patientName = patientName
        self.patientAddress = patientAddress
        self.patientDOB = patientDOB
        self.patientBlood = patientBlood
        self.patientRace = patientRace

    def getPatientID(self):
        return self.patientID
    
    def setPatientID(self, patientID):
        self.patientID = patientID

    def getPatientName(self):
        return self.patientName

    def setPatientName(self, patientName):
        self.patientName = patientName

    def getPatientAddress(self):
        return self.patientAddress

    def setPatientAddress(self, patientAddress):
        self.patientAddress = patientAddress

    def getPatientDOB(self):
        return self.getPatientDOB

    def setPatientDOB(self, patientDOB):
        self.patientDOB = patientDOB

    def getPatientBlood(self):
        return self.patientBlood
    
    def setPatientBlood(self, patientBlood):
        self.patientBlood = patientBlood

    def getPatientRace(self):
        return self.patientRace
    
    def setPatientRace(self, patientRace):
        self.patientRace = patientRace

    @classmethod
    def getPatientfromID(self,patientID):
        try:
            response = requests.get(f'http://127.0.0.1:5000/patients/{patientID}')
            patient = response.json()[0]
        except Exception as e:
            print(e)
            return Patient("","","","","","")
        
        return Patient(
            patient['patientID'],
            patient['patientName'],
            patient['address'],
            patient['dateOfBirth'],
            patient['bloodType'],
            patient['race']
        )
        
    