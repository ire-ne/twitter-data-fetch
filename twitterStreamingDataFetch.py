from twython import TwythonStreamer
from pprint import pprint
import json

APP_KEY = 'C4Wwk6ReE1dRh6acPWuZrdudn'
APP_SECRET = 'ePRF6m5EIlBH65uU3Vn4wU33TprPpeWKeVnG4z4vxiINuu9DOV'

def parse_write(raw_data):
    raw_data_json = json.dumps(raw_data)
    print(raw_data_json)
    fp.write(raw_data_json + "\n")

class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        parse_write(data)

    def on_error(self, status_code, data):
        print(data)
        print(status_code)

        # Want to stop trying to get data because of the error?
        # Uncomment the next line!
        # self.disconnect()

def getOauthTokens():
    fp = open("tokens/oauth_final_tokens")
    lines = fp.readlines()

    tokens_dict = {}

    for line in lines:
        line = line.split("\t")
        tokens_dict[line[0].strip()] = line[1].strip()

    OAUTH_TOKEN = tokens_dict['OAUTH_TOKEN']
    OAUTH_TOKEN_SECRET = tokens_dict['OAUTH_TOKEN_SECRET']
    return OAUTH_TOKEN, OAUTH_TOKEN_SECRET

if __name__ == '__main__':
    fp = open("data/streamingTwitterData.txt","w")
    OAUTH_TOKEN, OAUTH_TOKEN_SECRET = getOauthTokens()

    stream = MyStreamer(APP_KEY, APP_SECRET,
                        OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
    print("streamer instantiated")
    stream.statuses.filter(track='python, tech, programming, function programming, fp, java, C, C++, ml, AI, artificial intelligence, machines, machine learning', language='en')
    # stream.statuses.sample(language='en')
