# 1. Create a sh file that has all basic command:
# hostname, uptime, free -m, df -h, ps aux --sort=-%cpu | head 10, ss -tunl
# 2. put that script file to remote server
# 3. execute that script(set execute permission and then you execute)
# 4. export all the things to a log file
# 5. get back that log file to the controller machine
import paramiko
hostname="20.207.200.75"
username="azureuser"
private_key="/home/devops/.ssh/id_rsa"

local_script="/home/devops/paramiko-hc/health_check.sh"
remote_script="/home/azureuser/health_check.sh"

#connecting to the client
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
print("Connecting to Server...")
client.connect(
        hostname=hostname,
        username=username,
        key_filename=private_key
    )
print("Connected to Server!")

#opening sftp & placing script to remote
sftp=client.open_sftp()
print("Uploading script file to remote...")
sftp.put(local_script, remote_script)
print("Successfully Uploaded.")
sftp.close()

#make script executable & create an empty test file
stdin, stdout, stderr=client.exec_command("chmod +x /home/azureuser/health_check.sh && touch /home/azureuser/health_check.log")
stdout.read()

#execute it & save output to log file
print("Running Health check on remote machine...")
stdin1, stdout1, stderr1 = client.exec_command(
    "/home/azureuser/health_check.sh > /home/azureuser/health_check.log 2>&1"
)
stdout1.read()
stderr1.read()
print("Health check created on remote host")

print("Coping the log to managed host")
#download the log file to client
sftp= client.open_sftp()
sftp.get("/home/azureuser/health_check.log", "/home/devops/health_check_remote.log")
sftp.close()

client.close()





