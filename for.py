# Formas de se usar o FOR:
    # com um generator. Ex.: for n in range(10)
    # com um iterator. Ex.: for n in [1, 2, 3, 4, 5]

# usando com iterator
string = "juliana"   # vai iterar sobre cada letra da string, ou da lista etc

for c in string:
    print(c)

# usando com generator
for i in range(10):
    print(i)

# Quando teremos que usar while?
# Quando não sabemos o tamanho do iterável.
# Neste caso terei que usar o while True.
