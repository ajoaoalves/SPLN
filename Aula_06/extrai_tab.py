#!/usr/bin/python3

import re, csv
import shelve
import requests
import jjcli
from bs4 import BeautifulSoup as bs


# para não ser banido de sítio 
d = shelve.open("pagecache.db")

def myget(url):
    if url not in d:
        #print(f"... getting {url}")
        d[url] = requests.get(url).text
    return d[url]

# extrair tabelas
def main():
    cl = jjcli.clfilter("s:")
    sep = cl.opt.get("-s",", ") # se não disser nada o separator vai ser ,
    for url in cl.args:
        txt = myget(url)
        dt = bs(txt,'lxml')
        n=0
        for tab in dt.find_all("table"):
            n += 1
            if tab.find_all("table"): # se tiver pelo menos uma continua-se
                continue
            csv=""
            for tr in tab.find_all("tr"): # table row
                filhos = [re.sub(r"\s+","",f.text) for f in tr.find_all("td")] # tirar espaços
                csv += sep.join(filhos) + "\n"
            print(f"==> {url} // {n}\n{csv}")
             

main()   

d.close()


#tem_tags = dt.find_all('item')(text="...")
