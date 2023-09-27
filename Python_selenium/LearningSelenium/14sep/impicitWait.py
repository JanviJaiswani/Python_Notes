from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time


class FindingElement:
    def find_elements(self):
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        driver.get('https://login.salesforce.com/')
        driver.maximize_window()
        driver.implicitly_wait(10)
        driver.find_element(By.ID,"username").send_keys("janvi")
        driver.find_element(By.ID,"pasfrr").send_keys("12233")
        
        
        
        


findingby = FindingElement()
findingby.find_elements()
