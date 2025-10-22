frutas = ["maçã", "banana", "laranja", "uva", "pera"]
print(frutas)

frutas [-1] # pera
frutas [-3] # laranja

frutas = []
print(frutas)

letras = list("python")
print(letras)

numeros = list(range(10))
print(numeros)

carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
print(carro)

matriz = [ 
          [1, "a", 2],
          ["b", 3, 4],
          [6, 5, "c"]
]

matriz[0] # [1, "a", 2]    
matriz[0] [0] # 1
matriz [0] [-1] # 2
matriz [-1] [-1]# [1, "a", 2]

lista = ["p", "y", "t", "h", "o", "n"]

lista[2:] # lista a partir do índice 2 ["t", "h", "o", "n"]
lista[:2] # lista até o índice 2 ["p", "y"]
lista[1:3] # lista do índice 1 até o 3 (3 não incluso) ["y", "t"]   
lista[0:3:2] # lista do índice 0 até o 3 (3 não incluso) pulando de 2 em 2 ["p", "t"]
lista[::] # lista completa ["p", "y", "t", "h", "o", "n"]
lista[::-1] # lista completa ao contrário ["n", "o", "h", "t", "y", "p"]

carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)
    
for indice, in enumerate(carros):
    print(f"{indice}: {carro}")
    
    numeros = [1, 30, 21, 2, 9, 65, 34]
    pares = [ numero for numero in numeros if numero % 2 == 0 ]
    print(pares)