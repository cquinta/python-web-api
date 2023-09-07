# carregar os dados

dados = [{"nome": "João", "cidade" : "São Paulo"},
         {"nome": "Maria", "cidade": "Rio de Janeiro"}
]


# processar

template = """\
<html>
<body>
<ul>
    <li>Nome: {dados[nome]}</li>  
    <li>Cidade: {dados[cidade]}</li>
</ul>
</body>
</html>
"""

# renderizar

for item in dados:
    print(template.format(dados=item))
