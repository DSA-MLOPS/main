import requests
import sys

import requests

url = 'http://localhost:8000/stream'
response = requests.get(url, stream=True)

for line in response.iter_lines():
    if line:
        line_str = line.decode()
        if line_str == '[DONE]':
            print('Done streaming')
            break
        print(line_str, flush=True)

