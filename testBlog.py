import requests
import time

header = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
          }
url = "https://seeedstudio.com/blog/2020/05/21/what-is-a-homelab-and-why-you-need-it-m/"

for i in range(100):
    res = requests.get(url, headers=header )
    time.sleep(1)

