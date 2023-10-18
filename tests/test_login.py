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
    def test_userValidLogin_success(self, mock_get):
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

        
        result, status = Login.userValidLogin(credentials)
        self.assertDictEqual(result, expectedJSON)
        self.assertTrue(status)
    
    @patch('requests.get')
    def test_userValidLogin_failure(self, mock_get):
        response_data = {
            "ID": "DENIED",
            "role": "DENIED"
        }
        mock_get.return_value = Mock(status_code=401, text=json.dumps(response_data))

        expectedJSON = {
            "ID": "DENIED",
            "role": "DENIED"
        }
        credentials = {
            "email": "test@test.com",
            "password": "1299302"
        }

        
        result, status = Login.userValidLogin(credentials)
        self.assertDictEqual(result, expectedJSON)
        self.assertFalse(status)