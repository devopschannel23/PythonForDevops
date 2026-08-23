import subprocess

# general
# result = subprocess.run((["docker", "run", "-d", "-p", "8082:80", "nginx"]), capture_output=True, text=True, check=True, timeout=30)

# print(f"Std output:{result.stdout}")
# print(f"Return Code:{result.returncode}")
# print(f"Error:{result.stderr}")

#kubernetes
result = subprocess.run((["kubectl", "get", "pods"]), capture_output=True, text=True, check=True)
if result.returncode == 0:
    with open("pods.txt", "w") as file:
        file.write(result.stdout)
    print(f"Output:{result.stdout}")
else:
    print(result.stderr)
