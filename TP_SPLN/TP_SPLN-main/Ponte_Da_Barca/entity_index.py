import os
import spacy
import re
from collections import defaultdict
from bs4 import BeautifulSoup

# Carregar o modelo de NLP do spaCy
nlp = spacy.load("pt_core_news_lg")
nlp.add_pipe("merge_entities")

# Diretório com os arquivos XML
RECORDS_DIR = "records"
OUTPUT_FILE = "Index.md"

# Dicionários para armazenar entidades por categoria
entidades = {
    "pessoas": defaultdict(int),
    "lugares": defaultdict(int),
    "casas": defaultdict(int)
}

def limpa_texto(txt):
    """
    Limpa o texto removendo caracteres desnecessários.
    """
    txt = re.sub(r'&amp;', '&', txt)
    txt = re.sub(r'\n+', '. ', txt)
    return txt

def extract_scope_content(file_path):
    """
    Extrai o conteúdo da tag <ScopeContent> de um arquivo XML.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        soup = BeautifulSoup(file, "xml")
        scope_content = soup.find_all("ScopeContent")
        return [limpa_texto(tag.get_text()) for tag in scope_content]

def process_entities(text):
    """
    Processa as entidades mencionadas no texto usando spaCy.
    """
    arvore_documental = nlp(text)
    for frase in arvore_documental.sents:
        #print("Frase:", frase)
        for entidade in frase.ents:
            if entidade.label_ == "PER":  # Pessoas
                entidades["pessoas"][entidade.text] += 1
            elif entidade.label_ == "LOC":  # Lugares
                entidades["lugares"][entidade.text] += 1
            elif entidade.label_ == "ORG":  # Casas ou organizações
                entidades["casas"][entidade.text] += 1

def process_records():
    """
    Processa todos os arquivos na pasta records.
    """
    for filename in os.listdir(RECORDS_DIR):
        if filename.endswith(".xml"):
            file_path = os.path.join(RECORDS_DIR, filename)
            #print(f"Processando arquivo: {filename}")
            scope_contents = extract_scope_content(file_path)
            for content in scope_contents:
                process_entities(content)



if __name__ == "__main__":
    process_records()

    # Cria o Index.md APÓS o processamento completo
    with open(OUTPUT_FILE, "w", encoding="utf-8") as md_file:
        md_file.write("## Entidades mencionadas:\n\n")
        
        for categoria, itens in entidades.items():
            if itens:  # Só escreve categorias não vazias
                md_file.write(f"### {categoria.capitalize()}\n")
                
                for entidade, count in sorted(itens.items(), key=lambda x: x[1], reverse=True):
                    md_file.write(f"- {entidade}: {count}\n")
                
                md_file.write("\n")