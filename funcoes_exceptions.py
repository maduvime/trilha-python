
'Caso: Senha que só recebe números'

def recebe_pin():   # não tem nada no '()' pq o parâmetro virá no ONPUT
    senha = input("Digite seu PIN (número!) >> ")
    try:    # TENTA mudar senha pra INTEIRO kkkk
        senha = int(senha)  # pois uma STRING não conseguiria virar um INTEIRO
    except:     # SENÃO:
        print("Senha inválida. Tente digitar um número.")
        senha = input("Digite seu PIN (número!) >> ")
    print(senha)

recebe_pin()    # puxando a função

# Moral da história: Quando ele não consegue executar, em vez de dar "Erro", o código vai cair nessa EXCEÇÃO e dar essa conduta que pedimos a ele
# Pra isso que serve o TRY EXCEPT