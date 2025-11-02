# filtro versão 1
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

# filtro versão 2
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [ numero for numero in numeros if numero % 2 == 0 ]
print(pares)
    
# modificando valores versão 1
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado[]

for numero in numeros:
    quadrado.append(numero ** 2)
    
# modificando versão 2
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]
    
    