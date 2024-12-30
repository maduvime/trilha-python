'LAMBDA -> forma de reduzir blocos de funções simples'

def soma1(x, y):
    return x + y  # funções muito simples não precisam de toda essa formalidade

# forma mais simples de fazer:
soma2 = lambda x, y: (x + y)   # defino os parâmetros por lâmbda e em '()' eu coloco o que desejo de retorno

# Verificação se os mesmo valores serão retornados:
print(soma1(10,20), soma2(10,20))

# forma mais prática de escrever funções simples