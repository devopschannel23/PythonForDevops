import requests
url="https://api.github.com/repos/microsoft/vscode"
response=requests.get(url,timeout=5)
data=response.json()
print(data["name"])
print(data["forks_count"])