nota1 = float(input("Sua primeira nota: "))
nota2 = float(input("Sua segunda nota: "))
nota3 = float(input("Sua terceira nota: "))
nota4 = float(input("Sua quarta nota: "))


media = (nota1 + nota2 + nota3 + nota4)/4

if media > 7:
    print(f"Aprovado com média: {media}")
elif media >= 5 and media <= 7:
    print(f"Recuperção com média: {media}")
elif media < 5:
    print(f"Reprovado com média: {media}")
else:
    print("Opção inválida")

