import re
import jjcli
from collections import Counter

def lexer(txt):
    return re.findall(r'\w+(?:-\w+)*|[^\w\s]+',txt)

def pretty_print(freq, relative_freq,opt):
    if("-a" in opt):
        for word, count in freq.most_common():
            print(f"{word}    {count}")
    else:
        for word, count in relative_freq:
            print(f"{count:.2f}    {word}")

def ratio(relative_freq1, relative_freq2):
    result = []
    r2 = dict(relative_freq2)
    for word, count in relative_freq1:
        result[word] = count / r2.get(word,1/1000000)
    return result

def counter(freq_abs):
    total_freq_abs = sum(freq_abs.values())
    relative_freq = [(word, count/total_freq_abs*1000000) for word, count in freq_abs.most_common()]
    return relative_freq

def main():
    """
    Options:
        -a absolute frequencie
        -m 700 top 700 words (FIXME)
        -j json output (FIXME)

    """
    cl = jjcli.clfilter("am:",doc=main.__doc__)
    freq_abs = []
    for txt in cl.text():
        t = lexer(txt)
        freq_abs.extend(t)
    c = Counter(freq_abs)
    relative_frequencies= counter(c)
    pretty_print(c, relative_frequencies,cl.opt)

if __name__ == '__main__':
    main()
 
