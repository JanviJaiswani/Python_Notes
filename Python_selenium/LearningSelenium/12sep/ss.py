from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time


class FindingElement:
    def find_elements(self):
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')
        driver.maximize_window()
        continuedemo = driver.find_element(By.XPATH , "//button[@id='login-continue-btn']")
        continuedemo.screenshot(".//test.png")
        continuedemo.click()
        time.sleep(3)
        driver.get_screenshot_as_file("C:\\Users\\asus\\Desktop\\Celebal\\Python_selenium\\error.jpg")
        driver.save_screenshot(".\\test1.png")
        
findingby = FindingElement()
findingby.find_elements()
        

        