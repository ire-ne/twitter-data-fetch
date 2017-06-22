# twitter-data-fetch

Run in the following order for generating OAuth Tokens, authenticating and starting a streaming app for twitter data fetch. There are two options: 
stream.statuses.filter(track='python, tech', language='en') #This filters the statuses corresponding to the tracks given
stream.statuses.sample(language='en')# This outputs a small sample from the public statuses streamed.

1. generatingOAuth1Tokens.py	(required just once) >> Need to go to the printed URL and copy the pin
2. Input the pin code generated in the previous as oauth_verifier >> generatingActualOAuth1Tokens.py	(required to run just once) >> Once the tokens are generated, they are stored in the following files: oauth_final_tokens, oauth_tokens
3. twitterStreamingDataFetch.py

Run in the following order for generating Access Token, authenticating and starting a simple app which makes a REST API call continuously for twitter data fetch corresponding to the keywords defined in q
temp = twitter.search(q='python', count=100, lang='en')

1. generatingAccessCode.py (required just once) >> Once the access code is generated, it is stored in twitterAccessKey
2. twitterDataFetch.py
