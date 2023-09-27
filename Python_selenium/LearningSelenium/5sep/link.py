from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time


class FindingElementByXpath:
    def locate_by_Xpath(self):
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        driver.get('https://www.yatra.com/')
        driver.maximize_window()
        driver.find_element("link text","Yatra for Business").click()
        time.sleep(1000) 


findingbyXpath = FindingElementByXpath()
findingbyXpath.locate_by_Xpath()