from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time


class FindingElement:
    def find_elements(self):
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        driver.get('https://www.w3schools.com/w3css/w3css_input.asp')
        driver.maximize_window()
        print(driver.find_element("id", "male").is_selected())
        print(driver.find_element("id", "female").is_selected())
        driver.find_element("id","female").click()
        time.sleep(2)
        print(driver.find_element("id", "female").is_selected())
        print(driver.find_element("id", "male").is_selected())
        time.sleep(10)


findingby = FindingElement()
findingby.find_elements()