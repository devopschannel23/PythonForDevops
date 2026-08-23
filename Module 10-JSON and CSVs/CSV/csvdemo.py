import csv

from urllib3.filepost import writer

#--------------Reading the data--------------#
#reader example
# with open("servers.csv", "r", newline="", encoding="utf-8") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row[2])

#dictReader
# with open("servers.csv", "r", newline="", encoding="utf-8") as file:
#     reader=csv.DictReader(file)
#
#     for server in reader:
#         # print(server)
#         print(server["hostname"])

#----------------Writing of csv data--------------#
#using write row
# with open("server_update.csv", "a", newline="", encoding="utf-8") as file:
#     writer=csv.writer(file)
#     #line by line
#     writer.writerow(["hostname", "ip"])
#     writer.writerow(["host4", "10.0.1.2"])
#
#     #multiple line at once
#     writer.writerows([
#         ["host5", "10.11.2.3"],
#         ["host6", "10.9.8.11"]
#     ])

# write the data using dictWriter
servers = [
    {
        "hostname": "web01",
        "status": "DOWN"
    },
    {
        "hostname": "web02",
        "status": "UP"
    }
]
with open("server_update1.csv", "a", newline="", encoding="utf-8") as file:
    fieldnames= ["hostname","status"]
    writer=csv.DictWriter(file,fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(servers)


