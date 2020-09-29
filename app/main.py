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
for i in range(3):
    message = text_model.make_short_sentence(280, state_size=2)

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.update_status(message)
print(message)
print("done")

#docker build . --tag project1:1.0
# docker run --rm -it -v "$(pwd)/app:/app" project-1:1.0