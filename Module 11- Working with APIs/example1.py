import requests

url="https://api.github.com"
response=requests.get(url)
# print(response.status_code)
#print(response.text)
#print(response.json())
print(response.headers)
