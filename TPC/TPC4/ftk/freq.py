import re
import jjcli
from collections import Counter
from ftk.base import lexer, pretty_print, counter

def ratio(relative_freq1, relative_freq2):
    result = {}
    r2 = dict(relative_freq2)
    for word, count in relative_freq1:
        result[word] = count / r2.get(word, 1/1000000)
    return result

def main():
    """
    ftk-ratio
    """
    cl = jjcli.clfilter("am:", doc=main.__doc__)
    tokens1 = []
    tokens2 = []
    for i, arg in enumerate(cl.args):
        with open(arg, 'r') as file:
            txt = file.read()
            t = lexer(txt)
            if i == 0:
                tokens1.extend(t)
            else:
                tokens2.extend(t)
    c1 = Counter(tokens1)
    c2 = Counter(tokens2)
    
    relative_frequencies1 = counter(c1)
    relative_frequencies2 = counter(c2)
    
    ratio_frequencies = ratio(relative_frequencies1, relative_frequencies2)
    
    print(ratio_frequencies)
    
        
if __name__ == "__main__":
    main()
