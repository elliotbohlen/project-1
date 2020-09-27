import markovify
import random

# Get raw text as string.
with open("elliot.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)


#retain_original=False
# Print three randomly-generated sentences of no more than 280 characters
for i in range(1):
    message = text_model.make_short_sentence(400, state_size=2)
    print(message)



# docker run --rm -it -v "$(pwd)/app:/app" project-1:1.0