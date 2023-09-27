from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time


class FindingElementBySelector:
    def locate_by_selector(self):
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')
        driver.find_element("css selector", "#login-input").send_keys('test@test.com')
        time.sleep(10)
        


findingbyselector = FindingElementBySelector()
findingbyselector.locate_by_selector()

