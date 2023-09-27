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
        depart_Frm = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
        time.sleep(1)
        depart_Frm.click()
        time.sleep(1)
        depart_Frm.send_keys("New Delhi")
        time.sleep(1)
        depart_Frm.send_keys(Keys.ENTER)
        time.sleep(1)

        going_to = driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        time.sleep(1)
        going_to.send_keys("New")
        time.sleep(1)
        result = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
        print(len(result))
        for i in result:
            if "New York (JFK)" in i.text:
                i.click()
                time.sleep(5)
                break

        origin = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
        origin.click()
        time.sleep(1)
        dates = driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        for date in dates:
            print(date.get_attribute("data-date"))
            if date.get_attribute("data-date") == '20/09/2023':
                date.click()
                time.sleep(10)
                a = time.asctime()
                print(a)
                break
        time.sleep(10)


findingby = FindingElement()
findingby.find_elements()

