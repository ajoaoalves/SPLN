import re
import jjcli
from collections import Counter
from ftk.base import lexer, pretty_print

def ratio(relative_freq1, relative_freq2):
    result = []
    r2 = dict(relative_freq2)
    for word, count in relative_freq1:
        result[word] = count / r2.get(word,1/1000000)
    return result

def main():
    cl = jjcli.clfilter("am:",doc=main.__doc__)
    tokens1 = []
    tokens2 = []

    for cl in cl.args:
        for txt in cl.txt:
            t = lexer(txt)
            tokens1.extend(t)


    c1 = Counter(tokens1)
    c2 = Counter(tokens2)

    relative_frequencies1 = counter(c1)
    relative_frequencies2 = counter(c2)

if __name__ == '__main__':
    main()
 
