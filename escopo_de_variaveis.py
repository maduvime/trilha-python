# Para mudar uma variável 'a' global dentro do escopo de uma função -> usar 'global a'

a = 0

def escopo1():
    global a    # isso indica que a variável 'a', mesmo dentro da função, é global
    a = 10

escopo1()

print(a)    # se dermos print aqui sem definir 'global a' dentro do escopo da função, o valor printado será zero, e não 10