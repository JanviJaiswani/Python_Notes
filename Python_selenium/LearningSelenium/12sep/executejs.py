from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time


class FindingElement:
    def find_elements(self):
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        driver.execute_script("window.open('https://www.yatra.com/business', '_self');")
        driver.maximize_window()
        time.sleep(3)
        demo = driver.execute_script("return document.getElementsByTagName('a')[2];")
        driver.execute_script("arguments[0].click();",demo)
        time.sleep(10)

findingby = FindingElement()
findingby.find_elements()