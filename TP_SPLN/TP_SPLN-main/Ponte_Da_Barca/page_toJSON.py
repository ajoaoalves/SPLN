import os
import json
from bs4 import BeautifulSoup

# Caminho para a pasta 'records'
records_path = "records"
output_json_path = "output.json"

def process_records(path):
    """
    Percorre os arquivos XML na pasta especificada, extrai informações relevantes,
    e salva os dados em um arquivo JSON.
    """
    records = []
    for filename in os.listdir(path):
        if filename.lower().endswith(".xml"):  # Aceita .XML e .xml
            file_path = os.path.join(path, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                    soup = BeautifulSoup(content, 'xml')
                    record = parse_record(soup)
                    if record:
                        records.append(record)
            except Exception as e:
                print(f"Erro ao processar {filename}: {e}")
    
    if records:
        save_to_json(records, output_json_path)
    else:
        print("Nenhum registro válido encontrado.")

def parse_record(soup):
    """
    Extrai informações de um registro XML.
    """
    description_item = soup.find('DescriptionItem')
    if not description_item:
        return None
    
    id_tag = description_item.find('ID')
    root_parent_tag = description_item.find('RootParent')
    parent_tag = description_item.find('Parent')
    description_level_tag = description_item.find('DescriptionLevel')
    unit_title_tag = description_item.find('UnitTitle')
    
    return {
        "ID": id_tag.text.strip() if id_tag else None,
        "RootParent": root_parent_tag.text.strip() if root_parent_tag else None,
        "Parent": parent_tag.text.strip() if parent_tag else None,
        "DescriptionLevel": description_level_tag.text.strip() if description_level_tag else None,
        "UnitTitle": unit_title_tag.text.replace('\n', ' ').strip() if unit_title_tag else None
            }

def save_to_json(data, output_path):
    """
    Salva os dados em JSON.
    """
    with open(output_path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    print(f"Dados salvos em: {output_path}")

def construir_arvore(dados):
    """
    Constrói a árvore hierárquica a partir dos dados.
    """
    nodes = {item['ID']: {**item, 'children': []} for item in dados if item['ID']}
    raiz = []
    for item in dados:
        parent_id = item.get('Parent')
        if parent_id == '0' or not parent_id:
            raiz.append(nodes[item['ID']])
        else:
            if parent_id in nodes:
                nodes[parent_id]['children'].append(nodes[item['ID']])
    return raiz

def imprimir_arvore(nos, nivel=0):
    """
    Imprime a árvore no console.
    """
    for no in nos:
        id_ = no.get('ID', '—')
        desc = no.get('DescriptionLevel', '—')
        titulo = no.get('UnitTitle', '—')
        print('  ' * nivel + f"{id_} - {desc} - {titulo}")


        imprimir_arvore(no['children'], nivel + 1)

if __name__ == "__main__":
    # Passo 1: Processar os XMLs e gerar o JSON
    process_records(records_path)
    
    # Passo 2: Carregar o JSON e imprimir a árvore
    try:
        with open(output_json_path, 'r', encoding='utf-8') as f:
            dados = json.load(f)
            arvore = construir_arvore(dados)
            imprimir_arvore(arvore)
    except FileNotFoundError:
        print("Arquivo output.json não encontrado. Verifique se há dados processados.")
    except json.JSONDecodeError:
        print("Erro ao ler o arquivo JSON. Formato inválido.")