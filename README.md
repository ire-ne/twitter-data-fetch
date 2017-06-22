# twitter-data-fetch

Run in the following order for generating OAuth Tokens, authenticating and starting a streaming app for twitter data fetch:
1. generatingOAuth1Tokens.py	(required just once) >> Need to go to the printed URL and copy the pin
2. Input the pin code generated in the previous as oauth_verifier >> generatingActualOAuth1Tokens.py	(required to run just once) >> Once the tokens are generated, they are stored in the following files: oauth_final_tokens, oauth_tokens
3. twitterStreamingDataFetch.py

Run in the following order for generating Access Token, authenticating and starting a simple app which makes a REST API call continuously
1. generatingAccessCode.py (required just once) >> Once the access code is generated, it is stored in twitterAccessKey
2. twitterDataFetch.py
