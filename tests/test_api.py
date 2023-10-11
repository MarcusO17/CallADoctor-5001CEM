import requests
import unittest
from unittest.mock import patch,Mock


def get_index():
    response = requests.get('http://127.0.0.1:5000/')
    return response.text

def get_users():
    response = requests.get('http://127.0.0.1:5000/users')
    return response.json

def get_patients():
    response = requests.get('http://127.0.0.1:5000/patients')
    return response.json

def post_patients(data):
    response = requests.post('http://127.0.0.1:5000/patients',json=data)
    return response.text()


class TestCentralAPI(unittest.TestCase):


    @patch('requests.get') #So that the call is MOCKED and not actually run.
    def test_get_index(self, mockGet):
        mockResponse = Mock()

        expectedResponse = 'Welcome to Call a Doctor!'
        mockResponse.text = expectedResponse

        mockGet.return_value = mockResponse

        index = get_index()
        mockGet.assert_called_with('http://127.0.0.1:5000/')
        self.assertEqual(index, expectedResponse)


    @patch('requests.get') #So that the call is MOCKED and not actually run.
    def test_get_patients(self, mockGet):
        mockResponse = Mock()

        responseJSON = {
                "patientID": "12345",
                "patientName": "John Doe",
                "address": "123 Main St",
                "dateOfBirth": "1990-01-15",
                "patientICNumber": "A1234567",
                "bloodType": "O+",
                "race": "Caucasian"
            }
        
        mockResponse.json.return_value = responseJSON
        mockGet.return_value = mockResponse

        patients = get_patients()
        mockGet.assert_called_with('http://127.0.0.1:5000/patients')

        self.assertEqual(patients,responseJSON)

    @patch('requests.get') #So that the call is MOCKED and not actually run.
    def test_get_users(self, mockGet):
        mockResponse = Mock()

        responseJSON = {
                "ID": "P01033",
                "email": "sdh@example.com",
                "password": "Passw0rd",
                "role": "patient"
            }
        
        mockResponse.json = responseJSON
        mockGet.return_value = mockResponse

        users = get_users()
        mockGet.assert_called_with('http://127.0.0.1:5000/users')
        print(users)

        self.assertEqual(users,responseJSON)




if __name__ == "__main__":
  unittest.main()