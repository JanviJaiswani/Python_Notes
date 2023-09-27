
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time


class FindingElementByXpath:
    def locate_by_Xpath(self):
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        driver.get('https://training.openspan.com/login')
        driver.maximize_window()
        state = driver.find_element("xpath","//input[@id='login_button']").is_enabled()
        print(state)
        time.sleep(1000) 


findingbyXpath = FindingElementByXpath()
findingbyXpath.locate_by_Xpath()