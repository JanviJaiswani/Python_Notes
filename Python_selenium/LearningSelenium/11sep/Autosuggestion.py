from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time


class FindingElement:
    def find_elements(self):
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        driver.get('https://www.yatra.com')
        driver.maximize_window()
        depart_Frm = driver.find_element(By.XPATH,"//input[@id='BE_flight_origin_city']")
        time.sleep(3)
        depart_Frm.click()
        time.sleep(3)
        depart_Frm.send_keys("New Delhi")
        time.sleep(3)
        depart_Frm.send_keys(Keys.ENTER)
        time.sleep(3)
        
        going_to = driver.find_element(By.XPATH , "//input[@id='BE_flight_arrival_city']")
        time.sleep(3)
        going_to.send_keys("New")
        time.sleep(3)
        result = driver.find_elements(By.XPATH , "//div[@class='viewport']//div[1]/li")
        print(len(result))
        for i in result:
            if "New York (JFK)" in i.text:
                i.click()
                time.sleep(5)
                break


findingby = FindingElement()
findingby.find_elements()