import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import math

url = 'https://www.kabum.com.br/espaco-gamer/cadeiras-gamer'

headers ={'User-Ager':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0'}
site = requests.get(url, headers= headers)
soup = BeautifulSoup(site.content, 'html.parser')
quantItens = soup.find('div',id = 'listingCount' ).get_text().strip()
index = quantItens.find(" ")
qtd = quantItens[:index]
ulitmaPagina = math.ceil(int(qtd)/20)
dicProdutos = {'marca':[], 'preco':[]}

for i in range(1, ulitmaPagina+1):
    url_pgn= f'https://www.kabum.com.br/espaco-gamer/cadeiras-gamer?page_number={i}&page_size=20&facet_filters=&sort=most_searched'
    site = requests.get(url_pgn, headers= headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    produtos = soup.find_all('div',class_=re.compile('productCard'))

    for produto in produtos:
        marca = produto.find('span', class_=re.compile('nameCard')).get_text().strip()
        preco = produto.find('span', class_=re.compile('priceCard')).get_text().strip()
        print(marca, preco)
        dicProdutos['marca'].append(marca)
        dicProdutos['preco'].append(preco)


df = pd.DataFrame(dicProdutos)
print(df)


