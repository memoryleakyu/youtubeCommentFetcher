import requests
import pymongo
import time
client = pymongo.MongoClient(host='localhost', port=27017)
db = client.seeedPM
#collection = db.youtubeComment
collection = db.testDB

videos = ["YLOUhaqkLqY","Dd-qqaIL-ko","4XV8dlFwNd0","lrP5T6LrkPQ"]


header = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
          }
proxy = {
    "http": "socks5://127.0.0.1:1026",
    'https': 'socks5://127.0.0.1:1026'
}
for i in range(len(videos)):
    videoID = videos[i]
    url = "https://www.googleapis.com/youtube/v3/commentThreads?key={yourapikey}&textFormat=plainText&part=snippet&videoId=" + videoID +"&maxResults=100"
    base_url = url
    while 1:
        res = requests.get(url, headers=header, proxies=proxy)
        data = res.json()
        
        for i in range(len(data['items'])):
            commentText = data['items'][i]['snippet']['topLevelComment']['snippet']['textOriginal']
            likeCount = data['items'][i]['snippet']['topLevelComment']['snippet']['likeCount']
            userID = data['items'][i]['snippet']['topLevelComment']['snippet']['authorChannelId']['value']
            totalReply = data['items'][0]['snippet']['totalReplyCount']
            publishDate = data['items'][0]['snippet']['topLevelComment']['snippet']['publishedAt']
            comments = {
                'videoID': videoID,
                'product': 'Oydyssey',
                'commentText': commentText,
                'likeCount': likeCount,
                'userID': userID,
                'totalReply': totalReply,
                'publishDate': publishDate
            }
            collection.insert_one(comments)
            print(commentText)     
        try:
            pageToken = data['nextPageToken']
        except KeyError:
            print("Done fetching " + videoID )
            break

        url = base_url + '&pageToken=' + pageToken
        time.sleep(3)

print("done fetching all comments")