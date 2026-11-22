import smtplib

my_email = "devopschannel2308@gmail.com"
password = "xxxxxxxxxxxxxxxxx"
recv_email = "devopschannel2308@yahoo.com"

subject = "This is Subject line"
body = "Hello, This is my first automated mail using Python"
message= f"""From: {my_email}
To: {recv_email}
Subject: {subject}

{body}
"""
try:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            my_email, recv_email, message)

    print("Email sent Successfully!")
except smtplib.SMTPAuthenticationError:
    print("Authentication Error!")
except smtplib.SMTPConnectError:
    print("SMTP server Error!")
except smtplib.SMTPRecipientsRefused:
    print("Recipients Refused!")
except smtplib.SMTPException as e:
    print(e)
except Exception as e:
    print(e)
