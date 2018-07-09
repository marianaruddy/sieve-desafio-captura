# origin para esse projeto é sieve-captura no github

from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.epocacosmeticos.com.br').text
soup = BeautifulSoup(source,'lxml')
# print(soup.prettify())

def get_product_pages(soup_):
    products = set()
    for link in soup_.find_all('a'):
        # if 'https://www.epocacosmeticos.com.br' in link['href']:
            # print(link['href'])

        if 'https://www.epocacosmeticos.com.br' in link['href']:
            if link['href'].endswith('/p'):
                products.add(link['href'])
    return products


for url in get_product_pages(soup):
    print(url)
    linkPagProd = requests.get(url).text
    soupPagProd = BeautifulSoup(linkPagProd,'lxml')
    # print(soupPagProd.prettify())
    for nomeProd in soupPagProd.find_all('div',class_="productName"):
        print(nomeProd.text)


result = []
for link in iteravel:
    result.append(link['href'])


result = [link['href'] for link in iteravel]
