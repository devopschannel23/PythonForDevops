import subprocess

process = subprocess.Popen(
    ["kubectl", "get", "pods", "-w"],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True
)

try:
    for line in process.stdout:
        print(line, end="")
except KeyboardInterrupt:
    process.terminate()