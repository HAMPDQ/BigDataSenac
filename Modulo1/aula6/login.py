login_user = "admin"
login_senha = 123456


tentativa = 3



while tentativa > 0:
    entrada_user = input("Infome o login: ")
    entrada_senha = float(input("Informe a senha: "))

    if entrada_user != login_user and entrada_senha != login_senha:
        print("nome de usuário e senha invalidos ")
        tentativa = tentativa - 1
        print(f"Suas tentativas restantes são {tentativa} ")
    elif entrada_user != login_user:
        print("login invalido ")
        tentativa = tentativa - 1
        print(f"Suas tentativas restantes são {tentativa} ")
    elif entrada_senha != login_senha:
        print("Senha invalida ")
        tentativa = tentativa - 1
        


print("Muitas tentativas de login. Tente novamente em 30 segundos. ")