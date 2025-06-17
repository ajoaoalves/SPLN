### Aula5: 25 - 03 - 18 
---

Esta aula foi usado o requests e o beautifulsoup bs4

Web scraping
```
www       --->      html        --->        DT (document tree)
        - wget              - parsertHTML           <-> ações
        - curl              - parserXML                 - procurar elementos
        - requests                                     - aceder portas
```
parsertHTML: pydt, lxml, bs4

ajax: sellenium 

---

### proc-jonsay-co.uk.py 

```
python3 proc-jonsay-co.uk.py > _
```
---

Usar cache
```
para não ser banido do site
```
### extrai_tab.py

"url"

Não funciona para tabelas dentro de tabelas

```
python3 extrai_tab.py "https://www.jonsay.co.uk/dictionary.php?langa=German&langb=Polish&category=vegetables" > _1
```

Com separador
```
python3 extrai_tab.py "https://www.jonsay.co.uk/dictionary.php?langa=German&langb=Polish&category=vegetables" -s "  ::::  "
```

```
https://natura.di.uminho.pt/~jj/bs4/
https://natura.di.uminho.pt/~jj/bs4/folha8-2023/27-05-77-80-mil-assassinatos/
```

1. Buscar article que tem a class post e id = post e número
2. buscar aos metas do head - e outras coisas que pareçam civilizadas
3. save do artigo e gravar em post 7592  
