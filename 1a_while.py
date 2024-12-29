import random

escolhas = ("pedra", "papel", "tesoura")    # tupla
tentativas = 0
vitoria = 0
empate = 0
derrota = 0

while True:
    chute = input("Pedra, papel ou tesoura? ")
    escolha_pc = random.choice(escolhas)
    print(f"\nO PC escolheu: {escolha_pc}", '\n')
    if chute == escolha_pc:
        print("Você e o PC escolheram a mesma coisa. Tente novamente.", '\n')
        empate += 1
    else:
        if chute == "pedra" and escolha_pc == "papel":
            print("Papel embrulha pedra. Você perdeu essa rodada!", '\n')
            derrota += 1
        elif chute == "pedra" and escolha_pc == "tesoura":
            print("Pedra quebra tesoura. Você ganhou essa rodada!", '\n')
            vitoria += 1
        elif chute == "papel" and escolha_pc == "pedra":
            print("Papel embrulha pedra. Você ganhou essa rodada!", '\n')
            vitoria += 1
        elif chute == "papel" and escolha_pc == "tesoura":
            print("Tesoura corta papel. Você perdeu essa rodada!", '\n')
            derrota += 1
        elif chute == "tesoura" and escolha_pc == "pedra":
            print("Pedra quebra tesoura. Você perdeu essa rodada!", '\n')
            derrota += 1
        elif chute == "tesoura" and escolha_pc == "papel":
            print("Tesoura corta papel. Você ganhou essa rodada!", '\n')
            vitoria += 1
    tentativas = tentativas + 1
    if tentativas == 5:
        break

print(f"\n>>> Placar final:  Você {vitoria} x {derrota} PC", '\n')

if vitoria < derrota:
    print("Você perdeu para uma máquina, que vergonha!")
elif vitoria > derrota:
    print("Parabéns campeão!")
else:
    print("Você empatou com a máquina! Quem sabe numa próxima...")