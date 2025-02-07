import fitz  # PDFs
import sys

def read_pdf(file_path):
    """Lê um PDF e retorna uma lista de linhas extraídas."""
    doc = fitz.open(file_path)
    lines = []
    for page in doc:
        lines.extend(page.get_text("text").split("\n"))
    return lines

def read_generic_file(file_path):
    """Tenta ler qualquer arquivo como texto."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.readlines()
    except UnicodeDecodeError:
        print(f"Erro: O arquivo '{file_path}' não é um arquivo de texto legível.")
        sys.exit(1)
    except FileNotFoundError:
        print(f"Erro: O arquivo '{file_path}' não foi encontrado.")
        sys.exit(1)

def read_stdin():
    """Lê entrada do terminal até EOF (Ctrl+D ou Ctrl+Z)."""
    print("Insira o texto (Ctrl+D para finalizar):")
    return sys.stdin.read().split("\n")

def remove_duplicates(lines):
    """Remove linhas duplicadas preservando a ordem original."""
    seen = set()
    unique_lines = []
    for line in lines:
        normalized_line = line.lower().strip()
        if normalized_line and normalized_line not in seen:
            seen.add(normalized_line)
            unique_lines.append(line)
    return unique_lines

def process_file(file_path):
    """Processa um arquivo de qualquer tipo, removendo linhas duplicadas."""
    if file_path.lower().endswith(".pdf"):
        lines = read_pdf(file_path)
    else:
        lines = read_generic_file(file_path)

    return remove_duplicates(lines)

def main():
    args = sys.argv
    if len(args) == 2:  
        input_file = args[1]
        unique_lines = process_file(input_file)
    elif len(args) == 1:  
        unique_lines = remove_duplicates(read_stdin())
    else:
        print("Uso: python script.py entrada [ficheiro]")
        sys.exit(1)

    # Escreve no stdout
    sys.stdout.write("\n".join(unique_lines) + "\n")

if __name__ == "__main__":
    main()
