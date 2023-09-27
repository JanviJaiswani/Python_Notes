from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

class FindingElementByID:
    def locate_by_id(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get('https://secure.yatra.com/social/common/yatra/signin.htm')
        driver.find_element("id","login-input").send_keys('test@test.com')
        time.sleep(1000)
        driver.quit()


findingbyID = FindingElementByID()
findingbyID.locate_by_id()
