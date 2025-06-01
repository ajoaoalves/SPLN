# TPC6 - Scraper de Artigos do Natura

Este script (`natura.py`) faz scraping de artigos do site Natura da Universidade do Minho, guardando a informação relevante de cada artigo em ficheiros de texto individuais.

## O que faz o script?

- **Acede à página principal** do Natura (folha8-2023).
- **Percorre as tabelas** da página para encontrar links para artigos e subdiretórios.
- Para cada artigo encontrado:
  - Faz download da página do artigo (usando cache local para evitar downloads repetidos).
  - Extrai o título, autor, data de publicação e conteúdo do artigo.
  - Guarda esta informação num ficheiro de texto com o nome igual ao ID do artigo.
- Se encontrar subdiretórios (ex: "dd/"), entra nesses diretórios e repete o processo para os artigos lá presentes.
- Usa o ficheiro `pagecache.db` para guardar páginas já descarregadas, tornando o scraping mais eficiente.

## Estrutura dos ficheiros gerados

- Para cada artigo, é criado um ficheiro `<id>.txt` com:
  - Título
  - Autor
  - Data de publicação (formato: "dia de mês de ano, hora:minuto")
  - Conteúdo do artigo

## Requisitos

- Python 3
- Bibliotecas: `requests`, `bs4` (BeautifulSoup), `shelve`, `dateutil`, `locale`, `re`

## Como usar

1. Certifique-se de que tem as bibliotecas necessárias instaladas: pip install requests beautifulsoup4 python-dateutil


