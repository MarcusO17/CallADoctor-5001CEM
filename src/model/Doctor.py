import requests
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

    @classmethod
    def getDoctorfromID(self,doctorID):
        try:
            response = requests.get(f'http://127.0.0.1:5000/doctors/{doctorID}')
            doctor = response.json()[0]
        except Exception as e:
            print(e)
            return Doctor("","","","","","")
        
        return Doctor(
                doctor['doctorName'],
                doctor['doctorType'],
                doctor['doctorICNumber'],
                doctor['doctorContact'],
                doctor['yearOfExperience'],
                doctor['status'],
                doctor['clinicID']
        )
        