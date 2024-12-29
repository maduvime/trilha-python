import random

numero = random.randint(1, 100)
tentativas = 0

while tentativas < 10:
    chute = int(input("Digite um número entre 1 e 100: "))
    if chute == numero:
        print("PARABÉNS! Você acertou!")
        break
    elif chute < numero:
        print("O número é MAIOR que esse.")
    else:
        print("O número é MENOR que esse.")
    tentivas = tentativas + 1