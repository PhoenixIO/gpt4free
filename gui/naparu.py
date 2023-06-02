import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), os.path.pardir))

from gpt4free import you
import json

prompt = sys.argv[1]
response = you.Completion.create(prompt=prompt, detailed=True, include_links=True)

print(response.text)
sys.stdout.flush()
