#multiple commands
import paramiko
from debugpy.launcher import output

hostname="20.207.200.75"
username="azureuser"
private_key="/home/devops/.ssh/id_rsa"

client = paramiko.SSHClient()

commands = [
    "hostname",
    "uptime",
    "df -h",
    "free -m",
    "systemctl status nginx"
]

client.set_missing_host_key_policy(paramiko.AutoAddPolicy)

client.connect(
    hostname=hostname,
    username=username,
    key_filename=private_key
)

for command in commands:
    stdin,stdout,stderr=client.exec_command(command)
    stdout1=stdout.read().decode()
    stderr1=stderr.read().decode()
    print(f"Command: {command}")
    print(f"Output: {stdout1}")
    if stderr1:
        print(f"Error: {stderr1}")
    exit_status_code= stdout.channel.recv_exit_status()
