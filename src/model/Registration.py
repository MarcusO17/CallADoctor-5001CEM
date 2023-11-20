import requests
import json

class Registration:
    
    baseURL = "http://127.0.0.1:5000/"

    def registerDoctor(info,img):
        response = requests.post(f'http://127.0.0.1:5000/doctors',json=info)
        registerStatus = response.text

        if response.status_code == 201:
            doctorID = response.text.split(' : ')[1]
            responseUpload = requests.post(f'http://127.0.0.1:5000/doctors/image/upload/{doctorID}',files=img)
            print(responseUpload.text)
            return registerStatus, True
        else:
            return registerStatus, False
        
    def registerPatient(info):
        response = requests.post(f'http://127.0.0.1:5000/patients',json=info)
        registerStatus = response.text

        if response.status_code == 201:
            return registerStatus, True
        else:
            return registerStatus, False
        
    
    def registerClinic(info,img):
        response = requests.post(f'http://127.0.0.1:5000/clinics',json=info)
        registerStatus = response.text
       
        if response.status_code == 201:
            clinicID = response.text.split(' : ')[1]
            responseUpload = requests.post(f'http://127.0.0.1:5000/clinics/image/upload/{clinicID}',files=img)
            print(responseUpload.text)
            return registerStatus, True
        else:
            return registerStatus, False                    