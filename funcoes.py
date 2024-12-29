# O que são funções?
# definir um comando que salva um conjunto de informações

def comando(x, y):  # "def" é usada para criar o comando, e em '()' ficam os parâmetros, se forem necessários
    soma = x + y    # código a ser executado pelo comando
    print(soma) # -> se usar print, o comando vai apenas ser printado em vez de executado
    #return soma     # o certo é usar "RETURN"

comando(x=10, y=20) # se usar PRINT aqui de novo, será printado 'None'


def comando(x, y):
    soma = x + y
    return soma

print(comando(x=10, y=20))  # aqui, com RETURN no escopo, se não usar PRINT, nada acontece

print(comando(10, 20))  # também pode ser escrito assim


'Para detectar se um número é par'

def ehpar(numero):  # aqui passa um nº, e eu quero detectar se esse nº é par
    return numero % 2 == 0  # '%' divide o nº por 2 retornando o resto da divisão; se esse resto for igual(==) a zero, o nº é par

# print(ehpar(numero=10))     # mas não é necessário colocar esse 'numero=', apenas 'print(ehpar(10))'

print(ehpar(10))