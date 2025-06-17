import re
import shelve
import requests
from bs4 import BeautifulSoup as bs

# para não ser banido de sítio 
d = shelve.open("pagecache.db")

links = "https://natura.di.uminho.pt/~jj/bs4/folha8-2023/"
# url = "https://natura.di.uminho.pt/~jj/bs4/folha8-2023/27-05-77-80-mil-assassinatos/"

def myget(url):
    if url not in d:
        d[url] = requests.get(url).text
    return d[url]

def main():
    txt = myget(links)
    dt = bs(txt, "lxml")
    
    num = 0
    for link in dt.find_all("a", class_="nav"):
        txt2 = myget(link["href"])
        dtf = bs(txt2,'lxml')
        
        for artigo in dtf.find_all("article"):
            print(f"Artigo nº{num} -> {artigo.text} \n")
            num += 1
        
main()  
d.close()
