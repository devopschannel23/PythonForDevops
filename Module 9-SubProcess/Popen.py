import subprocess

process = subprocess.Popen(
    ["/usr/bin/python3"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)
# kill(), terminate(), poll(), wait()

stdout, stderr = process.communicate(
    input="print('Hello from DevOps')\n"
)
# process.kill

print(stdout)