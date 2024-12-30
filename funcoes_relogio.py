'REFAZENDO RELÓGIO USANDO FUNÇÕES' # Incompleto

import os
import time

def inicializa_valores():      # pq fazer isso?
    segundo = 0
    minuto = 0
    hora = 0
    return segundo, minuto, hora
# quando rodar a função, irá iniciar os valores em zero

# def conta_tempo():

def checa_viragem_de_unidade(segundo, minuto, hora):
    if segundo == 60:
        if minuto == 60:
            segundo = 0
            minuto = 0
            hora += 1
        else:
            segundo = 0
            minuto += 1
    return (segundo, minuto, hora)

def garante_duas_casas_dec(segundo, minuto, hora):
    if segundo < 10:
        segundo = f'0{str(segundo)}'    # pq precisou transformar em STRING?
    if minuto < 10:
        minuto = f'0{str(minuto)}'
    if hora < 10:
        hora = f'0{str(hora)}'
    return segundo, minuto, hora

def printa_hora(segundo, minuto, hora):
    print()         # pq essa parte tem que vir

def roda_relogio(): # não precisa de parâmetros pq é autosuficiente
    segundo, minuto, hora = inicializa_valores()    # hora de desempacotar(?)

    while True:     # Hora de rodar o relógio
        os.system('cls')
        segundo, minuto, hora = checa_viragem_de_unidade(segundo, minuto, hora)
        segundo, minuto, hora = garante_duas_casas_dec(segundo, minuto, hora)
        time.sleep(1)
        segundo += 1

roda_relogio()      # Hora de "chamar" a função



