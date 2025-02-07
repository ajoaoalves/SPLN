# Descrição do Código Python

Este código processa arquivos de texto (incluindo PDFs) e entrada padrão, removendo linhas duplicadas e preservando a ordem original. Ele pode ser executado em dois modos:
1. A partir de um arquivo fornecido como argumento na linha de comando.
2. A partir de dados inseridos diretamente pelo terminal.

## Funções

### 1. `read_pdf(file_path)`
- **Objetivo:** Ler um arquivo PDF e retornar uma lista de linhas extraídas.
- **Parâmetros:**
  - `file_path`: Caminho do arquivo PDF.
- **Como funciona:** 
  - Utiliza a biblioteca `fitz` para abrir o PDF e extrair o texto.
  - O texto extraído é dividido em linhas usando o caractere de nova linha (`\n`).

### 2. `read_generic_file(file_path)`
- **Objetivo:** Tenta ler qualquer arquivo como texto simples.
- **Parâmetros:**
  - `file_path`: Caminho do arquivo a ser lido.
- **Como funciona:**
  - O arquivo é aberto em modo leitura (`"r"`) com a codificação UTF-8.
  - Caso ocorra um erro de codificação (`UnicodeDecodeError`), uma mensagem de erro é exibida e o programa é encerrado.
  - Caso o arquivo não seja encontrado (`FileNotFoundError`), uma mensagem de erro é exibida e o programa é encerrado.
  
### 3. `read_stdin()`
- **Objetivo:** Ler entrada do terminal até o final (EOF).
- **Como funciona:**
  - Solicita ao usuário que insira texto até que o final da entrada seja indicado (Ctrl+D ou Ctrl+Z).

### 4. `remove_duplicates(lines)`
- **Objetivo:** Remover linhas duplicadas da lista fornecida, preservando a ordem original.
- **Parâmetros:**
  - `lines`: Lista de linhas a ser processada.
- **Como funciona:**
  - Cada linha é convertida para minúsculas e os espaços extras são removidos.
  - As linhas únicas são mantidas em uma lista, e as duplicadas são descartadas.

### 5. `process_file(file_path)`
- **Objetivo:** Processar o arquivo fornecido, removendo linhas duplicadas.
- **Parâmetros:**
  - `file_path`: Caminho do arquivo a ser processado.
- **Como funciona:**
  - Se o arquivo for um PDF (determinado pela extensão `.pdf`), a função `read_pdf` é chamada.
  - Caso contrário, a função `read_generic_file` é chamada para arquivos de texto simples.
  - Em seguida, as linhas do arquivo são processadas pela função `remove_duplicates`.

### 6. `main()`
- **Objetivo:** Função principal que orquestra a execução do programa.
- **Como funciona:**
  - O programa verifica os argumentos passados na linha de comando:
    - Se houver exatamente um argumento (o caminho do arquivo), o programa processa o arquivo fornecido.
    - Se não houver argumentos (somente o script é chamado), ele lê a entrada padrão (dados inseridos no terminal).
    - Se houver mais de um argumento ou nenhum, o programa exibe uma mensagem de uso e encerra.
  - O resultado final (as linhas únicas) é impresso no terminal (stdout).

## Execução

### Execução a partir de um arquivo:
```bash
python script.py arquivo.txt
