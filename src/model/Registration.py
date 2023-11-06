import requests
import json

class Registration:
    
    baseURL = "http://127.0.0.1:5000/"

    def registerDoctor(info):
        response = requests.post(f'http://127.0.0.1:5000/doctors',json=info)
        registerStatus = response.text

        if response.status_code == 201:
            return registerStatus, True
        else:
            return registerStatus, False
        
    def registerPatient(info):
        response = requests.post(f'http://127.0.0.1:5000/patient',json=info)
        registerStatus = response.text

        if response.status_code == 201:
            return registerStatus, True
        else:
            return registerStatus, False
        
    
    def registerClinic(info,img):
        response = requests.post(f'http://127.0.0.1:5000/clinics',json=info)
        responseUpload = requests.post(f'http://127.0.0.1:5000/clinics/image/upload/C005',files=img)
        registerStatus = response.text
        print(responseUpload.text)
        if response.status_code == 201:
            return registerStatus, True
        else:
            return registerStatus, False                    