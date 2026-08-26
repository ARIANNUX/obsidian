from PIL import Image
from io import BytesIO
import requests

r = requests.get('https://api.github.com/events')
r.raw.read(10)



with open('filename', 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)




















