import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import time

@pytest.fixture(scope="class")
def setup(request):
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        wait = WebDriverWait(driver,10)
        driver.get('https://www.yatra.com')
        driver.maximize_window()
        request.cls.driver = driver
        request.cls.wait = wait
        yield
        driver.close()