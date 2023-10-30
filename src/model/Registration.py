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
        
    
    def registerClinic(info):
        response = requests.post(f'http://127.0.0.1:5000/clinics',json=info)
        registerStatus = response.text

        if response.status_code == 201:
            return registerStatus, True
        else:
            return registerStatus, False                    