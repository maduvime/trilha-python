'WHILE'

import math

n = 2   # n começa a ser contado a partir de 2
somatorio = 0   # para que o somatório comece do zero (tela em branco)

while n < 10:
    somatorio = somatorio + 1/2**math.log(n, math.e)
    print(somatorio)
    n = n + 1   # se o valor de n nunca mudar, o WHILE executará constantemente n = 2 e o laço nunca vai terminar kkkk

print("\n >>> ACABOU O LAÇO!",'\n','\n')


'WHILE AVANÇADO'

# CRONÔMETRO
import time   # biblioteca nativa do python que adiciona recursos de tempo

c = 0
while c < 60:
    print(c)
    time.sleep(1)   # espera um tempinho antes de executar a próxima ação do código (esse "tempinho" são unidades de segundo)
    c = c + 1

print(">>> FIM DO CRONÔMETRO!")

# Outra forma de fazer
c = 0
while True:
    if c == 10:
        pass   # continua executando o código
    if c == 20:
        break   # estrutura de quebra  
    print(c)
    time.sleep(1)
    c = c + 1
print("Fui breakado!")


# Outra forma de fazer usando PASS e BREAK
c = 0
while True:
    if c <= 10:
        pass   # continua executando o código
    else:
        break   # estrutura de quebra  
    print(c)
    time.sleep(1)
    c = c + 1
print("Fui breakado!")


# Outra forma de fazer usando CONTINUE
c = 0
while c < 10:
    c = c + 1
    if c == 4:
        continue   # interrompe apenas a iteração atual (não interrompe o fluxo do while inteiro)
    print(c)
    time.sleep(1)
    
print("Fui breakado!")