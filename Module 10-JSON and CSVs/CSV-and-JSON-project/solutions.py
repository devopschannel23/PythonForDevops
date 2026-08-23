# Problem Statement:
import csv
import json
# 1. Read the deployment data from CSV
with open("deployments.csv", "r") as file:
    deployments=list(csv.DictReader(file))
# 2. Read the application health from JSON
with open("health.json", "r") as file:
    health_data=json.load(file)
# 3. match deployments with health data
issues = [] #list of dict
for deployment in deployments:
    for health in health_data["applications"]:
        if deployment["application"] == health["application"]:
            #if deployment was successful but afterwards it got failed
            if (deployment["status"] == "SUCCESS" and health["status"] == "unhealthy"):
                issues.append({
                    "application": deployment["application"],
                    "version": deployment["version"],
                    "cpu": health["cpu"],
                    "memory": health["memory"],
                    "error_rate": health["error_rate"]
                })
# 4. Generate CSV reports -> problematic deployment with their error rate
with open("deplyment_health_report.csv", "w", newline="") as file:
    fields=[
        "application",
        "version",
        "cpu",
        "memory",
        "error_rate"
    ]
    writer =csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(issues)
# 5. Display result
print(f"Problematic Deployments: {len(issues)}")
for issue in issues:
    print(
        f"{issue['application']}"
        f"CPU:{issue['cpu']}%"
    )
