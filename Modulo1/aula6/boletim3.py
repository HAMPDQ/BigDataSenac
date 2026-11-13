
resultados = []

for i in range(5):
    nome = input("Qual o nome do aluno ? ")


    nota1 = float(input(f"Olá {nome}. Insira sua primeira nota "))
    nota2 = float(input("Agora insira sua segunda nota "))
    media = (nota1 + nota2)/2

    resultados.append((nome, media))


for nome, media in resultados:
    if media > 7:
        print(f"Parabens {nome}, você foi aprovado com média: {media}")
    elif media >= 5 and media <= 7:
        print(f"{nome}, você está em recuperação com média: {media}")
    elif media < 5:
        print(f"{nome}, você foi reprovado com média: {media}")
    else:
        print("Opção inválida")