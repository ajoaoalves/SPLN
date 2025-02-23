cat -> imprime um ficheiro de cima para baixo

cat f1 - f3 -> concatena o ficheiro f1 com o stard input com o ficheiro f3
ls -> mostra directoria

tac -> imprime um ficheiro de baixo para cima

seq 70 -> imprime os numeros de 1 a 70

shuf -> escrevemos as linhas e ele devolve-as de forma aleatoria

(seq 1000; seq 90 100) | shuf
(seq 1000; seq 90 100) | shuf | ./aula2.py > _
(seq 1000000; seq 90 100) | shuf | ./aula2.py > _
time (seq 1000000; seq 90 100) | shuf | ./aula2.py > _
time (seq 100; seq 90 100) | shuf | ./aula2.py > _

Os comandos geram sequências numéricas, embaralham os números (shuf), processam com o script aula2.py e salvam no arquivo _. O time mede o tempo de execução. A principal diferença entre eles é a quantidade de números gerados (100, 1000 ou 1 milhão).

# Aula 2 

## Temas 

- Cultura Geral de Lingua Natural 
- Scripting 
- Ferramentas 
    - Ligadas sempre que possivel a Python 


## 

#### Conversa sobre o tpc 

Em que e que vamos usar a script ?

"Em que e que isto vai contribuir para a nossa felicidade?"

### Filtros Unix 

grep 

rg (ripgrep)

## Comandos 

qualquer ficheiro '>' x ( guarda num ficheiro )

qualquer ficheiro '>>' x( da append ao ficheiro )

qualquer ficheiro '<' y ( ridereciona o stdin )

qualquer ficheiro '<<<' "batatas" ( mandar   )

c | c2, ridereciona o output c para a entrada de c2 

( c1 ; c2 ) Executar c1 a seguir de c2 no mesmo processo 

( c1 ; c2 ) | c3 , C3 recebe a saida de c1 e c2 

diff, ver as diferencas entre 2 ficheiros 



## Cultura geral de PLN 

Tartarugas vivem muito tempo ( Verdade )

98% das tartarugas morrem quando nascem ate ao mar ( Verdade )

As tartarugas vivem muito tempo ( verdae )

é implicito que as tartarugas morrerem nao é importante 


## Filtrologia 
pip install jjcli

## Afixos

- Afixos:
    - sufixo
    - prefixo
    - infixo

- Parasintese

# Derivação
semantica da palavra é alterada
por exmplo: fazer ---(prefixo r)---> refazer

# Flexão
cão -- (ão -> ães) -> cães 
Número N= singular passa para N=Plural
mantem a semantica

Analisador morfologico -> olhando para uma palavra podemos ver os atributos que conseguimos inferir de cada um delas 