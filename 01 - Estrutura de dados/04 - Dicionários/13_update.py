contatos = {"chrys@gmail.com": {"nome": "Crislei Keli", "telefone": "99901-4668"}}

contatos.update({"chryslley@gmail.com": {"nome": "Cris"}})
print(contatos)  # {'chryslley@gmail.com': {'nome': 'Cris'}}

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
# {'chryslley@gmail.com': {'nome': 'Cris'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}
print(contatos)