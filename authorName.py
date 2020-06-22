import requests
import pymongo
import time
client = pymongo.MongoClient(host='localhost', port=27017)

api_key = "你的apikey"
videos = ["你想要的视频id"]


header = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
          }
proxy = {
    "http": "socks5://127.0.0.1:1026", #注意换成自己的代理端口
    'https': 'socks5://127.0.0.1:1026'
}
for i in range(len(videos)):
    videoID = videos[i]
    url = "https://www.googleapis.com/youtube/v3/commentThreads?key="+ api_key + "&textFormat=plainText&part=snippet&videoId=" + videoID +"&maxResults=100"
    base_url = url
    while 1:
        res = requests.get(url, headers=header, proxies=proxy)
        data = res.json()
        
        for i in range(len(data['items'])):
            commentAuthor = data['items'][i]['snippet']['topLevelComment']['snippet']['authorDisplayName']
            print(commentAuthor)     
        try:
            pageToken = data['nextPageToken']
        except KeyError:
            print("Done fetching " + videoID )
            break

        url = base_url + '&pageToken=' + pageToken
        time.sleep(3)

print("done fetching all authors")