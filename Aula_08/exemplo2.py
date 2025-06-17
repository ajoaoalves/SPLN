import spacy 
import jjcli 
import re
from collections import Counter

nlp = spacy.load("pt_core_news_lg")
nlp.add_pipe("merge_entities")


cl = jjcli.clfilter()

ocorrencias = Counter()

def limpa_texto(txt):
    # Limpa o texto
    txt = re.sub(r'&amp;','&', txt)
    txt = re.sub(r'\n+', '. ', txt)
    return txt
#Obter Entidades presentes 
#Obter Sents presentes no documento
#Obter Tokens presentes no documento
def entities (txt): 
    arvore_documental = nlp(limpa_texto(txt))

    for frase in arvore_documental.sents: 
        print("Frase: ", frase)
    # Cada uma destas frases é um documento singular 
        for entidade in frase.ents: 
            print("Entidade: ", entidade, entidade.label_)
            ocorrencias[entidade.text] += 1

        #for token in frase: 
        #    print(f"Token: {token.text} | Lemma {token.lemma_} | Pos: {token.pos_} | Ent_type : {token.ent_type_} ") 

        print("--------------------------------------------------")

for txt in cl.text(): 
    result = re.findall(r'<ScopeContent>(.*?)</ScopeContent>', txt, re.DOTALL)
    for i in result:
        entities(i)
    
print("Ocorrencias", ocorrencias)