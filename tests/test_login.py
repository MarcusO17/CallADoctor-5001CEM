import unittest
from unittest.mock import Mock, patch
from src.model.Login import Login
import json

def mockValidSession():
    return {
        "ID": "P00003",
        "role": "patient"
    }


class TestLogin(unittest.TestCase):
    @patch('requests.get')
    def test_userValidLogin(self, mock_get):
        #Mocking the get data for users response
        response_data = {
            "ID": "P00003",
            "role": "patient"
        }
        mock_get.return_value = Mock(status_code=200, text=json.dumps(response_data))

       
        expectedJSON = {
            "ID": "P00003",
            "role": "patient"
        }
        credentials = {
            "email": "test@test.com",
            "password": "1299302"
        }

        
        result, success = Login.userValidLogin(credentials)
        self.assertEqual(result, expectedJSON)
        self.assertTrue(success)