'ABREVIAÇÃO'

numeros_pares_ate_20 = [] # quero colocar todos os nºs pares até 20 aqui

for i in range(11): # coloquei 11 e não 10 pq começa a contar a partir do zero
    numeros_pares_ate_20.append(i*2) # multiplica por 2 todos os nºs de 1 a 10 (ou seja, todo os nºs pares até 20)

print(numeros_pares_ate_20)

# Dá pra criar isso de forma mais rápida usando LIST COMPREHENSIONS
# É uma forma de criar itens de uma lista iterando com FOR de forma mais rápida

pares_ate_40 = [i*2 for i in range(21)] # coloca "i*2" para cada i numa faixa de 21 valores
print(pares_ate_40)     # não precisa colocar ".append()" pq a função já está dentro da lista -> '[aqui]'

# Dá pra colocar uma tupla ali dentro tbm... O CÉU É O LIMITE!