'Queremos fazer uma função para cálculo fatorial'

def fatorial(numero):   # vai receber um 'numero' para realizar o cálculo fatorial
    fat = 1
    while numero > 1: # pois em cada loop o numero perderá 1 unidade, até ser igual a 1
        fat *= numero   # fat = fat * numero
        numero -= 1   # numero = numero - 1
    return fat  # fat aqui no final será igual ao nº que se quer calcular a fatorial, e em cada loop, perderá 1 unidade
# esse bloco acima é responsável por retornar a sequência de nºs que serão multiplicados entre si

print(fatorial(5))  # o que faz os nºs multiplicarem entre si?


'Outro caminho (sem loop)'

def fatorial1(numero): 
    if numero == 0 or numero == 1:
        return 1    # pq 1! e 0! = 1
    else:
        return numero * fatorial1(numero - 1)   # aqui o código viu a necessidade de calcular "fatorial1(numero - 1)", portanto a função foi novamente ativada para outro valor, e assim sucessivamente até alcançar o valor = 1

print(fatorial1(5))

# O resultado será o mesmo, mas esse caminho não utilizou loop.
# Então por que deu certo?
# Foi utilizada uma estratégia chamada RECURSÃO.
# Funções recursivas: Haverá uma estrutura de IF/ELSE, onde um dos dois sempre "chamará" a função com outro valor, até que uma hora ela caia no IF e encerre