import os
from bs4 import BeautifulSoup

def parse_hierarchy(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    hierarchy = []
    stack = []

    for line in lines:
        level = len(line) - len(line.lstrip())
        content = line.strip()

        while stack and stack[-1][1] >= level:
            stack.pop()

        node = {"content": content, "children": []}
        if stack:
            stack[-1][0]["children"].append(node)
        else:
            hierarchy.append(node)

        stack.append((node, level))

    return hierarchy


def generate_html(hierarchy, output_dir='html'):
    """
    Gera o HTML da hierarquia principal com o mesmo estilo das páginas filhas
    """
    # Criar estrutura base da página
    soup = BeautifulSoup('<!DOCTYPE html>', 'html.parser')
    html = soup.new_tag('html')
    soup.append(html)
    
    # Head com metadados e estilos
    head = soup.new_tag('head')
    html.append(head)
    
    # Meta tags
    meta_charset = soup.new_tag('meta')
    meta_charset['charset'] = "utf-8"
    head.append(meta_charset)
    
    meta_viewport = soup.new_tag('meta')
    meta_viewport['name'] = "viewport"
    meta_viewport['content'] = "width=device-width, initial-scale=1"
    head.append(meta_viewport)
    
    # Título da página
    title = soup.new_tag('title')
    title.string = "Estrutura Hierárquica - Arquivo Municipal"
    head.append(title)
    
    # Estilos CSS (mesmo estilo das páginas filhas)
    style = soup.new_tag('style')
    style.string = """
    body { 
        font-family: 'Segoe UI', Arial, sans-serif; 
        line-height: 1.6; 
        margin: 0; 
        padding: 20px; 
        background: #f5f5f5; 
    }
    .container { 
        max-width: 1000px; 
        margin: 0 auto; 
        background: white; 
        padding: 30px; 
        border-radius: 8px; 
        box-shadow: 0 2px 4px rgba(0,0,0,0.1); 
    }
    h1 {
        color: #2c3e50;
        border-bottom: 2px solid #3498db;
        padding-bottom: 10px;
        margin-top: 0;
    }
    ul {
        list-style-type: none;
        padding-left: 20px;
    }
    li {
        margin: 10px 0;
        position: relative;
    }
    li a {
        color: #3498db;
        text-decoration: none;
        transition: color 0.3s;
    }
    li a:hover {
        color: #2980b9;
    }
    .tree-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 25px;
    }
    """
    head.append(style)
    
    # Corpo do documento
    body = soup.new_tag('body')
    html.append(body)
    
    # Container principal
    container = soup.new_tag('div', **{'class': 'container'})
    body.append(container)
    
    # Cabeçalho
    header = soup.new_tag('div', **{'class': 'tree-header'})
    container.append(header)
    
    # Título principal
    h1 = soup.new_tag('h1')
    h1.string = "Estrutura Hierárquica "
    header.append(h1)
    
    # Função recursiva para construir a lista
    def build_tree(nodes, parent):
        ul = soup.new_tag('ul')
        for node in nodes:
            li = soup.new_tag('li')
            if not node["children"]:  # Nó folha
                a = soup.new_tag('a', href=f"html/{node['content'].split()[0]}.html")
                a.string = node['content']
                li.append(a)
            else:
                span = soup.new_tag('span', style="font-weight: 600; color: #34495e;")
                span.string = node['content']
                li.append(span)
                build_tree(node["children"], li)
            ul.append(li)
        parent.append(ul)
    
    # Construir a árvore hierárquica
    build_tree(hierarchy, container)
    
    return soup.prettify()


def find_leaf_nodes(hierarchy):
    """
    Encontra todos os nós folha (nós que não possuem filhos) na hierarquia.
    """
    leaf_nodes = []

    for node in hierarchy:
        if not node["children"]:  # Se o nó não possui filhos, é uma folha
            leaf_nodes.append(node["content"])
        else:
            # Busca recursiva nos filhos
            leaf_nodes.extend(find_leaf_nodes(node["children"]))

    return leaf_nodes


def generate_node_page(node_data, output_dir='html'):
    """
    Gera uma página HTML para um nó específico com formatação profissional.
    """
    try:
        # Parse do conteúdo XML
        soup_content = BeautifulSoup(node_data['content'], 'xml')
        desc_item = soup_content.find('DescriptionItem')
        
        # Criar estrutura base da página
        soup = BeautifulSoup('<!DOCTYPE html>', 'html.parser')
        html = soup.new_tag('html')
        soup.append(html)
        
        # Head com metadados e estilos
        head = soup.new_tag('head')
        html.append(head)
        
        # Meta tags (forma correta)
        meta_charset = soup.new_tag('meta')
        meta_charset['charset'] = "utf-8"
        head.append(meta_charset)
        
        meta_viewport = soup.new_tag('meta')
        meta_viewport['name'] = "viewport"
        meta_viewport['content'] = "width=device-width, initial-scale=1"
        head.append(meta_viewport)
        
        # Título da página (com verificação de segurança)
        title = soup.new_tag('title')
        unit_title = desc_item.find('UnitTitle').text if desc_item.find('UnitTitle') else 'Sem título'
        process_id = desc_item.find('ID').text if desc_item.find('ID') else 'Sem ID'
        title.string = f"Processo {process_id} - {unit_title}"
        head.append(title)
        
        # Estilos CSS (mantido igual)
        style = soup.new_tag('style')
        style.string = """
        body { font-family: 'Segoe UI', Arial, sans-serif; line-height: 1.6; margin: 0; padding: 20px; background: #f5f5f5; }
        .container { max-width: 1000px; margin: 0 auto; background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        h1 { color: #2c3e50; border-bottom: 2px solid #3498db; padding-bottom: 10px; }
        .metadata-section { margin: 25px 0; }
        .metadata-item { display: grid; grid-template-columns: 200px 1fr; margin: 10px 0; }
        .metadata-label { font-weight: 600; color: #34495e; }
        .metadata-value { color: #2c3e50; }
        .back-link { display: inline-block; margin-bottom: 25px; color: #3498db; text-decoration: none; }
        .xml-source { margin-top: 40px; padding: 15px; background: #f8f9fa; border-radius: 4px; }
        """
        head.append(style)
        
        # Corpo do documento
        body = soup.new_tag('body')
        html.append(body)
        
        # Container principal
        container = soup.new_tag('div', **{'class': 'container'})
        body.append(container)
        
        # Link de voltar
        back_link = soup.new_tag('a', href='../hierarquia.html', **{'class': 'back-link'})
        back_link.string = '← Voltar à estrutura principal'
        container.append(back_link)
        
        # Cabeçalho
        header = soup.new_tag('div')
        container.append(header)
        
        # Título principal (com verificação)
        h1 = soup.new_tag('h1')
        h1.string = f"{unit_title} ({process_id})"
        header.append(h1)
        
        # Seção de metadados principais (com tratamento para datas)
        main_section = soup.new_tag('div', **{'class': 'metadata-section'})
        container.append(main_section)
        
        # Função auxiliar para extração segura de dados
        def get_xml_text(element, default="N/A"):
            return element.text if element else default
        

        def get_valid_xml_text(element, default=None):
            if element and element.text.strip():
                return element.text.strip()
            return default
        

        # Mapeamento de campos
        metadata_fields = {
            'Descrição': ('UnitTitle', None),
            'Código de Referência': ('CompleteUntid', None),
           'Datas': (
                lambda: f"{get_valid_xml_text(desc_item.find('UnitDateInitial')) or '?'} - {get_valid_xml_text(desc_item.find('UnitDateFinal')) or '?'}",
                None
            ),
            'Nível de Descrição': ('DescriptionLevel', None),
            'Dimensão': ('Dimensions', None),
            'Suporte': ('PhysTech', lambda x: x if x not in ['N/A', '?'] else None),
            'Conteudo' : ('ScopeContent', None), 
            'Localização Física': ('PhysLoc', None),
            'Biografia': ('BiogHist', None),
            'Restrições de Acesso': ('AccessRestrict', None)
        }
        
        # Construção dinâmica dos campos
        for label, (field, processor) in metadata_fields.items():
            div = soup.new_tag('div', **{'class': 'metadata-item'})
            
            span_label = soup.new_tag('span', **{'class': 'metadata-label'})
            span_label.string = f"{label}:"
            div.append(span_label)
            
            span_value = soup.new_tag('span', **{'class': 'metadata-value'})
            
            if callable(field):
                span_value.string = field()
            else:
                value = get_xml_text(desc_item.find(field))
                span_value.string = processor(value) if processor else value
            
            div.append(span_value)
            main_section.append(div)
    
        # Seção de metadados adicionais
        additional_section = soup.new_tag('div', **{'class': 'metadata-section'})
        container.append(additional_section)

        h2 = soup.new_tag('h2')
        h2.string = 'Informações Adicionais'
        additional_section.append(h2)

        # Campos adicionais
        additional_fields = ['Repository', 'LangMaterial', 'UseRestrict', 'IdentifierUrl']

        for field in additional_fields:
            div = soup.new_tag('div', **{'class': 'metadata-item'})

            span_label = soup.new_tag('span', **{'class': 'metadata-label'})
            span_label.string = f"{field}:"
            div.append(span_label)

            span_value = soup.new_tag('span', **{'class': 'metadata-value'})
            value = desc_item.find(field)

            if value and field == 'IdentifierUrl':
                link = soup.new_tag('a', href=value.text)
                link.string = value.text
                span_value.append(link)
            else:
                span_value.string = value.text if value else "N/A"

            div.append(span_value)
            additional_section.append(div)

    # Salvar arquivo
        os.makedirs(output_dir, exist_ok=True)
        html_filename = f"{node_data['id']}.html"

        with open(os.path.join(output_dir, html_filename), 'w', encoding='utf-8') as f:
            f.write(soup.prettify())

        print(f"Página HTML gerada: {html_filename}")
        return html_filename
        
    except Exception as e:
        print(f"Erro ao gerar página para {node_data.get('id', 'ID desconhecido')}: {str(e)}")
        return None


def process_leaf_nodes(hierarchy, records_dir, output_dir='html'):
    """
    Processa os nós folha da hierarquia e gera páginas HTML para cada um.
    """
    # Criar um mapeamento de arquivos na pasta records para otimizar a busca
    record_files = {}
    for filename in os.listdir(records_dir):
        if filename.endswith('.xml'):
            # Extrair o ID do formato oai_PT_MVNF_<id>.xml
            file_id = filename.split('_')[-1].split('.')[0]
            record_files[file_id] = filename

    print(f"Arquivos encontrados na pasta records: {record_files.keys()}")

    leaf_nodes = find_leaf_nodes(hierarchy)
    print(f"Nós folha encontrados: {leaf_nodes}")

    for leaf in leaf_nodes:
        # Extrair o número inicial do nó folha (ex.: "29561" de "29561 - D - Bilhete-postal")
        leaf_id = leaf.split(' ')[0]

        if leaf_id in record_files:  # Verifica se o ID do nó está no mapeamento
            file_path = os.path.join(records_dir, record_files[leaf_id])
            
            # Ler os dados do arquivo (exemplo: texto simples)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Criar os dados do nó
            node_data = {
                'id': leaf_id,
                'title': leaf,
                'content': content
            }
            
            # Gerar a página HTML
            generate_node_page(node_data, output_dir)
        else:
            print(f"Arquivo não encontrado para o nó folha: {leaf}")


def main():
    input_file = "hierarquia.txt"
    output_file = "hierarquia.html"
    records_dir = "records"
    output_dir = "html"

    # Gerar a hierarquia
    hierarchy = parse_hierarchy(input_file)
    
    # Gerar o HTML da hierarquia principal
    html_content = "<!DOCTYPE html>\n<html>\n<head>\n<title>Hierarquia</title>\n</head>\n<body>\n"
    html_content += generate_html(hierarchy, output_dir)
    html_content += "</body>\n</html>"

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(html_content)
    print(f"Arquivo hierarquia.html gerado em: {output_file}")
    
    # Processar os nós folha e gerar páginas HTML
    process_leaf_nodes(hierarchy, records_dir, output_dir)


if __name__ == "__main__":
    main()