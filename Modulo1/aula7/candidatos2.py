candidatos_validos = []

for i in range(2):
    nome = input("Qual o nome do candidato ? ")

    
    idade = int(input(f"Olá {nome}. Insira sua idade "))
    mail = input("Insira seu e-mail ")
    fone = input("Insira seu telefone ")

    if idade >= 18:
        candidatos_validos.append(nome, idade, mail, fone)
        aprovado = {candidatos_validos}
    elif idade < 18:
        print(f"Desculpe {nome}, você não possui idade suficiente para se candidatar. ")



    
print(candidatos_validos)
