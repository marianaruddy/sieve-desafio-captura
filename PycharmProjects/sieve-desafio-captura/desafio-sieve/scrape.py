import string

from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.epocacosmeticos.com.br').text

soup = BeautifulSoup(source,'lxml')

# print(soup.prettify())

for link in soup.find_all('a'):
    if 'https://www.epocacosmeticos.com.br' in link['href']:
        print(link['href'])
