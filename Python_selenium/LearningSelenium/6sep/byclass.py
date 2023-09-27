from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
import time


class FindingElementByXpath:
    def locate_by_Xpath(self):
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')
        driver.maximize_window()
        driver.find_element(By.CLASS_NAME,'email-login-box').send_keys("mat@gmail.com")
        time.sleep(1000)


findingbyXpath = FindingElementByXpath()
findingbyXpath.locate_by_Xpath()