from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

# class FindingElementByID:
#     def locate_by_id(self):
#        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
#         driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')
#         driver.find_element("id","login-input").send_keys('test@test.com')
#         time.sleep(1000)
#         driver.quit()


# findingbyID = FindingElementByID()
# findingbyID.locate_by_id()



class FindingElementByXpath:
    def locate_by_Xpath(self):
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')
        driver.find_element("xpath","//input[@id='login-input']").send_keys('test@test.com')
        time.sleep(1000)
        driver.quit()


findingbyXpath = FindingElementByXpath()
findingbyXpath.locate_by_Xpath()
