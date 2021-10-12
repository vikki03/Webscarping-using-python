scrapping - using - python
import urllib.request
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

url = 'https://www.practo.com/chennai/clinics/siddha-clinics'
response = requests.get(url)
response
soup = BeautifulSoup(response.text, "html.parser")
soup
x = [i.get('href') for i in soup.find_all('a', limit=30)]
type(x)
df = pd.DataFrame(x, columns=['url'])
df
y = ['https://www.practo.com']
df['url'] = y + df.url
df
##importing hyper links to csv
df.to_csv('sample.csv', index=False, encoding='utf-8')
##getting individuals records from csv
urll = df.url[2]
responsee = requests.get(urll)
responsee
soup1 = BeautifulSoup(responsee.text, "html.parser")
soup1
y = [j.get('href') for j in soup1.find_all('a', limit=30)]
type(y)
artist_name_list = soup1.find(class_='tabs react-tabs')
artist_name_list_items = artist_name_list.find_all('a')
for artist_name in artist_name_list_items:
    print(artist_name.prettify())

    artist_name_list = soup1.find(class_='tabs react-tabs')
artist_name_list_items = artist_name_list.find_all('a')

for artist_name in artist_name_list_items:
    print(artist_name.prettify())
for artist_name in artist_name_list_items:
    names = artist_name.contents[0]
    print(names)
    print(names)