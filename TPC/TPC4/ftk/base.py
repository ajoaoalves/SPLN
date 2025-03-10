import re
import jjcli
from collections import Counter
from itertools import islice
import json

def lexer(txt):
    return re.findall(r'\w+(?:-\w+)*|[^\w\s]+', txt)

def counter(tokens):
    """Conta a frequência absoluta dos tokens."""
    return Counter(tokens)

def frequencia_relativa(contagem_tokens):
    total_tokens = sum(contagem_tokens.values())
    if total_tokens == 0:
        return {token: 0 for token in contagem_tokens}
    return {token: contagem / total_tokens * 1000000 for token, contagem in contagem_tokens.items()}, total_tokens

def pretty_print(freq, relative_freq, opt):
    """Exibe ou salva os resultados conforme as opções escolhidas."""
    
    if "-r" in opt:
        dict_1, total_tokens = relative_freq
        print(f"Total de tokens: {total_tokens}")
    else:
        dict_1 = freq  # Frequência absoluta por padrão

    if "-m" in opt:
        new_dict = dict(islice(dict_1.items(), int(opt["-m"])))
    else:
        new_dict = dict_1

    if "-j" in opt:
        try:
            with open("freq.json", "w", encoding="utf-8") as arquivo:
                json.dump(new_dict, arquivo, ensure_ascii=False, indent=4)
            print("Frequência salva em freq.json")
        except Exception as e:
            print(f"Erro ao salvar o arquivo: {e}")
    else:
        print("\n\nToken        Frequência\n")
        for token, count in new_dict.items():
            if "-a" in opt:  # Exibir frequência absoluta, se ativado
                print(f'{token}:\t\t{count}')
            else:  # Exibir frequência relativa (caso -r seja ativado)
                print(f'{token}:\t\t{count:.2f}')

def main():
    """
    Opções:
      -a: frequência absoluta
      -r: frequência relativa
      -m 500: top 500 palavras
      -j: saída em JSON
    """
    cl = jjcli.clfilter("arm:j", doc=main.__doc__)  # Adicionando a opção "-a"
    tokens = []
    for txt in cl.text():
        tokens.extend(lexer(txt)) 

    c = counter(tokens)
    relative_freq = frequencia_relativa(c)
    pretty_print(c, relative_freq, cl.opt)

if __name__ == "__main__":
    main()
