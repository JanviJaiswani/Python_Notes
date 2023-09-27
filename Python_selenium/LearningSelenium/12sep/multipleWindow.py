from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time


class FindingElement:
    def find_elements(self):
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        driver.get('https://www.yatra.com')
        driver.maximize_window()
        parent = driver.current_window_handle
        print(parent)

        driver.find_element(By.XPATH, "//img[@class='conta iner']").click()
        handles = driver.window_handles
        print(handles)

        for handle in handles:
            if handle != parent:
                driver.switch_to.window(handle)
                driver.find_element(By.XPATH, "//a[normalize-space()='Terms and Conditions']").click()
                time.sleep(3)
                driver.close()
                time.sleep(2)
                break

        # After the loop, switch back to the parent window
        driver.switch_to.window(parent)
        driver.find_element(By.XPATH, "//img[@class='conta iner']").click()
        # Continue your code here for the parent window


findingby = FindingElement()
findingby.find_elements()
