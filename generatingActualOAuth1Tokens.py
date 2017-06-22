from twython import Twython

APP_KEY = 'C4Wwk6ReE1dRh6acPWuZrdudn'
APP_SECRET = 'ePRF6m5EIlBH65uU3Vn4wU33TprPpeWKeVnG4z4vxiINuu9DOV'

oauth_verifier = 7408809
fp = open("tokens/oauth_tokens")
lines = fp.readlines()

tokens_dict = {}

for line in lines:
    line = line.split("\t")
    tokens_dict[line[0].strip()] = line[1].strip()

OAUTH_TOKEN = tokens_dict['OAUTH_TOKEN']
OAUTH_TOKEN_SECRET = tokens_dict['OAUTH_TOKEN_SECRET']

twitter = Twython(APP_KEY, APP_SECRET,
                  OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

final_step = twitter.get_authorized_tokens(oauth_verifier)
OAUTH_TOKEN = final_step['oauth_token']
OAUTH_TOKEN_SECRET = final_step['oauth_token_secret']

fp = open("tokens/oauth_final_tokens","w")
fp.write("OAUTH_TOKEN\t" + OAUTH_TOKEN + "\n")
fp.write("OAUTH_TOKEN_SECRET\t" + OAUTH_TOKEN_SECRET)

print(OAUTH_TOKEN)
print(OAUTH_TOKEN_SECRET)