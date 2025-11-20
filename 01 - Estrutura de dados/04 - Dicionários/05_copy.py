contatos = {"chryslley": {"nome": "Crislei", "telefone": "99901-4668"}}

copia = contatos.copy()
copia["chryslleykelly@gmail.com"] = {"nome": "Cris"}

print(contatos["Crislei"])  # {"nome": "Crislei", "telefone": "99901-4668"}

print(copia["chryslleykelly@gmail.com"])  # {"nome": "Cris"}