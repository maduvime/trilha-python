# Sets: 
lista = [1, 2, 3, 3, 4, 5, 5]
conjunto = {1, 2, 3, 3, 4, 5, 5}
conjunto2 = set(lista)

print(conjunto)
print(conjunto2)  # será igual e vai "comer" os nºs repetidos

# Tuplas:
lista = [1, 2, 3, 3, 4, 5, 5]
tupla = (1, 2)    # imutável  # usa parênteses em vez de colchetes

# Desempacotamento das Tuplas
um, dois = tupla

print(um)

print(tupla)