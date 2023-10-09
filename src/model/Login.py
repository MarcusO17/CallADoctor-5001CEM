import requests
import json

class Login:
    
    baseURL = "http://127.0.0.1:5000/"

    def userValidLogin(self,email,password):
        response = requests.get(f'{self.baseURL}users/auth',json={
                                    "email" : email,
                                    "password" : password
                                })
        sessionInfo = json.loads(response.text)

        if response.status_code == 200:
            return sessionInfo, True
        elif response.status_code == 204:
            return sessionInfo, False
                            
                            

    
 

            
        
