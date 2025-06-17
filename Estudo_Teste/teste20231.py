import shelve
import requests
import json
from bs4 import BeautifulSoup
from urllib.parse import urljoin

d = shelve.open("pagecache.db")

def myget(url):
    if url not in d:
        d[url] = requests.get(url).text
    return d[url]

def main():
    base_url = "http://127.0.0.1:3000/Estudo_Teste/modalidades.html"
    main_html = myget(base_url)
    main_soup = BeautifulSoup(main_html, 'html.parser')

    modalities = {}
    table = main_soup.find('table', class_='modalities-table')

    for row in table.find_all('tr')[1:]:  # Ignora o cabeçalho
        cols = row.find_all('td')
        link = cols[1].find('a')
        if link:
            # Extrair nome e URL da modalidade
            modality_name = link.get_text(strip=True)
            
            linkmodalidade = "http://127.0.0.1:3000/Estudo_Teste/modalidades"
            #linkmodalidade = cols[1].find('a')['href']
            modalidade_html = myget(linkmodalidade)
            modalidade_soup = BeautifulSoup(modalidade_html, 'html.parser')
            # Extrair detalhes
            details = {
                'dificuldade': cols[2].get_text(strip=True),  # Dificuldade da tabela principal
                'instrutor': 'Não especificado',
                'horario': []
            }
            # Extrair instrutor da página detalhada
            detail_list = modalidade_soup.find('ul', class_='sport-details')
            if detail_list:
                for item in detail_list.find_all('li', class_='sport-detail'):
                    text = item.get_text(strip=True)
                    if 'Instrutor:' in text:
                        details['instrutor'] = text.split(':')[-1].strip()
            # Extrair horários formatados corretamente
            schedule_table = modalidade_soup.find('table', class_='schedule-table')
            if schedule_table:
                for row in schedule_table.find_all('tr')[1:]:  # Ignorar cabeçalho
                    cells = row.find_all('td')
                    # Formatar como "HH:MM - HH:MM"
                    time_range = cells[1].get_text(strip=True) 
                    details['horario'].append(time_range)
            modalities[modality_name] = details

    # Salvar em JSON
    with open('modalidades.json', 'w', encoding='utf-8') as f:
        json.dump(modalities, f, ensure_ascii=False, indent=2, sort_keys=True)

    d.close()

if __name__ == "__main__":
    main()