import unittest
from ResultData import ResultData


class TestTestData(unittest.TestCase):

    def setUp(self):
        self.data = ResultData()

    def test_get_data(self):
        allData = self.data.getTestData()
        self.assertTrue(len(allData) >= 0)

    def test_add_data(self):
        self.data.addResults(['Target1', 'Target2'], ['Result1', 'Result2'], ['Text1', 'Text2'], [0, 1])
        # Successful entry addition if no errors.

    def test_get_results(self):
        results = self.data.getResults()
        self.assertTrue(len(results) >= 0)