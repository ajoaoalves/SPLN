import requests
from bs4 import BeautifulSoup
import json


def get_books_category(url):
    response = requests.get(url)

    books = []

    if response.status_code != 200:
        print(f"Failed to load page: {response.status_code}")
        return []

    soup = BeautifulSoup(response.content, "html.parser")

    for book in soup.find_all("div", class_="Livros_Container"):

        
        print("book",book)

        current_book = {}

        current_book["Title"] = book.find("h3", class_="Livros_Titulo").text.strip()
        current_book["Link"] = book.find("a")["href"]
        current_book["download"] = book.find("a", class_="Botao_2")["href"]
       
        books.append(current_book)


    return books


def get_medicine_books(url):
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Failed to load page: {response.status_code}")

    soup = BeautifulSoup(response.content, "html.parser")

    books = soup.find_all("ul", class_="table-of-content-list table-cont")

    medicine_books = {}

    for book in books:
        for li in book.find_all("li"):
            link = li.find("a")["href"] 
            #link = "http://127.0.0.1:3000/Estudo_Teste/medicina/" + link
            link = "http://127.0.0.1:3000/Estudo_Teste/clinica_medica.html"
            medicine_books[link] = get_books_category(link)


    return medicine_books


if __name__ == "__main__":
    books = get_medicine_books("http://127.0.0.1:3000/Estudo_Teste/medicina.html")
    with open("books.json", "w", encoding="utf-8") as file:
        json.dump(books, file, indent=4, ensure_ascii=False)