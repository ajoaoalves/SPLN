import requests
import xml.etree.ElementTree as ET

url = "https://repositorium.sdum.uminho.pt/oai/oai"
col = "col_1822_21316"  # Coleção: MSc Tese DI

records = []

for n in range(0, 1000, 100):  # Ajuste o limite conforme necessário
    params = {
        "verb": "ListRecords",
        "resumptionToken": f"dim///{col}/{n}"
    }
    r = requests.get(url, params=params).text

    if "noRecordsMatch" in r:
        break

    try:
        root = ET.fromstring(r)
        list_records = root.find("{http://www.openarchives.org/OAI/2.0/}ListRecords")
        if list_records is not None:
            for record in list_records.findall("{http://www.openarchives.org/OAI/2.0/}record"):
                records.append(record)
    except ET.ParseError as e:
        print(f"Erro ao processar XML no ciclo {n}: {e}")
        continue

# Criar documento final bem-formado
root = ET.Element("root")
for rec in records:
    root.append(rec)

tree = ET.ElementTree(root)
tree.write("colecao.xml", encoding="utf-8", xml_declaration=True)

print("Coleção extraída e guardada em colecao.xml")
