#!/bin/python3

import os
from sys import argv
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPEN_API_TOKEN"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",            
            "content": "provide me unicode art"
        },
        {
            "role": "user",
            "content": argv[1]
        }
    ],
    model="gpt-4o", temperature=0.1
)


# post a prompt to user
# define the prompt sent to chatgpt

# for arg in argv:
#     print(argv)

print(chat_completion.choices[0].message.content)

