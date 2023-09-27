import time
from selenium import webdriver
import smtplib
import ssl
from email.message import EmailMessage
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By


# Set your e-commerce product URL and target price threshold
product_url = "https://www.flipkart.com/vivo-v27-pro-5g-magic-blue-256-gb/p/itmb928965669f5c?pid=MOBGN39EBRDT3JUR&lid=LSTMOBGN39EBRDT3JURQHPZJG&marketplace=FLIPKART&q=vivo+v29+pro+2023&store=tyy%2F4io&srno=s_1_1&otracker=AS_Query_OrganicAutoSuggest_1_8_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_1_8_na_na_na&fm=search-autosuggest&iid=2ecdfe6d-279b-47ab-821f-1b06f6a16eea.MOBGN39EBRDT3JUR.SEARCH&ppt=clp&ppn=mobile-phones-store&ssid=emf51ue9ds0000001695113007693&qH=38073b32ce67a5cf"
target_price_threshold = 40000.0  # Set your desired threshold

# Configure the Edge WebDriver (make sure you have the Microsoft Edge WebDriver installed)
driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

# Open the product page
driver.get(product_url)
driver.maximize_window()
time.sleep(3)

# Locate and extract the current product price (modify this according to your website's structure)
price_element = driver.find_element(By.XPATH, "//div[@class='_30jeq3 _16Jk6d']")

# Extract the price text and remove the Indian Rupee symbol and commas
price_text = price_element.text.replace("₹", "").replace(",", "")
print(price_text)

# Convert the cleaned price text to a float
current_price = float(price_text)
print(current_price)
# Check if the current price is below the threshold
if current_price < target_price_threshold:
    print("Done!!")
    # Send an email alert (you need to configure your SMTP server and credentials)
    email_sender = "jaiswanijanvi08@gmail.com"
    email_password = "qbid otsf tojd pumc"
    email_receiver ="2020pceitjanvi22@poornima.org"

    subject = "Price Alert: Product Price Dropped Below Threshold"
    body = f"The product price is now ${current_price:.2f}, which is below your threshold of ${target_price_threshold:.2f}. You can check it here: {product_url}"

    em = EmailMessage()
    em['from']=email_sender
    em['to']=email_receiver
    em['subject']=subject
    em.set_content(body)

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
          smtp.login(email_sender,email_password)
          smtp.sendmail(email_sender,email_receiver,em.as_string())
          print("Email alert sent successfully.")
    except Exception as e:
        print(f"Error sending email: {str(e)}")

# Close the WebDriver
driver.quit()
