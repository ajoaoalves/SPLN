import subprocess
import os
import shlex
import time

HTML_DIR = "html"
INDEX_DIR = "glimpse_index"
GLIMPSEINDEX_CMD = "glimpseindex"
PRIORITY_FILE = "hierarquia.html"
TIMEOUT = 10  # Timeout de 10 segundos

def create_or_update_index():
    if not os.path.exists(HTML_DIR):
        raise FileNotFoundError(f"Diretório {HTML_DIR} não existe!")
    
    if os.path.exists(PRIORITY_FILE) and not os.path.exists(os.path.join(HTML_DIR, PRIORITY_FILE)):
        os.system(f"cp {PRIORITY_FILE} {HTML_DIR}/")
    
    print(f"Indexando {len(os.listdir(HTML_DIR))} arquivos...", end='', flush=True)
    start_time = time.time()
    
    cmd = f"{GLIMPSEINDEX_CMD} -H {INDEX_DIR} {HTML_DIR}"
    process = subprocess.run(
        shlex.split(cmd),
        capture_output=True,
        text=True
    )
    
    if process.returncode != 0:
        print("\nERRO na indexação:")
        print(process.stderr)
        exit(1)
    
    print(f" OK! ({time.time() - start_time:.2f}s)")

def search(query, use_priority=True):
    final_results = []  # Mantém a ordem
    seen = set()        # Evita duplicatas
    partial = False
    
    try:
        # Busca prioritária
        if use_priority and os.path.exists(os.path.join(HTML_DIR, PRIORITY_FILE)):
            cmd_priority = f"glimpse -H {INDEX_DIR} -i {shlex.quote(query)} -f {PRIORITY_FILE}"
            process = subprocess.Popen(
                shlex.split(cmd_priority),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            try:
                stdout, _ = process.communicate(timeout=TIMEOUT)
                if stdout:
                    for line in stdout.splitlines():
                        if line not in seen:
                            seen.add(line)
                            final_results.append(line)
            except subprocess.TimeoutExpired:
                partial = True
                process.kill()
                stdout, _ = process.communicate()
                if stdout:
                    for line in stdout.splitlines():
                        if line not in seen:
                            seen.add(line)
                            final_results.append(line)

        # Busca geral
        cmd_general = f"glimpse -H {INDEX_DIR} -i {shlex.quote(query)}"
        process = subprocess.Popen(
            shlex.split(cmd_general),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        try:
            stdout, _ = process.communicate(timeout=TIMEOUT)
            if stdout:
                for line in stdout.splitlines():
                    if line not in seen:
                        seen.add(line)
                        final_results.append(line)
        except subprocess.TimeoutExpired:
            partial = True
            process.kill()
            stdout, _ = process.communicate()
            if stdout:
                for line in stdout.splitlines():
                    if line not in seen:
                        seen.add(line)
                        final_results.append(line)

    except Exception as e:
        print(f"Erro na busca: {str(e)}")
        return None, False

    return "\n".join(final_results) if final_results else None, partial

def main():
    try:
        create_or_update_index()
    except Exception as e:
        print(f"Falha crítica: {str(e)}")
        exit(1)
    
    while True:
        query = input("\nBusca (ou 'sair'): ").strip()
        if query.lower() == "sair":
            break
        
        start_time = time.time()
        results, partial = search(query)
        status_msg = " (busca parcial)" if partial else ""
        
        
        unique_paths = []  # Armazena caminhos únicos
        if results:
            for line in results.splitlines():
                if ":" in line:
                    file_path = line.split(":")[0].strip()
                    relative_path = file_path.split("/html/")[-1]
                    full_path = f"/html/{relative_path}"
                    physical_path = os.path.join(HTML_DIR, relative_path)  
                    if os.path.exists(physical_path):  
                        if full_path not in unique_paths:
                            unique_paths.append(full_path)
            
            # Imprime todos os caminhos únicos
            for path in unique_paths:
                print(path)
            print(f"\nResultados ({len(unique_paths)} encontrados{status_msg} em {(time.time() - start_time):.2f}s):")
        else:
            print("Procura não encontrada")
        
        if results and partial: 
            for line in results.splitlines():
                # Extrai o ID (primeiro número antes do primeiro espaço ou '-')
                if line.strip():
                    parts = line.split()
                    if parts:  # Verifica se há elementos
                        doc_id = parts[0].strip()  # Pega o primeiro elemento (ID)
                        if doc_id.isdigit():  # Confirma se é um número
                            file_path = os.path.join(HTML_DIR, f"{doc_id}.html")
                            if os.path.exists(file_path): 
                                html_path = f"/html/{doc_id}.html"
                                if html_path not in unique_paths:
                                    unique_paths.append(html_path)

            
            # Imprime todos os caminhos únicos
            for path in unique_paths:
                print(path)
            if path: 
                print(f"\nResultados ({len(unique_paths)} encontrados{status_msg} em {(time.time() - start_time):.2f}s):")
            else: 
                print("Procura não encontrada")

if __name__ == "__main__":
    main()