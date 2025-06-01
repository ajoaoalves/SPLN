# TPC7 - Análise de Texto de Harry Potter com Word Embeddings

Este notebook (`harrypotter.ipynb`) realiza uma análise de linguagem natural sobre o livro "Harry Potter" em PDF, utilizando técnicas de processamento de texto e modelos de Word Embeddings (Word2Vec).

## O que o notebook faz?

1. **Instalação e importação de bibliotecas**  
   Utiliza bibliotecas como `pdfplumber` para extrair texto do PDF, `nltk` para tokenização e `gensim` para treinar e manipular modelos Word2Vec.

2. **Extração do texto do PDF**  
   Lê o ficheiro `Harry-Potter.pdf` e extrai todo o texto.

3. **Pré-processamento do texto**  
   - Tokeniza o texto em frases e palavras.
   - Converte tudo para minúsculas.

4. **Treino de um modelo Word2Vec**  
   Treina um modelo de embeddings de palavras com o texto extraído, permitindo analisar relações semânticas entre palavras do universo Harry Potter.

5. **Exploração do modelo**  
   - Consulta vetores de palavras.
   - Procura palavras mais semelhantes (`most_similar`).
   - Calcula similaridade entre pares de palavras.
   - Descobre a palavra "menos relacionada" num grupo (`doesnt_match`).
   - Realiza analogias do tipo "A está para B assim como C está para ?".

6. **Visualização**  
   - Reduz a dimensionalidade dos vetores para 2D usando PCA ou t-SNE.
   - Plota as palavras escolhidas para visualizar relações semânticas.

7. **Guardar e carregar modelos**  
   - Guarda o modelo treinado e os vetores em ficheiros para uso posterior.

## Estrutura dos ficheiros

- `Harry-Potter.pdf`: Livro usado como fonte de texto.
- `harrypotter.ipynb`: Notebook com todo o processamento, treino e análise.
- `models/`: Pasta onde são guardados os modelos treinados e os vetores.

## Requisitos

- Python 3
- Bibliotecas: `pdfplumber`, `gensim`, `nltk`, `matplotlib`, `scikit-learn`

## Como usar

1. Certifique-se de que o ficheiro `Harry-Potter.pdf` está na mesma pasta do notebook.
2. Execute as células do notebook sequencialmente.
3. Explore as relações semânticas entre palavras do universo Harry Potter!

---