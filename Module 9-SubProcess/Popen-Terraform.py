import subprocess

process = subprocess.Popen(
    ["terraform", "apply", "-auto-approve"],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True
)

for line in process.stdout:
    print(line, end="")

return_code = process.wait()

if return_code == 0:
    print("Terraform deployment successful")
else:
    print("Terraform deployment failed")