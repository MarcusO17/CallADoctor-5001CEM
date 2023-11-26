import unittest
import requests
from unittest.mock import Mock, patch
from src.model import graphs

class TestGraphs(unittest.TestCase):
    @patch('requests.get')
    def test_generateGraph_success(self, mock_get):
        mockGraphData = [{"dates": "2023-01-01", "count": 10}, 
                         {"dates": "2023-01-02", "count": 15}]
        
        mockResponse = Mock()
        mockResponse.json.return_value = mockGraphData
        mock_get.return_value = mockResponse

        result = graphs.graphGen.generateGraph()

        self.assertIsNotNone(result)  

    @patch('requests.get')
    def test_generateGraph_failure(self, mock_get):
        mockGraphData = []
                    
        mockResponse = Mock()
        mockResponse.json.return_value = mockGraphData
        mock_get.return_value = mockResponse

        result = graphs.graphGen.generateGraph()

        self.assertIsNone(result)  
  
  
if __name__ == '__main__':
    unittest.main()