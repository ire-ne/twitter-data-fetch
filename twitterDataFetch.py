from twython import Twython
from pprint import pprint

def parseAndWrite(raw_data):
    statuses = raw_data['statuses']
    for status in statuses:
        text = status['text']
        hashtags = status['entities']['hashtags']
        print(len(hashtags))
        if(len(hashtags)==0):
            return
        # print(hashtags)
        hashtags_text = []
        for h in hashtags:
            hashtags_text.append(h['text'])
        hashtags_text = ",".join(hashtags_text)
        print(text)
        print(hashtags_text)
        fp.write(text + "\n")
        fp.write(hashtags_text + "\n")


if __name__ == '__main__':
    fp = open("twitterAccessKey")
    fp.readline()
    ACCESS_TOKEN = fp.readline()
    ACCESS_TOKEN = ACCESS_TOKEN.strip()
    APP_KEY = 'C4Wwk6ReE1dRh6acPWuZrdudn'
    twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)
    fp = open("data/pythonData.txt","w")
    while True:
        temp = twitter.search(q='python', count=100, lang='en')
        parseAndWrite(temp)
