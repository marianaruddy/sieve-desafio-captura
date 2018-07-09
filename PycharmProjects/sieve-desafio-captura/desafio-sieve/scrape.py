# origin para esse projeto é sieve-captura no github

from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.epocacosmeticos.com.br').text
soup = BeautifulSoup(source,'lxml')
# print(soup.prettify())

for link in soup.find_all('a'):
    # if 'https://www.epocacosmeticos.com.br' in link['href']:
        # print(link['href'])

    if 'https://www.epocacosmeticos.com.br' in link['href']:
        linksplitted = link['href'].split('/')
        if link['href'].split('/')[-1:] == ['p']:
            print(link['href'])
            linkPagProd = requests.get(link['href']).text
            soupPagProd = BeautifulSoup(linkPagProd,'lxml')
            # print(soupPagProd.prettify())
            for nomeProd in soupPagProd.find_all('div',class_=""):
                print(nomeProd['content'])



# <meta content="Corretivo para Olhos Maybelline Instant Age Eraser" name="Abstract"/>
