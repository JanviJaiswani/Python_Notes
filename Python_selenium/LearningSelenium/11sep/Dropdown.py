from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select 
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time


class FindingElement:
    def find_elements(self):
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        driver.get('https://www.salesforce.com/au/form/signup/freetrial-sales/?d=topnav2-btn-ft')
        driver.maximize_window()
        dropdown = driver.find_element(By.NAME, "UserTitle")
        dd = Select(dropdown)
        dd.select_by_index(5)
        time.sleep(3)
        dd.select_by_value("Sales_Manager_ANZ")
        time.sleep(3)
        dd.select_by_visible_text("Customer Service Manager")
        time.sleep(10)


findingby = FindingElement()
findingby.find_elements()