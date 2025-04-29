#!/usr/bin/python3

import re
import shelve
import requests
from bs4 import BeautifulSoup as bs
import locale
from dateutil import parser

locale.setlocale(locale.LC_TIME, "pt_PT.UTF-8")

d = shelve.open('pagecache.db')

def myget(url):
    if url not in d:
        d[url] = requests.get(url).text
    return d[url]


def save_article(link):
    page = myget(url+link)
    p = bs(page, 'lxml')

    for article in p.find_all("article"):

        id = article.get("id")
        title = article.find(class_='entry-title')
        author = article.find(class_='fa fa-user')
        date_published = article.find(class_='entry-date published')
        #tipo = article.find(class_='at-cat-item-7').text.strip()
        content = article.find(class_='entry-content').text.strip()

        if date_published:
            date_obj = parser.parse(date_published['datetime'])
            formatted_date = date_obj.strftime("%d de %B de %Y, %H:%M")
        
        with open(f"{id}.txt", "w") as f:
            if title:
                f.write(f"Título: {title.text.strip()}\n\n")
            if author:
                f.write(f"Autor: {author.next_sibling.strip()}\n\n")
            if date_published:
                f.write(f"Data de Publicação: {formatted_date}\n\n")
            #f.write(f"Tipo: {tipo}\n\n")
            f.write(f"{content}\n\n\n\n")
            


url = "https://natura.di.uminho.pt/~jj/bs4/folha8-2023/"
txt = myget(url)
dt = bs(txt, 'lxml')

for table in dt.find_all("table"):
    for tr in table.find_all("tr")[3:10]:
        link = tr.find_all("td")[1].find("a").get("href")
        print(link)
        if re.match(r"\d\d/", link):
            pasta = myget(url+link)
            p = bs(pasta, 'lxml')
            for t in p.find_all("tr")[3:-1]:
                l = t.find_all("td")[1].find("a").get("href")
                print("     " + l)
                save_article(link+l)
        else:
            save_article(link)
            pass


d.close()