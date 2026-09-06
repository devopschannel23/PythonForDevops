#create issues after authentication and after verifying that your company app is down
import requests
import os

url1="https://api.github.com/repos/devopschannel23/markdown.io/issues"
url2="https://api.github.com/anotherURL"

response2=requests.get(url2,timeout=5)
token1=os.getenv("GITHUB_TOKEN")
if response2.status_code != 200:
   header = {
       "Authorization": f"Bearer {token1}",
       "Accept": "application/vnd.github+json",
       "X-Github-Api-Version": "2022-11-28",
       "Content-Type": "application/json"
   }
   data ={
       "title": "Company app is not responding!",
       "body": "Please fix the deployments ASAP!"
   }
   response1=requests.post(url1, headers=header, json=data)
   print(f"Status Code: {response1.status_code}")
   print(f"Data:{response1.json()}")
else:
    print(f"Your company URL {url2} is up and running fine!")

