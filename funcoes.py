# O que são funções?
# definir um comando que salva um conjunto de informações

#def comando(x, y):  # "def" é usada para criar o comando, e em '()' ficam os parâmetros, se forem necessários
   # soma = x + y    # código a ser executado pelo comando
   # print(soma) # -> se usar print, o comando vai apenas ser printado em vez de executado
    #return soma     # o certo é usar "RETURN"

#comando(x=10, y=20) # se usar PRINT aqui de novo, será printado 'None'

def comando(x, y):
    soma = x + y
    return soma

print(comando(x=10, y=20))  # aqui, com RETURN no escopo, se não usar PRINT, nada acontece