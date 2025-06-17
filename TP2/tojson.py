import xml.etree.ElementTree as ET
import json

data = []

tree = ET.parse('colecao.xml')
root = tree.getroot()

ns = {
    'oai': 'http://www.openarchives.org/OAI/2.0/',
    'dim': 'http://www.dspace.org/xmlns/dspace/dim'
}

# Para cada registo (record) no XML
for record in root.findall('.//oai:record', ns):
    file_info = {}
    dim = record.find('.//dim:dim', ns)
    if dim is None:
        continue
    fields = dim.findall('dim:field', ns)
    # Extrair keywords (subject)
    file_info["keywords"] = [f.text.strip() for f in fields if f.get('element') == 'subject' and f.text]
    # Extrair título
    file_info["titulo"] = next((f.text.strip() for f in fields if f.get('element') == 'title' and f.text), "")
    # Extrair autor
    file_info["autor"] = next((f.text.strip() for f in fields if f.get('element') == 'contributor' and f.get('qualifier') == 'author' and f.text), "")
    # Extrair data
    file_info["data"] = next((f.text.strip() for f in fields if f.get('element') == 'date' and f.text), "")
    # Extrair resumo (abstract)
    file_info["abstract"] = next((f.text.strip() for f in fields if f.get('element') == 'description' and f.get('qualifier') == 'abstract' and f.text), "")
    data.append(file_info)

with open('ColDoc.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)