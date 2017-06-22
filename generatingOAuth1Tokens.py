from twython import Twython

APP_KEY = 'C4Wwk6ReE1dRh6acPWuZrdudn'
APP_SECRET = 'ePRF6m5EIlBH65uU3Vn4wU33TprPpeWKeVnG4z4vxiINuu9DOV'


twitter = Twython(APP_KEY, APP_SECRET)
auth = twitter.get_authentication_tokens()

OAUTH_TOKEN = auth['oauth_token']
OAUTH_TOKEN_SECRET = auth['oauth_token_secret']

fp = open("tokens/oauth_tokens","w")
fp.write("OAUTH_TOKEN\t" + OAUTH_TOKEN + "\n")
fp.write("OAUTH_TOKEN_SECRET\t" + OAUTH_TOKEN_SECRET)
print(auth['auth_url'])
