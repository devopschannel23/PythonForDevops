import json
deployment = {
    "app_name": "webApp01",
    "version": "v1.2.0",
    "environment": "Production",
    "status": "UP"
}
with open("deplyment.json", "w") as file:
    json.dump(deployment,file,indent=4)