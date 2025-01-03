# based on https://til.simonwillison.net/llms/python-react-pattern

import openai
import re
import httpx
import os
from dotenv import load_dotenv

_ = load_dotenv()
from openai import OpenAI

client = OpenAI()

chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello world"}]
)

chat_completion.choices[0].message.content

