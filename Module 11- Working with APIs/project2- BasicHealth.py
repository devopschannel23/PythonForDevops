#basic checks servers are up or not and also response healthy depends on the response time
import time

import requests
url="https://api.github.com/doesnt-exists"

try:
    start_time=time.time()
    response=requests.get(url,timeout=5)
    end_time=time.time()
    response_time=end_time-start_time
    if response.status_code == 200:
        if response_time <= 5:
          print(f"{url} is UP and Healthy")
        else:
          print(f"{url} is UP but Unhealthy")
    else:
        print(f"{url} is DOWN")
except requests.exceptions.RequestException as e:
    print(f"ERROR | {url} | {e}")