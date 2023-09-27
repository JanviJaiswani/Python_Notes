from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time


class FindingElement:
    def find_elements(self):
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        driver.get('https://www.snapdeal.com/products/mobiles?sort=plrty')
        driver.maximize_window()
        ele1 = driver.find_element(By.XPATH,"//a[contains(@class,'left-handle')]") 
        ele2 = driver.find_element(By.XPATH,"//a[contains(@class,'right-handle')]") 
       # ActionChains(driver).drag_and_drop_by_offset(ele1,60,0).perform()
        ActionChains(driver).click_and_hold(ele1).pause(1).move_by_offset(60,0).release().perform()
        time.sleep(2)
        ActionChains(driver).drag_and_drop_by_offset(ele2,-40,0).perform()
        time.sleep(5)
        
        


findingby = FindingElement()
findingby.find_elements()
