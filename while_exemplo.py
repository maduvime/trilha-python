'CRONÔMETRO COM PYTHON'

# Importando biblioteca que introduz o conceito de tempo no Python
import time

# Definindo uma variável que irá receber o valor do tempo atual

# tempo = 0    # Tempo começando em zero

# while True:    # Usando WHILE o cronômetro tem que rodar para sempre
#    print(tempo)    # Colocando antes, printa o ZERO também
#    time.sleep(1)    # espera unidades de segundo antes de executar a próxima ação do código
#    tempo += 1    # tempo = tempo + 1


'Introduzindo o conceito de minuto'

segundo = 0
minuto = 0

# while True:
#    if segundo == 60:
#        segundo = 0
#        minuto = minuto + 1
#    print(f'{minuto}:{segundo}')
#    time.sleep(1)
#    segundo = segundo + 1

# O que fazer pra não poluir o terminal? -> BIBLIOTECA OS (Operational System)
import os    # Importando biblioteca que interage com o sistema operacional

while True:
    os.system('cls')    # sempre limpa o terminal no início do loop a partir da interação do terminal com o código em Python
    if segundo == 60:
        segundo = 0
        minuto = minuto + 1

    if segundo < 10:
        print(f'{minuto}:0{segundo}')
    else:
        print(f'{minuto}:{segundo}')
        
    time.sleep(1)
    segundo = segundo + 1