import time
import unittest
import chromedriverLocation
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
    
class Challenge1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(chromedriverLocation.mylocation)

    def tearDown(self):
        self.driver.close()

    def test_challenge1(self):
        wait = WebDriverWait(self.driver,15)

        self.driver.get("https://www.copart.com/")
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Vehicle Finder")))
        self.driver.find_element(By.LINK_TEXT, "Vehicle Finder").click()
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Exotics")))
        self.driver.find_element(By.LINK_TEXT, "Exotics").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-resultstable")))
        self.driver.find_element(By.CSS_SELECTOR, "#serverSideDataTable_filter .form-control").send_keys("lot_make_desc=\"Porsche\"")
        time.sleep(5)
        assert self.driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(1) > td:nth-child(5) > span").text == "PORSCHE"

if __name__ == '__main__':
    unittest.main()