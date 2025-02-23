#!/usr/bin/env python3


from jjcli import * 
'''
Repetidas - Remove linhas repetidas num programa. 
Usage - 
    repetidas options file*
Options: 
    - s  fix me keep spaces 
    - e remove empty lines 

'''

def remove_linhas_repetidas(cl): 
    linhas_vistas = set()
   
    for linha in cl.input(): 
        if "-e" not in cl.opt: 
            ln = linha.strip()
        else: 
            ln = linha 
        if not ln or ln not in linhas_vistas: 
            print(ln, end="")
            linhas_vistas.add(ln)


def main (): 
    cl = clfilter(opt="s,e", man=__doc__)
    remove_linhas_repetidas(cl)

if __name__ == '__main__': 
    main()