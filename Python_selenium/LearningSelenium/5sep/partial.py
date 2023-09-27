from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

class FindingElementByPartialLinkText:
    def locate_by_PartialLinkText(self):
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        driver.get('https://www.yatra.com/')
        driver.find_element("partial link text", "Holid").click()
        time.sleep(1000) 
        
        
    

findingbyPartialLinkText = FindingElementByPartialLinkText()
findingbyPartialLinkText.locate_by_PartialLinkText()