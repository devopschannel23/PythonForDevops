import csv

with open("servers2.csv", "r", newline="", encoding="utf-8") as file:
    reader=csv.DictReader(file)
    for server in reader:
        hostname=server["hostname"].strip().lower()
        environment=server["env"].strip().lower()
        cpu_usages=int(server["cpu_usage"])

        if (server["env"] == "prod" and cpu_usages < 80):
            print(f"Healthy Server: {server['hostname']}")
            print(f"CPU_Usage: {server['cpu_usage']}%")
