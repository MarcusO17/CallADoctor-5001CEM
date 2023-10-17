import requests
import pytest

@pytest.fixture
def mockPatients():
    return {
                "patientID": "12345",
                "patientName": "John Doe",
                "address": "123 Main St, City, Country",
                "dateOfBirth": "1990-05-15",
                "bloodType": "A+",
                "race": "Caucasian"
            }

def test_getPatients(mocker,mockPatients):
    mocker.patch(
        'requests.get("http://127.0.0.1:5000/patients")'
        mockValue = mockPatients
    )expected = (
     response = requests.get("http://127.0.0.1:5000/patients")
    )
    ss


if __name__ == '__main__':
    unittest.main()