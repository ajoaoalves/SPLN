import requests
from lxml import etree
import time
import os
import re

def harvest_aif_records(output_dir='records'):
    base_url = 'https://arquivo.cmpb.pt/OAI-PMH'
    params = {
        'verb': 'ListRecords',
        'metadataPrefix': 'AIF'
    }
    
    ns = {'oai': 'http://www.openarchives.org/OAI/2.0/'}
    
    # Criar diretório se não existir
    os.makedirs(output_dir, exist_ok=True)
    
    while True:
        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            root = etree.fromstring(response.content)

            # Processar cada registro
            records = root.xpath('//oai:record', namespaces=ns)
            for record in records:
                # Criar cópia do registro
                record_copy = etree.fromstring(etree.tostring(record))
                
                # Extrair identificador
                identifier = record_copy.xpath('.//oai:identifier/text()', namespaces=ns)[0].strip()
                
                # Sanitizar nome do arquivo
                sanitized_id = re.sub(r'[^\w\-_.]', '_', identifier)
                file_path = os.path.join(output_dir, f'{sanitized_id}.xml')
                
                # Criar estrutura XML completa para o registro
                new_root = etree.Element('{http://www.openarchives.org/OAI/2.0/}OAI-PMH')
                list_records = etree.SubElement(new_root, '{http://www.openarchives.org/OAI/2.0/}ListRecords')
                list_records.append(record_copy)
                
                # Escrever arquivo
                tree = etree.ElementTree(new_root)
                tree.write(file_path, 
                         pretty_print=True, 
                         xml_declaration=True, 
                         encoding='UTF-8')

            # Verificar token de continuação
            token = root.xpath('//oai:resumptionToken/text()', namespaces=ns)
            if not token:
                break
                
            params = {'verb': 'ListRecords', 'resumptionToken': token[0]}
            time.sleep(1)

        except Exception as e:
            #print(f"Erro: {e}")
            break

if __name__ == '__main__':
    harvest_aif_records()
    print("Todos os registros foram guardados na pasta 'records'")