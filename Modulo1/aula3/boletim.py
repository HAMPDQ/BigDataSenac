nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno:" ))


media = (nota1 + nota2)/2


resultado = media
# print(f"Segue a média obetida: {resultado}") #dessa forma também funciona. No caso, o f vem na frente de format, ele vai considerar tudo oque esta dentro das aspas como str mas somente oque entra em chaves fica como variável


if resultado < 12:
    print (f"Sua média foi {resultado}, você está reprovado")
elif resultado >= 12:
    print (f"Sua média foi {resultado}, você está aprovado")

