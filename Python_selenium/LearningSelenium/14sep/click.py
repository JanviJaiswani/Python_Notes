from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time


class FindingElement:
    def find_elements(self):
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        driver.get('https://demo.guru99.com/test/simple_context_menu.html')
        driver.maximize_window()
        # action = ActionChains(driver)
        # right_click = driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']") 
        # action.context_click(right_click).perform()
        # time.sleep(3)
        # driver.find_element(By.XPATH,"//span[normalize-space()='Copy']").click()
        # time.sleep(1)      
        
        
        action1 = ActionChains(driver)
        double_click=driver.find_element(By.XPATH,"//button[normalize-space()='Double-Click Me To See Alert']") 
        action1.double_click(double_click).perform()
        time.sleep(5)
        
        


findingby = FindingElement()
findingby.find_elements()
