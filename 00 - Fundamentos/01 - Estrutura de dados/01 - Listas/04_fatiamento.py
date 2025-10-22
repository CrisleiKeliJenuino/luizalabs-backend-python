lista = ["p", "y", "t", "h", "o", "n"]

lista[2:] # lista a partir do índice 2 ["t", "h", "o", "n"]
lista[:2] # lista até o índice 2 ["p", "y"]
lista[1:3] # lista do índice 1 até o 3 (3 não incluso) ["y", "t"]   
lista[0:3:2] # lista do índice 0 até o 3 (3 não incluso) pulando de 2 em 2 ["p", "t"]
lista[::] # lista completa ["p", "y", "t", "h", "o", "n"]
lista[::-1] # lista completa ao contrário ["n", "o", "h", "t", "y", "p"]

