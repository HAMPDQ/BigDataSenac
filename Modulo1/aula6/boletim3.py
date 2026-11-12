

for i in range(4):
    nome = input("Qual o nome do aluno ? ")


    nota1 = float(input(f"Olá {nome}. Insira sua primeira nota "))
    nota2 = float(input("Agora insira sua segunda nota "))
    media = (nota1 + nota2)/2

    if media > 7:
        print(f"Aprovado com média: {media}")
    elif media >= 5 and media <= 7:
        print(f"Recuperção com média: {media}")
    elif media < 5:
        print(f"Reprovado com média: {media}")
    else:
        print("Opção inválida")









