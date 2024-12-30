'Diferenças entre funções e GENERATOR'

lista = [1,2,3,4]

# Eu quero que a cada chamada dessa função, se faça uma conta com o próxima elemento da lista

# Poderia ser assim:

#def function(x):
#    return x**2

#for i in lista:
#    print(function(i))

# Mas eu não quero fazer assim

# Dá pra usar GENERATOR pra fazer a mesma coisa:

def generator(lista):   # sim, parece uma função mesmo
    for i in lista:
        yield i**2      # 'yield' é o nome-chave que caracteriza o generator

g = generator(lista)    # generator precisa ser definido dentro de uma variável
for i in range(4):
    print(next(g))  # 'next(g)' significa "me dá o próximo elemento"

# A cada "print(next(g))", o código vai retornando o próximo elemento

# Na função, o 'return' quebra a função e ignora qualquer linha abaixo naquele mesmo escopo
# No 'yield' retorna o que tá até o 'yield', mas na próxima vez quechamar a função, ela vai continuar do 'yield', ou seja, ele vai ler o que estiver abaixo do 'yield'

# OBS.: A função 'iter()' gera um generator