from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time


class FindingElement:
    def find_elements(self):
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        driver.get('https://jqueryui.com/droppable/')
        driver.maximize_window()
        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='demo-frame']"))
        ele1 = driver.find_element(By.ID,"draggable") 
        ele2 = driver.find_element(By.ID,"droppable") 
        #ActionChains(driver).drag_and_drop(ele1,ele2).perform()
        ActionChains(driver).drag_and_drop_by_offset(ele1,100,100).perform()
        
        time.sleep(3)
       
        
        


findingby = FindingElement()
findingby.find_elements()
