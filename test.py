
import chromedriverLocation
import unittest
from selenium import webdriver
    
class challenge1(unittest.TestCase):

#unittest.TestCase tells it that we run setUp, then every method that starts with "test_", then tearDown

    def setUp(self): 
        self.driver = webdriver.Chrome(chromedriverLocation.mylocation)

    def tearDown(self):
        self.driver.close()

    def test_challenge1(self):
        self.driver.get("https://www.google.com")
        self.assertIn("Google", self.driver.title)

if __name__ == '__main__':
    unittest.main()