# Problem statement:
# 1.Read from CSV
# 2. Extract hostname
# 3. run a ping from subprocess
# 4. Determine whether they are UP or DOWN
# 5. Generate a new CSV report
import csv
import subprocess
#list of dictionries for using it for dictWriter
results=[]

#opening the file
with open("servers3.csv", "r") as file:
    reader=csv.DictReader(file)

    for server in reader:
        hostname=server["hostname"]
        result=subprocess.run(["ping", "-c", "1", hostname], capture_output=True,text=True)

        if result.returncode == 0:
            status="UP"
        else:
            status="DOWN"
        results.append({
            "hostname": hostname,
            "env": server["environment"],
            "status": status
        })
#write to a new csv file as result
with open("ping_status.csv", "w", newline="", encoding="UTF-8") as file:
    fieldnames=["hostname", "env", "status"]
    writer=csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(results)
