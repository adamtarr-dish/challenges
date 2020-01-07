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
        self.driver.find_element(By.XPATH, "//*[@id=\"collapseinside3\"]/form/div/input").send_keys("Porsche")
        time.sleep(5)
        assert self.driver.find_element(By.CSS_SELECTOR, ".odd:nth-child(1) > td:nth-child(5) > span").text == "PORSCHE"
    
    
    def test_challenge3(self):

        wait = WebDriverWait(self.driver,15)
        self.driver.get("https://www.copart.com/")
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Trending")))
        trendingpath = "//*[@id=\"tabTrending\"]/div[@ng-if=\"popularSearches\"]//a"
        # //*[@id="tabTrending"]/div[1]//a also works but the above is more robust
        elements = self.driver.find_elements(By.XPATH, trendingpath)
        for element in elements:
            print(element.text, " - ", element.get_property("href"))
    
    def test_challenge4(self):

        wait = WebDriverWait(self.driver,15)
        self.driver.get("https://www.copart.com/")
        self.driver.maximize_window

        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Trending")))
        trendingpath = "//*[@id=\"tabTrending\"]/div[@ng-if=\"popularSearches\"]//a"
        # //*[@id="tabTrending"]/div[1]//a also works but the above is more robust
        elements = self.driver.find_elements(By.XPATH, trendingpath)
        for element in elements:
            print(element.text, " - ", element.get_property("href"))


    def test_challenge5(self):

        wait = WebDriverWait(self.driver,15)
        self.driver.get("https://www.copart.com/")
        self.driver.maximize_window
        wait.until(EC.presence_of_element_located((By.ID, "input-search")))
        
        self.driver.find_element(By.ID, "input-search").send_keys("porsche")
        self.driver.find_element(By.XPATH, "//*[@data-uname=\"homepageHeadersearchsubmit\"]").click()
        
        wait.until(EC.presence_of_element_located((By.NAME, "serverSideDataTable_length")))

        dropdown = self.driver.find_element(By.NAME, "serverSideDataTable_length")
        dropdown.click()
        dropdown.find_element(By.XPATH, "//option[. = '100']").click()

        wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"serverSideDataTable_processing\"][contains(@style, 'display: none')]")))
        modelList = self.driver.find_elements(By.XPATH,"//span[@data-uname=\"lotsearchLotmodel\"]")
        damageList = self.driver.find_elements(By.XPATH,"//span[@data-uname=\"lotsearchLotdamagedescription\"]")

        models = {}
        for model in modelList:
            modelName = model.get_property("innerHTML")
            if modelName in models:
                models[modelName] += 1
            else:
                if not "[[" in modelName: #the junk entry at the bottom of the table
                    models[modelName] = 1
        for x, y in models.items():
            print(y, " ", x)
        
        damages = {"REAR END":0,"FRONT END":0,"MINOR DENT/SCRATCHES":0,"UNDERCARRIAGE":0,"MISC":0}
        for damage in damageList:
            damageName = damage.text
            if damageName in damages:
                damages[damageName] += 1
            else:
                if not "[[" in damageName:
                    damages["MISC"] += 1
        for x, y in damages.items():
            print(y, " ", x)


        


if __name__ == '__main__':
    unittest.main()
 
# python3 -m unittest challenges.Challenges.test_challenge5 (or whatever challenge you want)