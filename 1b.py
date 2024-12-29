import math

n = 2
somatorio = 0

while n < 100000:
    somatorio += 1/(n*math.log(n, math.e)**2)
    print(somatorio)
    n = n + 1

print("\n >>> ACABOU O LAÇO!",'\n')

# Acredito que esteja CONVERGINDO para 2.0

# Mesmo com WHILE TRUE há adições infinitas muito pequenas ao valor de 2.0

# Porém, ainda que as adições sejam muito pequenas, continua havendo adições, por isso não estou 100% convicta de que seja CONVERGENTE