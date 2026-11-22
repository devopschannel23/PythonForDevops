import smtplib
import ssl
from email.message import EmailMessage

sender=devopschannel2308@gmail.com
password="xxxxxxxxxxxxxxxx"
to_emails = [
    "dev1@gmail.com",
    "dev2@gmail.com"
]
cc_emails = [
    "manager@gmail.com"
]
bcc = [
    "admin@gmail.com"
]
msg = EmailMessage()
msg["From"] = sender
msg["To"] = ", ".join(to_emails)
msg["Cc"] = ", ".join(cc_emails)
msg["Bcc"] = ", ".join(bcc)
msg["Subject"] = "Message send to multiple recipients"
msg.set_content("""
Hello Team,

Deployment was completed Successfully!

Regards,
DevOps Team
""")

all_recipients = to_emails + cc_emails + bcc

with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=sender, password=password)
    connection.send_message(msg, from_addr=sender, to_addrs=all_recipients)
