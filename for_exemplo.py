texto = "Python é uma linguagem de programação de alto nível, [5] interpretada de script, imperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum em 1991. [1] Atualmente, possui um modelo de desenvolvimento comunitário, aberto e gerenciado pela organização sem fins lucrativos Python Software Foundation. Apesar de várias partes da linguagem possuírem padrões e especificações formais, a linguagem, como um todo, não é formalmente especificada. O padrão na pratica é a implementação CPython. A linguagem foi projetada com a filosofia de enfatizar a importância do esforço do programador sobre o esforço computacional. Prioriza a legibilidade do código sobre a velocidade ou expressividade. Combina uma sintaxe concisa e clara com os recursos poderosos de sua biblioteca padrão e por módulos e frameworks desenvolvidos por terceiros."

lista_de_palavras = texto.split(' ')

#print(lista_de_palavras)

for indice in range(len(lista_de_palavras)):
    if lista_de_palavras[indice] == "Python":
        lista_de_palavras[indice] = "Fython"
    elif lista_de_palavras[indice] == "CPython.":
        lista_de_palavras[indice] = "CFython."
    else:
        pass       # mas isso não precisa colocar, vai passar automaticamente
print(' '.join(lista_de_palavras))

# OU

novo_texto = ""

for palavra in lista_de_palavras:
    novo_texto = novo_texto + palavra + " "   # concatenação
print(novo_texto)