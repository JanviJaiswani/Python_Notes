from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time


class FindingElementBySelector:
    def locate_by_selector(self):
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        driver.get('https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp')
        attribute_Value = driver.find_element("xpath","//button[normalize-space()='Toggle Hide and Show']").is_displayed()
        print(attribute_Value)
        time.sleep(10)
        


findingbyselector = FindingElementBySelector()
findingbyselector.locate_by_selector()

