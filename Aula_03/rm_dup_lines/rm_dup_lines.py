#!/usr/bin/env python3


from jjcli import *

'''
Repetidas - Remove linhas repetidas num programa. 
Usage - 
    repetidas options file*
Options: 
    -s   keep spaces 
    -e   remove empty lines 
    -p   replace empty lines with #
'''

def remove_linhas_repetidas(cl): 
    linhas_vistas = set()  # Para armazenar linhas únicas

    for linha in cl.input():  # Itera sobre as linhas do arquivo
        # Se "-s" não está presente, remove os espaços em branco do início e fim
        if "-s" not in cl.opt: 
            ln = linha.strip()  
        else:
            ln = linha  # Mantém os espaços
        
        # Se a linha estiver vazia
        if not ln:
            if "-p" in cl.opt:  # Se "-p" for passado, substitui por "#"
                print("#")
                continue
            elif "-e" in cl.opt:  # Se "-e" for passado, ignora a linha vazia
                continue  

        # Se a linha não for duplicada
        if not ln or ln not in linhas_vistas:  
            print(ln, end="")  # Imprime sem duplicatas
            linhas_vistas.add(ln)  # Adiciona a linha ao conjunto

def main(): 
    cl = clfilter(opt="s,e,p", man=__doc__)  # Definindo as opções válidas: -s, -e, -p
    remove_linhas_repetidas(cl)

if __name__ == '__main__': 
    main()