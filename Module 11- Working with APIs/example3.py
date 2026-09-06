import requests
url="https://api.github.com/do-not-exist"
response=requests.get(url)
print(response.status_code)
response.raise_for_status()