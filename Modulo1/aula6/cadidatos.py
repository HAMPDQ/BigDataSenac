candidatos_validos = []

for i in range(5):
    nome = input("Qual o nome do candidato ? ")

    
    idade = int(input(f"Olá {nome}. Insira sua idade "))
    mail = input("Insira seu e-mail ")
    fone = input("Insira seu telefone ")

    if idade >= 18:
        candidatos_validos.append((nome, idade, mail, fone))
    elif idade < 18:
        print(f"Desculpe {nome}, você não possui idade suficiente para se candidatar. ")


print("Candidatos válidos: ")
for candidato in candidatos_validos:
    print(f"Nome: {candidato[0]}, Idade: {candidato[1]}, E-mail: {candidato[2]}, Telefone: {candidato[3]}")

    


