#!/usr/bin/python3

import re
import shelve
import requests
from bs4 import BeautifulSoup as bs


# para não ser banido de sítio 
d = shelve.open("pagecache.db")

def myget(url):
    if url not in d:
        #print(f"... getting {url}")
        d[url] = requests.get(url).text
    return d[url]

# lista de dicionario
lista_pt_cn = []

# extrair tabelas
# dtf - data tree do filho
def proc_filho(txt, cat):
    dtf = bs(txt,'lxml')
    for tab in dtf.find_all("table", class_="mytable2"):
        for tr in tab.find_all("tr"): # table row
            #print(tr)
            # buscar td se tiver três
            filhos = tr.find_all("td") # lista de filhos (dts)
            if len(filhos) == 3:
                pt,py,cn = filhos
                # selecionar só o text
                lista_pt_cn.append({
                    "pt": pt.text,
                    "py": py.text,
                    "cn": cn.text,
                    "dom": cat
                })

def main():
    url = "https://www.jonsay.co.uk/dictionary.php?langa=Portuguese&langb=Chinese"

    txt = myget(url)
    dt = bs(txt, "lxml")

    # buscar cada um dos links
    n=1
    for link in dt.find_all("a", class_="nav"):
        cat = link.text # categoria
        # print("ir buscar...",link["href"])
        txt2 = myget(link["href"])
        proc_filho(txt2, cat)
        n += 1
        if n == 4:
            break
        
main()   
print(lista_pt_cn)
d.close()


# item_tags = dt.find_all('item')(text="...")
