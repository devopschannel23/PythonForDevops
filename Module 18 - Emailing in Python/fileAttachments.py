import smtplib
import ssl
import os
from email.contentmanager import maintype
from email.message import EmailMessage

sender="devopschannel2308@gmail.com"
password="xxxxxxxxxxxxxxxx"
receiver="devopschannel2308@yahoo.com"

msg=EmailMessage()

msg["Subject"] = "Application Log Report"
msg["From"] = sender
msg["To"] = receiver

msg.set_content("Hello team,\n\nPlease find the attached app log file.")

file_path="application.log"

with open(file_path, "rb") as file:
    file_data = file.read()
    msg.add_attachment(
        file_data,
        maintype="text",
        subtype="plain",
        filename=os.path.basename(file_path))

with smtplib.SMTP("smtp.gmail.com",587) as connection:
    connection.starttls()
    connection.login(user=sender,password=password)
    connection.send_message(msg)

