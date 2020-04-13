import pymongo
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.seeedPM
collection = db.testDB
#product = 'Jetson Nano'

data = pd.DataFrame(list(collection.find()))
wf = pd.DataFrame(data['commentText'].str.split(expand=True).stack().value_counts())
wf.to_excel("wf.xlsx")
data.to_excel("comments.xlsx")
#data = data[data['product'].str.contains(product)]

text = data['commentText'].values
stopwords = ['see', 'run', 'try', 'SBC', 'board', 'love', 'think', 'will', 'really', 'good', 'better', 'pc', 'please', 'make', 'running', 'system', 'might', 'possible', 'know', 'thank', 'need', 'build', 'version', 'great', 'test', 'PC', 'one', 'work', 'nice', 'look', 'using',
             'want', 'thing', 'come', 'window', 'full', 'etc', 'go', 'use', 'even', 'boards', 'now', 'maybe', 'thanks', 'rather', 'interested', 'something', 'new', 'review', 'option', 'around', 'much', 'enough', 'things', 'amazing', 'take', 'anything', 'cool', 'looking'] + list(STOPWORDS)



wordcloud = WordCloud(
    width=3000,
    height=2000,
    background_color='white',
    stopwords=stopwords).generate(str(text))
fig = plt.figure(
    figsize=(40, 30),
    facecolor='k',
    edgecolor='k')
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.tight_layout(pad=0)
plt.show()
