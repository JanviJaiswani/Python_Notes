from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time


class FindingElement:
    def find_elements(self):
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        driver.get('https://www.yatra.com')
        driver.maximize_window()
        action = ActionChains(driver)
        action.move_to_element(driver.find_element(By.XPATH,"//span[@class='more-arr']")).perform()
        time.sleep(3)
        driver.find_element(By.XPATH,"//span[normalize-space()='Xplore']").click()
        time.sleep(5)      
        


findingby = FindingElement()
findingby.find_elements()
