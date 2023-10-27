import requests
from .Patient import Patient
class Doctor:
    def __init__(self,doctorID, doctorName, clinicID, status, doctorType, doctorContact, doctorICNumber, yearsOfExperience):
        self.doctorID = doctorID
        self.doctorName = doctorName
        self.clinicID = clinicID
        self.status = status
        self.doctorType = doctorType
        self.doctorContact = doctorContact
        self.doctorICNumber = doctorICNumber
        self.yearsOfExperience = yearsOfExperience

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

    def getDoctorType(self):
        return self.doctorType

    def setDoctorType(self, doctorType):
        self.doctorType = doctorType

    def getDoctorICNumber(self):
        return self.doctorICNumber
   
    def setDoctorICNumber(self, doctorICNumber):
        self.doctorICNumber = doctorICNumber
  
    def getDoctorContact(self):
        return self.doctorContact

    def setDoctorContact(self, doctorContact):
        self.doctorContact = doctorContact

    def getYearsOfExperience(self):
        return self.yearsOfExperience
    
    def setYearsOfExperience(self, yearsOfExperience):
        self.yearsOfExperience = yearsOfExperience
    

    @classmethod
    def getDoctorfromID(self,doctorID):
        try:
            response = requests.get(f'http://127.0.0.1:5000/doctors/{doctorID}')
            doctor = response.json()[0]
        except Exception as e:
            print(e)
            return Doctor("","","","","","","")
        
        return Doctor(
                doctor['doctorID'],
                doctor['doctorName'],
                doctor['clinicID'],
                doctor['status'],
                doctor['doctorType'],
                doctor['doctorContact'],
                doctor['doctorICNumber'],    
                doctor['yearOfExperience'] 
        )
        
    @classmethod
    def getDoctorPastPatients(self,doctorID):
        patientList = []
        try:
            response = requests.get(f'http://127.0.0.1:5000/doctors/pastpatients/{doctorID}')
            recordsList = response.json()
        except requests.RequestException as e:
                print(f'Error : {e}')
                return []
        
        for records in recordsList:
                tempPatient = Patient("","","","","","",)

                tempPatient.setPatientID(records['patientID'])
                tempPatient.setPatientName(records['patientName'])
                tempPatient.setPatientAddress(records['address'])
                tempPatient.setPatientDOB(records['dateOfBirth'])
                tempPatient.setPatientBlood(records['bloodType'])
                tempPatient.setPatientRace(records['race'])

                patientList.append(tempPatient)
                
        return patientList   