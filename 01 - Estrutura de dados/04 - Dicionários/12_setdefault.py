contato = {"nome": "Crislei Keli", "telefone": "99901-4668"}

contato.setdefault("nome", "Geovanna")  # "Crislei Keli"
print(contato)  # {'nome': 'Crislei Keli', 'telefone': '99901-4668'}

contato.setdefault("idade", 39)  # 39
print(contato)  # {'nome': 'Crislei Keli', 'telefone': '99901-4668', 'idade': 39}