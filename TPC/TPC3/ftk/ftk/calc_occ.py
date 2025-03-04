#!/usr/bin/env python3

'''
Calculate Frequency - calculates different frequencies for word occurrences.
Usage:
    calc_occ.py options word files*  
    calc_occ.py files*  (apenas retorna o dicionário de ocorrências)
Options:
    -fa   absolute frequency  
    -fr   relative frequency  
    -fm   relative frequency per million  
    -log  logarithm of relative frequency  
'''

import sys
import math
import re


def calc_occ(files):
    """ Calcula a ocorrência de palavras nos arquivos de entrada """
    occor = {}

    for file in files:
        try:
            with open(file, "r", encoding="utf-8") as f:
                for line in f:
                    words = re.findall(r'\w+', line.lower()) 
                    for word in words:
                        occor[word] = occor.get(word, 0) + 1 
        except FileNotFoundError:
            print(f"Erro: Arquivo '{file}' não encontrado.")
            sys.exit(1)

    return occor

def calc_freq(word, occor, options):
    """ Calcula as frequências da palavra com base nas opções fornecidas """
    total_occ = sum(occor.values()) 
    word_occ = occor.get(word.lower(), 0) 

    if "-fa" in options:
        print(f"Frequência absoluta de '{word}': {word_occ}")

    if "-fr" in options:
        fr = (word_occ / total_occ) * 100 if total_occ > 0 else 0
        print(f"Frequência relativa de '{word}': {fr:.6f}%")

    if "-fm" in options:
        fm = (word_occ / total_occ) * 1_000_000 if total_occ > 0 else 0
        print(f"Frequência por milhão de '{word}': {fm:.2f} por milhão")

    if "-log" in options:
        log_fr = math.log(fr) if fr > 0 else float('-inf')  
        print(f"Logaritmo da frequência relativa de '{word}': {log_fr:.6f}")

def main():
    if len(sys.argv) < 2:
        print("Uso: python3 calc_occ.py [opções] [palavra] arquivos*")
        sys.exit(1)

    options = [arg for arg in sys.argv[1:] if arg.startswith("-")]  
    args = [arg for arg in sys.argv[1:] if not arg.startswith("-")]

    if options == [] and len(args) >= 1:
        occor = calc_occ(args) 
        print(occor)  
        return 

    if len(args) < 2:  
        print("Erro: Deve passar uma palavra e pelo menos um arquivo de entrada.")
        sys.exit(1)

    word = args[0]  
    files = args[1:] 

    occor = calc_occ(files) 
    calc_freq(word, occor, options) 

if __name__ == '__main__':
    main()