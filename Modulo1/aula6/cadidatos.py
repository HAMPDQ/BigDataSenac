for i in range(12):
    nome = input("Qual seu nome? ")
    idade = float(input("Qual a sua idade? "))

    if idade >= 18:
        tel = input(f"Olá {nome}! Informe um número de telefone: ")
        mail = input(f"Qual o seu melhor e-mail? ")
    
    elif idade < 18:
        print("Você não possui a idade mínima para o cadastro. ")
        