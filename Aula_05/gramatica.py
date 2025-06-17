from lark import Lark, Transformer, v_args

gramatica = r'''
start: (PAR_COM_PARENTESIS|PT_LINE|TETUN_LINE|FIG_LINE|UNKNOWN_LINE)+

PAR_COM_PARENTESIS : /(\b\w+\b )+\(.+\)/
PT_LINE: /PORTUGUÊS: .*/
TETUN_LINE: /TETUN: .*/
FIG_LINE: /Figura \d+\- (\b\w+\b )+\(.+\)/
UNKNOWN_LINE: /.+/

%import common.WS
%ignore WS
'''

ex= r'''
Bissetriz de um Ângulo (Bisetriz Hosi Sikun Ida) ...................................................................... 33
Cálculo (Kálkulu / Sura) ............................................................................................................. 34
Cateto (Katetu) ............................................................................................................................ 34
Cateto Adjacente (Katetu Adjasente) .......................................................................................... 34
Cateto Oposto (Katetu Opostu) ................................................................................................... 35


Figura 7 - Ângulo Obtuso (Sikun Obtuzu)

Ângulo Reto (Sikun Siku)
PORTUGUÊS: Ângulo com valor igual à 90º (noventa graus). Exemplo: Ver em
TETUN.
TETUN: Sikun ho valór hanesan 90 º (grau sianulu). Ezemplu:

Figura 8 - Ângulo Reto (Sikun Siku)

Ângulo Suplementar (Sikun Suplementár)
PORTUGUÊS: Ângulo cuja soma com outro é igual a 180º (cento e oitenta graus).
Exemplo: Ver em TETUN.
TETUN: Sikun ne´ebé tau tan sikun seluk hanesan 1800 (grau Atus ida ualunulu).
Ezemplu:

Figura 9 - Ângulo Suplementar (Sikun Suplementár)
𝛼 + 30º = 180º → 𝛼 = 150º
Ângulo Suplementar igual a 150º (cento e cinquenta graus).
Sikun Suplementár hanesan 150º (grau atus ida limanulu).
25' \
'''

processador = Lark(gramatica, parser='lalr')
tree = processador.parse(ex)

print(tree.pretty())

@v_args(inline=True)
class T(Transformer):
    def start(self,*t):
        return t

    def PAR_COM_PARENTESIS(self,t): return ('par', re.split(r' *[\\](t.value.split('()'))

    def PT_LINE(self,t):
 2
    def TETUN_LINE(self,t):

    def FIG_LINE(self,t):

    def UNKNOWN_LINE(self,t):

arvore = (T().transform(tree))

for e in arvore:
    print(e)