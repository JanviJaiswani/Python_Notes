from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
import time


class FindingElementByXpath:
    def locate_by_Xpath(self):
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        driver.get('https://yatra.com')
        driver.maximize_window()
        text = driver.find_element("xpath","//span[@class='main-heading']").text
        print(text)
        time.sleep(1000)


findingbyXpath = FindingElementByXpath()
findingbyXpath.locate_by_Xpath()