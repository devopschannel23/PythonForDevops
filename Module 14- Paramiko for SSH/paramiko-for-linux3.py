#SFTP
import paramiko

hostname="20.207.200.75"
username="azureuser"
private_key="/home/devops/.ssh/id_rsa"
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
try:
    client.connect(
        hostname=hostname,
        username=username,
        key_filename=private_key
    )
    sftp1=client.open_sftp()
    #sftp1.put("/home/devops/hello.txt", "/home/azureuser/hello.txt")
    sftp1.get("/home/azureuser/hello.txt", "/home/devops/hello.txt")
except paramiko.AuthenticationException:
    print("you have got problem related to authentication")
except paramiko.SSHException as e:
    print(f"SSH Exception: {e}")
except Exception as e:
    print(f"Other Exceptions: {e}")
finally:
    client.close()