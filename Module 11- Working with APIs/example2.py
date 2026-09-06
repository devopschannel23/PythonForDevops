#parameters
import requests

url="https://api.github.com/search/repositories"
params={
    "q": "python"
}
response=requests.get(url, params=params)
print(response.url)
print(response.json())
