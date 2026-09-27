import paramiko
import getpass

host="20.219.189.61"
username="azureuser"
password=getpass.getpass("Enter Admin Password: ")

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)

client.connect(hostname=host, username=username,password=password,port=22)

print("Connected Successfully!")

stdin1, stdout2, stderr3 = client.exec_command("New-Item test.txt -ItemType File")

print(f"File Created?: {stdout2.read().decode()}")

client.close()

