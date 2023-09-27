from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time


class FindingElementBySelector:
    def locate_by_selector(self):
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')
        attribute_Value = driver.find_element("xpath","//input[@id='login-input']").get_attribute("title")
        print(attribute_Value)
        time.sleep(10)
        


findingbyselector = FindingElementBySelector()
findingbyselector.locate_by_selector()

