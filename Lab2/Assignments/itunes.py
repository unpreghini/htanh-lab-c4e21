import requests
import pyexcel
from collections import OrderedDict

url = 'https://itunes.apple.com/us/rss/topsongs/limit=100/json'

response = requests.get(url)

data = response.json()

songs = []

for itunes_data in data['feed']['entry']:
    artist = itunes_data['im:artist']['label']
    title = itunes_data['im:name']['label']
    song = OrderedDict({
        "Title": title,
        "Artist": artist,
    })
    songs.append(song)

pyexcel.save_as(records=songs, dest_file_name="top100_itunes.xlsx")
