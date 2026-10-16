import docker

#filtering exit containers
# client = docker.from_env()

# for container in client.containers.list(all=True):
#     container.reload()
#     if container.status == "exited":
#         print(f"Stopped Containers: {container.name}")

#exceptional handling
try:
    client = docker.from_env()
    client.ping()
    container = client.containers.get("Python-demo-nginx1")
    print("Container Status: ", container.status)
except docker.errors.NotFound:
    print("Container does not exist")
except docker.errors.DockerException as e:
    print("Docker Connect or SDK error", e)
