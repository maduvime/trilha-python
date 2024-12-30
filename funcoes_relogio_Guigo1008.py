import os
import time

def inicializa_valores():
    segundo = 0
    minuto = 0
    hora = 0
    return segundo, minuto, hora

def checa_viragem_de_unidade(segundo, minuto, hora):
    if segundo == 60:
        if minuto == 59:
            minuto = 0
            segundo = 0
            hora += 1
        else:
            segundo = 0
            minuto += 1

    return segundo, minuto, hora

def printa_legal(segundo, minuto, hora):
    if segundo < 10:
        segundo = f'0{segundo}'
    if minuto < 10:
        minuto = f'0{minuto}'
    if hora < 10:
        hora = f'0{hora}'
    print(f'{hora}:{minuto}:{segundo}')

def roda_relogio():
    segundo, minuto, hora = inicializa_valores()

    while True:
        os.system('cls')

        segundo, minuto, hora = checa_viragem_de_unidade(segundo, minuto, hora)
        printa_legal(segundo, minuto, hora)

        time.sleep(1)
        segundo += 1

roda_relogio()