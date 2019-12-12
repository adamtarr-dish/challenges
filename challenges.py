import time
import unittest
import chromedriverLocation
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
    
class Challenges(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(chromedriverLocation.mylocation)

    def tearDown(self):
        self.driver.close()
    
    def test_challenge1(self):
        self.driver.get("https://www.google.com")
        self.assertIn("Google", self.driver.title)

    def test_challenge2(self):
        wait = WebDriverWait(self.driver,15)

        self.driver.get("https://www.copart.com/")
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Vehicle Finder")))
        self.driver.find_element(By.LINK_TEXT, "Vehicle Finder").click()
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Exotics")))
        self.driver.find_element(By.LINK_TEXT, "Exotics").click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-resultstable")))
        #self.driver.find_element(By.CSS_SELECTOR, "#serverSideDataTable_filter .form-control").send_keys("lot_make_desc=\"Porsche\"")
        self.driver.find_element(By.XPATH, "//*[@id=\"collapseinside3\"]/form/div/input").send_keys("Porsche")
        time.sleep(5)
        assert self.driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(1) > td:nth-child(5) > span").text == "PORSCHE"
    
    
    def test_challenge3(self):

        wait = WebDriverWait(self.driver,15)
        self.driver.get("https://www.copart.com/")
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Trending")))
        trendingpath = "//*[@id=\"tabTrending\"]/div[@ng-if=\"popularSearches\"]//a"
        elements = self.driver.find_elements(By.XPATH, trendingpath)
        for element in elements:
            print(element.text, " - ", element.get_property("href"))


if __name__ == '__main__':
    unittest.main()

# //*[@id="tabTrending"]/div[1]//a
 
# python3 -m unittest challenges.Challenges.test_challenge3