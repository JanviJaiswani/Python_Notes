import time
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.common.keys import Keys
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# Input location from the user
location = input("Enter the desired location for weather forecast: ")

# Set up the Edge WebDriver
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

# Open the weather website based on the specified location
weather_url = f"https://www.accuweather.com/"
driver.get(weather_url)
driver.maximize_window()

# Wait for the weather information to load (customize the wait time as needed)
time.sleep(5)  # Adjust the sleep duration as needed to allow the page to load


# Wait for the search input field to be clickable
wait = WebDriverWait(driver, 10)
input_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='searchbar-content']")))
input_element.click()

# Send the location keys to the input element
input_element.send_keys(location)
time.sleep(1)

# Send arrow down key to select the first suggestion
input_element.send_keys(Keys.ARROW_DOWN)

# Send Enter key to confirm the selection
input_element.send_keys(Keys.ENTER)
time.sleep(3)

# Scrape the temperature and weather condition from the webpage
try:
    temperature_element = driver.find_element(By.CSS_SELECTOR, "div[class='cur-con-weather-card__panel'] div[class='temp']")
    weather_condition_element = driver.find_element(By.CSS_SELECTOR, "span[class='phrase']")

    temperature = temperature_element.text
    weather_condition = weather_condition_element.text
except NoSuchElementException:
    # Handle the case where the elements are not found
    temperature = "N/A"
    weather_condition = "N/A"

# Close the WebDriver
driver.quit()

# Define the Excel file name
excel_file_name = "C:\\Users\\asus\\Desktop\\weather_forecast.xlsx"


# Open an existing Excel spreadsheet or create a new one
try:
    workbook = openpyxl.load_workbook(excel_file_name)
    sheet = workbook.active
except FileNotFoundError:
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.append(["Location", "Temperature (°C)", "Weather Condition"])

# Write the location, temperature, and weather condition data into the spreadsheet
sheet.append([location, temperature, weather_condition])

# Save the Excel file
workbook.save(excel_file_name)

# Close the Excel file
workbook.close()

print("Weather forecast data has been saved to the Excel file.")
