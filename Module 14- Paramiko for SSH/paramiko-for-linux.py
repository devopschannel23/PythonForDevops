import paramiko

hostname="20.207.200.75"
username="azureuser"
private_key="/home/devops/.ssh/id_rsa"

client = paramiko.SSHClient()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy)

client.connect(
    hostname=hostname,
    username=username,
    key_filename=private_key
)
stdin1, stdout2, stderr3 = client.exec_command("hostname")

print(f"Hostname is : {stdout2.read().decode()}")

client.close()