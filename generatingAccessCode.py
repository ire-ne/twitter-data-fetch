from twython import Twython

APP_KEY = 'C4Wwk6ReE1dRh6acPWuZrdudn'
APP_SECRET = 'ePRF6m5EIlBH65uU3Vn4wU33TprPpeWKeVnG4z4vxiINuu9DOV'

twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()
fp = open("twitterAccessKey","w")
print(ACCESS_TOKEN)
fp.write("ACCESS_TOKEN" + "\n")
fp.write(ACCESS_TOKEN)
fp.close()
