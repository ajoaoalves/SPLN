import re
import jjcli

def lexer(txt):
    return re.findall(r'\w+(-\w+)*|[^\w\s]+',txt) #FIXME patterns stopwords lems 

def main():
    cl = jjcli.clfilter()
    for txt in cl.text():
        print(lexer(txt))