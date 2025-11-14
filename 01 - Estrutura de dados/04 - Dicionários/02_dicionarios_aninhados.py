contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
    "chryslleykelly@gmail.com": {"nome": "Crislei Keli", "telefone": "99901-4668", "extra": {"twitter": "@chryslleykelly"}},
    }

telefone = contatos["chryslleykelly@gmail.com"]["telefone"]  # "99901-4668"
print(telefone)

extra = contatos["chryslleykelly@gmail.com"]["extra"]  # {"twitter": "@chryslleykelly"}
print(extra)  # {'nome': 'Crislei Keli', 'telefone': '99901-4668', 'extra': {'twitter': '@chryslleykelly'}} 