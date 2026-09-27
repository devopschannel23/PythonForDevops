#Exceptional Handling
import paramiko

hostname="20.207.200.75"
username="azureuser"
private_key="/home/devops/.ssh/id_rsa"

client = paramiko.SSHClient()

try:
    client.connect(
        hostname=hostname,
        username=username,
        key_filename=private_key
    )
    print("Connected Successfully")
except paramiko.AuthenticationException:
    print("you have got problem related to authentication")
except paramiko.SSHException as e:
    print(f"SSH Exception: {e}")
except Exception as e:
    print(f"Other Exceptions: {e}")
finally:
    client.close()