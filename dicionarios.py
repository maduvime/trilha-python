# Se eu fizesse com listas:
lista = [["Barra da Tijuca", "Ipanema", "Gavea", "Leblon"],
          ["Rio de Janeiro", "Sao Paulo", "Belo Horizonte"]]

# 0 eh bairros
# 1 eh cidades
print(lista[0])

# Se eu fizesse com dicionarios:
dictionary = {"Bairros": ["Barra da Tijuca", "Ipanema", "Gavea", "Leblon"],
               "Cidades": ["Rio de Janeiro", "Sao Paulo", "Belo Horizonte"]}

print(dictionary["Bairros"])

lista_de_chaves = list(dictionary.keys())
print(lista_de_chaves)

# Adicionando valores:
dictionary["Bairros"].append("Botafogo")
print(dictionary["Bairros"])

# Adicionando chaves:
dictionary["Estados"] = ["RJ", "SP", "MG"]
print(dictionary)