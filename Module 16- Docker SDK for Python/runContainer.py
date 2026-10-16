import docker
from docker.api import container

client = docker.from_env()

#start a container
# container = client.containers.run(
#     "nginx:alpine",
#     name="Python-demo-nginx",
#     detach=True,
#     ports={"80/tcp": ("127.0.0.1", 8080)},
#     labels={"managed-by": "python"}
# )
# print("Container: ", container.name)
# print("ID: ", container.short_id)
# print("Status: ", container.status)

#get the container
container=client.containers.get("Python-demo-nginx")
# container.start()

#fetch the latest 10 log lines
logs= container.logs(tail=10)
print(logs.decode("utf-8", errors="replace"))

#execute commands inside container
result= container.exec_run(["nginx", "-t"])
print("Exit Code: ", result.exit_code)
print(result.output.decode("utf-8", errors="replace"))
