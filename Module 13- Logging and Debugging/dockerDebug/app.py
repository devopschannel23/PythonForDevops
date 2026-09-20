import debugpy
import time

debugpy.listen(("0.0.0.0", 5678))

print("Waiting for python debugger...")
debugpy.wait_for_client()

print("Debugger Connected!")

env="Production"
replicas=3

print(f"env: {env}")
print(f"replicas: {replicas}")

for i in range(replicas):
    print(f"Deploying replicas {i+1}")
    time.sleep(2)

