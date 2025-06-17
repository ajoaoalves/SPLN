import re

def anota_entidades(texto, dicionario):
    
	def substitui_entidade(match):
		entidade = match.group(0)
		tipo = dicionario.get(entidade)
		if tipo:
			return f"<e t=\"{tipo}\">{entidade}</e>"
		return entidade

	regex = r'\b(?:' + '|'.join(re.escape(entidade) for entidade in dicionario.keys()) + r')\b'
	
	texto_anotado = re.sub(regex, substitui_entidade, texto)
	print("Texto anotado:", texto_anotado)
	
	return texto_anotado

texto = "Consta que Platão estudou em Miranda do Douro e Constantim" 
DE={ "Miranda do Douro": "cidade", "Platão": "filósofo", "Violeta Parra": "cantautor"}
anota_entidades(texto,DE)