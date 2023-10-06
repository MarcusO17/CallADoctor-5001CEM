import requests
import json

class Login:

    baseURL = "http://127.0.0.1:5000/"

    def userValidLogin(self,email,password):
        response = requests.get(f'{self.baseURL}users/auth')
        users = json.loads(response.text)
        if response.status_code == 200:
            for user in users:
                if email == user['email'] and password == user['password']:
                    return True
                else:
                    continue
        return False
    

    
 

            
        
