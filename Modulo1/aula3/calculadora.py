valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))

decisao = float(input("Digite que operação deseja fazer: 1 - soma, 2 - subtração, \n3 - divisão, 4 - multiplicação: "))



# o sinal de % serve para mostrar apenas o resto da minha divisão
soma = valor1 + valor2
subtracao = valor1 - valor2
divisao = valor1 / valor2
multiplicacao = valor1 * valor2


if decisao == 1:
    print(soma)
elif decisao == 2:
    print(subtracao)
elif decisao == 3:
    print(divisao)
elif decisao == 4:
    print(multiplicacao)
else:
    print("Operação inválida")
