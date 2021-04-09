import tweepy
import markovify
from authorization_tokens import *

# Get raw text as string.
with open("elliot.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)

#NewlineText
#retain_original=False
# Print three randomly-generated sentences of no more than 280 characters
for i in range(1):
    message = text_model.make_short_sentence(240, state_size=3, retain_original=False)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.update_status(message)
print(message)


#docker build . --tag project1:1.0
# docker run --rm -it -v "$(pwd)/app:/app" project1:1.0