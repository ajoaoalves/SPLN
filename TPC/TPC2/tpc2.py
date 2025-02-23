#!/usr/bin/env python3

from jjcli import *

'''
Repetidas - Remove linhas repetidas num programa. 
Usage - 
    repetidas options file*
Options: 
    -s   keep spaces 
    -e   remove empty lines 
    -p   replace empty lines with # and puts # before duplicate lines
'''

def remove_linhas_repetidas(cl): 
    linhas_vistas = set()  

    for linha in cl.input():  
        # Se "-s" não está presente, remove os espaços em branco do início e fim
        if "-s" not in cl.opt: 
            ln = linha.strip()  
        
        # Se a linha estiver vazia
        if not ln or ln in linhas_vistas:
            if "-p" in cl.opt:  # Se "-p" for passado, substitui por "#" nas linhas vazias ou duplicadas
                print("#" + ln)
                continue
        if not ln:
            if "-e" in cl.opt:  # Se "-e" for passado, ignora a linha vazia
                continue  
        else:
            ln = linha  
        if not ln or ln not in linhas_vistas:  
            print(ln)  
            linhas_vistas.add(ln) 

def main(): 
    cl = clfilter(opt="s,e,p", man=__doc__)  # Definindo as opções válidas: -s, -e, -p
    remove_linhas_repetidas(cl)

if __name__ == '__main__': 
    main() 

    