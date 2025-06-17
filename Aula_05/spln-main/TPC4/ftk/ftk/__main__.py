import jjcli
import json
from base import Pipeline, Convert2ProbabilityStage
from probability import RelativeProbabilityPerMillion
from corpus import get_dictionary

def pretty_print(freqs, opts):
    freqs = dict(sorted(freqs.items(), key=lambda item: item[1].value, reverse=True))
    total = freqs[list(freqs.keys())[0]].total

    if '-a' not in opts:
        freqs = {key: RelativeProbabilityPerMillion(val) for key, val in freqs.items()}

    if '-m' in opts:
        m = int(opts['-m'])
        freqs = dict(list(freqs.items())[:m])

    freqs = {key: val.value for key, val in freqs.items()}
    if '-j' in opts:
        print(json.dumps({'total': total, 'words': freqs}, indent=4))
    else:
        print(total)
        for key, val in freqs.items():
            print(f'{val}\t{key}')

def main_surpresa():
    """
    Opções:
      -l: language filter(default PT)
    """
    cl = jjcli.clfilter("l:", doc=main_surpresa.__doc__) 

    dic_geral = get_dictionary(cl.opt.get('-l', 'pt'))

    pipe = Pipeline()
    pipe.set_reduction(Convert2ProbabilityStage())

    for word in cl.text():
        txt_abs_freq= pipe.apply(txt)

        racios = []
        for word, freq in txt_abs_freq.items():
            if word not in dic_geral:
                print(word,freq, 2)
            else: 
                racios.append((freq/dic_geral.get(word,), word))
        print(sorted(racios))


def main():
    """Options:
        -a: aboslute frequency
        -m N: top N words
        -j: JSON output
    """

    cl = jjcli.clfilter("am:j", doc=main.__doc__)
    pipe = Pipeline()
    pipe.set_reduction(Convert2ProbabilityStage())

    for txt in cl.text():
        c = pipe.apply(txt)
        pretty_print(c, cl.opt)


if __name__ == '__main__':
    main()

