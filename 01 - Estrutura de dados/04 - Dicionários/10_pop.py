contatos = {"chryslleykelly@gmail.com": {"nome": "Crislei Keli", "telefone": "99901-4668"}}

resultado = contatos.pop("chryslleykelly@gmail.com")  # {'nome': 'Crislei Keli', 'telefone': '99901-4668'}
print(resultado)

resultado = contatos.pop("chryslleykelly@gmail.com", {})  # {}
print(resultado)