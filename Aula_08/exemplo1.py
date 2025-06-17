import spacy

nlp = spacy.load("pt_core_news_lg")
nlp.add_pipe("merge_entities") #junto as entidades de forma completa

documento = "O João Manuel da Silva nasceu em Tebosa em Fevereiro de 1901. Emigrou para a cidade de S. Paulo no Brasil."

ad = nlp(documento)

#Obter as frases: cada uma destas frases é um documento singular

for frase in ad.sents :
    print("Frase:", frase)

    #Obter as entidades

    for entidade in frase.ents:
        print("Entidade:", entidade, entidade.label_ )
    
    #Obter os tokens

    for token in frase:
        print(f"Token:  {token.text} | Lemma: {token.lemma_} | Pos: {token.pos_} | Ent_type: {token.ent_type_}")
        