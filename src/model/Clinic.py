import requests

class Clinic:
    def __init__(self,clinicID, clinicName,clinicContact 
                 ,clinicAddress,approvalStatus,lat,lon):
        self.clinicID = clinicID
        self.clinicName = clinicName
        self.clinicContact = clinicContact
        self.clinicAddress = clinicAddress
        self.approvalStatus = approvalStatus
        self.lat = lat
        self.lon = lon

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
        self.clinicContact  = clinicContact 

    def getClinicAddress(self):
        return self.clinicAddress

    def setClinicAddress(self, clinicAddress):
        self.clinicAddress = clinicAddress

    def getClinicStatus(self):
        return self.approvalStatus

    def setClinicStatus(self, approvalStatus ):
        self.approvalStatus = approvalStatus

    def getClinicLat(self):
        return self.lat

    def setClinicLat(self,lat):
        self.lat = lat
    
    def getClinicLon(self):
        return self.lon

    def setClinicLon(self, lon):
        self.lon = lon

    @classmethod
    def getClinicfromID(self,clinicID):
        try:
            response = requests.get(f'http://127.0.0.1:5000/clinics/{clinicID}')
            clinic = response.json()[0]
        except Exception as e:
            print(e)
            return Clinic("","","","","","","")
        
        if len(clinic) == 0:
            return Clinic("","","","","","","")

        return Clinic(
            clinic['clinicID'],
            clinic['clinicName'],
            clinic['clinicContact'],
            clinic['address'],
            clinic['governmentApproved'],
            clinic['lat'],
            clinic['lon']
        )

    def getCertification(self):
        response =  requests.get(f'http://127.0.0.1:5000/clinics/image/download/{self.clinicID}')
        if response.status_code == 200:
            print('Image Recieved')
            return response.content
        else:
            print(f'Error: {response.status_code}')
            return None
    
    def approve(self):
        response =  requests.patch(f'http://127.0.0.1:5000/clinics/approve/{self.clinicID}')
        if response.status_code == 200:         
            return True
        else:
            return False

    def cancel(self):
        response =  requests.delete(f'http://127.0.0.1:5000/clinics/cancel/{self.clinicID}')
        if response.status_code == 200:         
            return True
        else:
            return False