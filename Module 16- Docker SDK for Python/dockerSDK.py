import docker

client = docker.from_env()

print(f"Docker Version:", client.version()["Version"])

for container in client.containers.list(all=True):
    container.reload()
    print("Name: ", container.name)
    print("ID: ", container.short_id)
    print("Image: ", container.image.tags)
    print("Status: ", container.status)
    print("-------------------------------------")