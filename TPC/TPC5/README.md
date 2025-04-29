

## Objetivo

O código utiliza a biblioteca **Lark** para definir e processar uma gramática capaz de identificar e separar diferentes tipos de linhas dentro de um texto, especificamente:

- **Linhas contendo termos em Português e Tétun**
- **Descrições estruturadas nas duas linguas**
- **Linhas desconhecidas ou não categorizadas**

## Componentes do Código

### 1. Definição da Gramática

A gramática Lark especifica os diferentes padrões que podem ser encontrados no texto:
- `PAR_COM_PARENTESIS`: Expressões com traduções entre parênteses
- `PT_LINE`: Linhas que começam com "PORTUGUÊS:"
- `TETUN_LINE`: Linhas que começam com "TETUN:"
- `FIG_LINE`: Linhas que contêm referências a figuras
- `UNKNOWN_LINE`: Qualquer outra linha não classificada

### 2. Parser e Análise da Entrada

O código utiliza a classe `Lark` para processar o texto de entrada e gerar uma árvore sintática (`tree`). Essa árvore é então transformada usando a classe `T(Transformer)`, que reestrutura os dados em um formato mais acessível.

### 3. Extração de Dados

Os elementos extraídos são classificados em duas listas:
- `unknown`: Contém linhas que não foram reconhecidas por nenhum padrão definido na gramática.
- `dicionario`: Contém os termos e suas respectivas traduções ou explicações.

### 4. Armazenamento de Resultados

- As linhas não reconhecidas são gravadas em um ficheiro **unknown.txt**.
- O dicionário extraído é exibido no terminal usando a biblioteca **tabulate** para melhor visualização.

## Exemplo de Saída

Se o texto de entrada contém:
```
PORTUGUÊS: Localização de um ponto em relação ao eixo horizontal x.
TETUN: Fatin ba pontu sira-ne´ebé iha relasaun ho eixu orizontál.
Figura 1- Eixo X-Y com abscissas
```

O programa extrairia:
```
Dicionário:
---------------------------------
Português                         | Localização de um ponto em relação ao eixo horizontal x.
Tétun                              | Fatin ba pontu sira-ne´ebé iha relasaun ho eixu orizontál.
Figura                              | Figura 1- Eixo X-Y com abscissas
---------------------------------
```

## Bibliotecas Utilizadas

- **re**: Para manipulação de expressões regulares.
- **lark**: Para criar e processar a gramática personalizada.
- **tabulate**: Para formatar a saída do dicionário no terminal.

## Possíveis Melhorias

- **Melhoria na Gramática**: Refinar os padrões para capturar mais tipos de informação.
- **Exportação em Outros Formatos**: Gerar um ficheiro CSV ou JSON para facilitar a reutilização dos dados extraídos.
- **Interface Gráfica**: Criar uma interface para interagir com os dados extraídos de forma visual.

Este código é útil para processar listas de termos bilíngues e organizar glossários automaticamente.

