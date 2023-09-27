from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time


class FindingElement:
    def find_elements(self):
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        driver.get('https://www.w3schools.com/js/tryit.asp?filename=tryjs_confirm')
        driver.maximize_window()
        driver.switch_to.frame("iframeResult")
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(4)
        driver.switch_to.alert.accept()
        time.sleep(2)
        
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(4)
        driver.switch_to.alert.dismiss()
        time.sleep(2)
        
        driver.find_element(By.XPATH, "//button[normalize-space()='Try it']").click()
        time.sleep(4)
        
        # Print the text of the alert
        print(driver.switch_to.alert.text)
        driver.switch_to.alert.send_keys("hurray!!")
        driver.switch_to.alert.accept()
        time.sleep(15)
        
        


findingby = FindingElement()
findingby.find_elements()
