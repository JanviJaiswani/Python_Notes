from email.message import EmailMessage
import smtplib
import ssl

email_sender = "jaiswanijanvi08@gmail.com"
email_password = "bosvxcjolrpmqvvy"
email_receiver ="2020pceitjanvi22@poornima.org"

subject ="Implementing email using python"
body = """
hey! mail sent Successfully.
"""

em = EmailMessage()
em['from']=email_sender
em['to']=email_receiver
em['subject']=subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(email_sender,email_password)
    smtp.sendmail(email_sender,email_receiver,em.as_string())