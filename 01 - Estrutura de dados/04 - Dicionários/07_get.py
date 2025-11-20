contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError

resultado = contatos.get("chave")  # None
print(resultado)

resultado = contatos.get("chave", {})  # {}
print(resultado)

resultado = contatos.get(
    "chryslleykelly@gmail.com", {}
)  # {"chryslleykelly@gmail.com": {"nome": "Crislei Keli", "telefone": "99901-4668"}}
print(resultado)