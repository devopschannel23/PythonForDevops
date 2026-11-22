import smtplib
import ssl
from email.message import EmailMessage

sender="devopschannel2308@gmail.com"
password="xxxxxxxxxxxxxxxx"
receiver="devopschannel2308@yahoo.com"

msg=EmailMessage()
msg["Subject"] = "Server health Reports"
msg["From"] = sender
msg["To"] = receiver

#add plain text
msg.set_content("""
Hello team,

Deployment was sent, details are following by
""")

#add HTML content
html_content = """
<html>
<body>
  <h2 style="color:green;">Server health Reports</h2>
  <p>Hello Team, </p>
  <p>Below are the details:</p>
  <table border="1" cellpadding="10" cellspacing="0">
  <tr>
      <th>Metric</th>
      <th>Usage</th>
      <th>Status</th>
  </tr>
  <tr>
      <td>CPU Usage</td>
      <td>45%</td>
      <td style="color:green;">Healthy</td>
  </tr>
  <tr>
      <td>Memory</td>
      <td>98%</td>
      <td style="color:red;">Unhealthy</td>
  </tr>
  </table>
  </body>
  </html>
  """
msg.add_alternative(html_content, subtype="html")

with smtplib.SMTP("smtp.gmail.com",587) as connection:
    connection.starttls()
    connection.login(user=sender,password=password)
    connection.send_message(msg)
