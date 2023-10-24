import unittest
import requests
from unittest.mock import Mock, patch
from src.model import Clinic, ClinicRepo


class TestClinic(unittest.TestCase):
    """Class to test Clinic and Clinic Repo Models.
    """

    @patch('requests.get')
    def test_getClinicfromID_success(self, mockGet):
        # Create a mock response
        mockClinicData = {
            "clinicID": 134,
            "clinicName": "Test Clinic",
            "clinicContact": "Contact Info",
            "address": "10-29B Main St",
            "governmentApproved": True,
        }
        mockResponse = Mock()
        mockResponse.json.return_value = [mockClinicData]
        mockGet.return_value = mockResponse


        # Call the function with a clinic ID
        result = Clinic.getClinicfromID(134)

        # Assert that the function returned the expected Clinic object
        self.assertEqual(result.getClinicID(), mockClinicData["clinicID"])
        self.assertEqual(result.getClinicName(),  mockClinicData["clinicName"])
        self.assertEqual(result.getClinicContact(),  mockClinicData["clinicContact"])
        self.assertEqual(result.getClinicAddress(),  mockClinicData["address"])
        self.assertEqual(result.getClinicStatus(),  mockClinicData["governmentApproved"])


    @patch('requests.get')
    def test_getClinicfromID_failed(self, mockGet):
        # Creating Mock Response Failure
        mockClinicData = {}
        mockResponse = Mock()
        mockResponse.json.return_value = [mockClinicData]
        mockGet.return_value = mockResponse

        # Call the function with a clinic ID
        result = Clinic.getClinicfromID(134)

        # Assert that the function returned the expected Clinic object
        self.assertEqual(result.getClinicID(),"")
        self.assertEqual(result.getClinicName(),  "")
        self.assertEqual(result.getClinicContact(),  "")
        self.assertEqual(result.getClinicAddress(),  "")
        self.assertEqual(result.getClinicStatus(),  "")

    @patch('requests.get')
    def test_getClinicList_success(self, mockGet):
        # Creating Mock Response Failure
        mockClinicListData = [{
                "clinicID": 1,
                "clinicName": "Clinic 1",
                "clinicContact": "124215",
                "address": "123 Main St",
                "governmentApproved": True,
            },
            {
                "clinicID": 2,
                "clinicName": "Clinic 2",
                "clinicContact": "2222222",
                "address": "456 Elm St",
                "governmentApproved": False,
            }]
        
        mockResponse = Mock()
        mockResponse.json.return_value = mockClinicListData
        mockGet.return_value = mockResponse

        resultList = ClinicRepo.ClinicRepository.getClinicList()

        #Test Length 
        self.assertEqual(len(resultList),len(mockClinicListData))


        for i in range(len(resultList)):
            self.assertEqual(resultList[i].getClinicID(), mockClinicListData[i]["clinicID"])
            self.assertEqual(resultList[i].getClinicName(), mockClinicListData[i]["clinicName"])
            self.assertEqual(resultList[i].getClinicContact(), mockClinicListData[i]["clinicContact"])
            self.assertEqual(resultList[i].getClinicAddress(), mockClinicListData[i]["address"])
            self.assertEqual(resultList[i].getClinicStatus(), mockClinicListData[i]["governmentApproved"])

    @patch('requests.get')
    def test_getClinicList_failed(self, mockGet):
        # Creating Mock Response Failure
        mockGet.side_effect = requests.RequestException('Connection Error')

        resultList = ClinicRepo.ClinicRepository.getClinicList()

        #Test Length 
        self.assertEqual(len(resultList),0)
        self.assertEqual(resultList,[])




if __name__=="__main__":
    unittest.main()