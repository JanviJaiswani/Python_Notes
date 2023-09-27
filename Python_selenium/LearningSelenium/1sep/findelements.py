from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time


class FindingElement:
    def find_elements(self):
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')
        driver.maximize_window()
        lista = driver.find_elements("tag name",'a')
        print(len(lista))
        for i in lista:
            print(i.text)
        time.sleep(15)


findingby = FindingElement()
findingby.find_elements()