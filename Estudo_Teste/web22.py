import requests
from bs4 import BeautifulSoup
import json

def get_uc_info(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, "html.parser")
        
        return {
            "title": soup.find("div", class_="uc_title").find("b").get_text(strip=True) if soup.find("div", class_="uc_title") else "",
            "description": soup.find("div", class_="uc_descricao").find("p").get_text(strip=True) if soup.find("div", class_="uc_descricao") else ""
        }
    except Exception as e:
        return {"error": str(e)}

def get_plano(url):

    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Failed to load page: {response.status_code}")

    soup = BeautifulSoup(response.content, "html.parser")

    uc = soup.find_all("tr")[1:]

    ucs_book = {}

    for uc_info in uc:
        tds = uc_info.find_all("td")
        link = tds[1].find("a")["href"]

        #link = "http://127.0.0.1:3000/Estudo_Teste/lei/ucs" + link
        link = "http://127.0.0.1:3000/Estudo_Teste/lei/ucs/logica.html"
        ucs_book[link] = get_uc_info(link)


    return ucs_book

if __name__ == "__main__":
    books = get_plano("http://127.0.0.1:3000/Estudo_Teste/lei/ucs.html")
    with open("ucs.json", "w", encoding="utf-8") as file:
        json.dump(books, file, indent=4, ensure_ascii=False)