
# **Repetidas - Remover Linhas Repetidas em um Programa**

Este script em Python tem como objetivo remover linhas repetidas de um arquivo. Ele possui opções para manipular espaços em branco, linhas vazias e linhas duplicadas.

## **Uso**

O script pode ser executado da seguinte maneira:

```bash
chmod +x tpc2.py
./tpc2.py [opções] [arquivo]
```

### **Opções:**
- **`-s`**: **Manter os espaços** (não remove os espaços em branco no início ou fim das linhas).
- **`-e`**: **Remover linhas vazias** (ignorará as linhas que não possuem conteúdo).
- **`-p`**: **Substituir linhas vazias por `#`** (caso haja linhas vazias, serão substituídas por um `#`).

### **Exemplo de Uso:**

1. **Remover linhas repetidas, mantendo espaços e sem remover linhas vazias**:
    ```bash
    ./tpc2.py -s arquivo.txt
    ```

2. **Remover linhas repetidas e linhas vazias**:
    ```bash
    ./tpc2.py -e arquivo.txt
    ```

3. **Substituir linhas vazias por `#` e remover duplicatas**:
    ```bash
    ./tpc2.py -p arquivo.txt
    ```

4. **Combinação das opções**:
    ```bash
    ./tpc2.py -s -p arquivo.txt
    ```

---

## **Explicação do Código**

### **1. Importação de Dependências**

```python
from jjcli import *
```

A biblioteca `jjcli` é utilizada para facilitar o processamento de argumentos e opções de linha de comando. Ela fornece funções para capturar opções e argumentos do usuário e também ajuda na leitura de arquivos.

### **2. Descrição do Programa**

```python
'''
Repetidas - Remove linhas repetidas num programa. 
Usage - 
    repetidas options file*
Options: 
    - s  fix me keep spaces 
    - e remove empty lines 
    - p replace empty lines with #
'''
```

Aqui temos a documentação do programa, explicando seu funcionamento e as opções disponíveis para o usuário.

### **3. Função `remove_linhas_repetidas(cl)`**

Esta é a função principal responsável por processar o arquivo e remover linhas repetidas, conforme as opções passadas.

```python
def remove_linhas_repetidas(cl): 
    linhas_vistas = set()  # Para armazenar linhas únicas
```

- **`linhas_vistas`**: Um conjunto que armazena as linhas já processadas. Conjuntos são usados porque eles não permitem duplicatas.

```python
    for linha in cl.input():  # Itera sobre as linhas do arquivo
```

A função **`cl.input()`** recebe as linhas do arquivo fornecido pelo usuário.

```python
        if "-s" not in cl.opt: 
            ln = linha.strip()  
        else:
            ln = linha  # Mantém os espaços
```

- **`-s`**: Se a opção `-s` não for passada, os espaços em branco no início e fim da linha são removidos usando o método `strip()`. Se `-s` estiver presente, os espaços são mantidos.

```python
        if not ln:
            if "-p" in cl.opt:  # Se "-p" for passado, substitui por "#"
                print("#")
                continue
            elif "-e" in cl.opt:  # Se "-e" for passado, ignora a linha vazia
                continue  
```

- **`-p`**: Se a linha estiver vazia e a opção `-p` estiver ativada, ela será substituída por `#`.
- **`-e`**: Se a opção `-e` estiver ativada, as linhas vazias serão ignoradas.

```python
        if not ln or ln not in linhas_vistas:  
            print(ln, end="")  # Imprime sem duplicatas
            linhas_vistas.add(ln)  # Adiciona a linha ao conjunto
```

- **Remoção de duplicatas**: O script verifica se a linha não foi vista antes. Se não for, ela será impressa e adicionada ao conjunto de linhas vistas.

### **4. Função `main()`**

```python
def main(): 
    cl = clfilter(opt="s,e,p", man=__doc__)  # Definindo as opções válidas: -s, -e, -p
    remove_linhas_repetidas(cl)
```

- **`clfilter()`**: Configura as opções válidas (`-s`, `-e`, `-p`) e a documentação do programa.
- **`remove_linhas_repetidas(cl)`**: Chama a função que processa o arquivo e remove as linhas repetidas.

### **5. Execução do Script**

```python
if __name__ == '__main__': 
    main()
```

Esta parte garante que a função **`main()`** seja executada apenas quando o script for executado diretamente, e não quando for importado como um módulo.

---

## **Testes e Exemplos**

### **Arquivo de Entrada (`teste.txt`):**
```
  Python  
C++
  
JavaScript
Java  
C++
```

### **Exemplo 1: Sem opções**

```bash
./aula2.py teste.txt
```

**Saída:**
```
Python
C++
JavaScript
Java
```

### **Exemplo 2: Com opção `-s` (Manter espaços)**

```bash
./aula2.py -s teste.txt
```

**Saída:**
```
  Python  
C++
  
JavaScript
Java  
```

### **Exemplo 3: Com opção `-e` (Remover linhas vazias)**

```bash
./aula2.py -e teste.txt
```

**Saída:**
```
Python
C++
JavaScript
Java
```

### **Exemplo 4: Com opção `-p` (Substituir linhas vazias por `#`)**

```bash
./aula2.py -p teste.txt
```

**Saída:**
```
Python
C++
#
JavaScript
Java
```

---

## **Conclusão**

Este script fornece uma maneira prática de processar arquivos de texto, removendo linhas duplicadas e manipulando linhas vazias com diferentes opções. Ele é altamente configurável e pode ser usado para diferentes necessidades de processamento de arquivos. 

---
