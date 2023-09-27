from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time


class FindingElement:
    def find_elements(self):
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        driver.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe_frameborder_css')
        driver.maximize_window()
        # driver.switch_to.frame(driver.find_element(By.XPATH, "//iframe[@id='iframeResult']"))
        driver.switch_to.frame("iframeResult")
        driver.switch_to.frame(0)
        driver.find_element(By.XPATH, "//a[@id='navbtn_exercises']").click()
        time.sleep(10)


findingby = FindingElement()
findingby.find_elements()
