import requests
import json

class Login:
    
    baseURL = "http://127.0.0.1:5000/"

    def userValidLogin(credentials):
        try:
            response = requests.get(f'http://127.0.0.1:5000/users/auth',json=credentials)
            sessionInfo = json.loads(response.text)
        except requests.RequestException as e:
            print(f'Error : {e}')
            return None,False

        if response.status_code == 200:
            return sessionInfo, True
        elif response.status_code == 401:
            return sessionInfo, False
                            
                            
 

            
        
