import requests
import json

class Registration:
    
    baseURL = "http://127.0.0.1:5000/"

    def registerDoctor(info):
        response = requests.post(f'http://127.0.0.1:5000/doctors',json=info)
        registerStatus = json.loads(response.text)

        if response.status_code == 201:
            return registerStatus, True
        else:
            return registerStatus, False
                            