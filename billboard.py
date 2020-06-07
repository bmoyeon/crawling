import requests
from bs4 import BeautifulSoup
import csv

f = open('billboard.csv', 'w+', encoding='utf-8')
cw = csv.writer(f)
cw.writerow(['rank', 'song', 'artist'])

url = requests.get('https://www.billboard.com/charts/hot-100')
html = url.text

bs = BeautifulSoup(html, 'html.parser')

infos = bs.select('li.chart-list__element')


for info in infos:
    rank = info.select('span.chart-element__rank__number')[0].text
    song = info.select('span.chart-element__information__song')[0].text
    artist = info.select('span.chart-element__information__artist')[0].text

    cw.writerow( (rank, song, artist) )

f.close()