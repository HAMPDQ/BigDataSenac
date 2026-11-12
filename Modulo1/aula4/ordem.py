a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
c = int(input("Terceiro número: "))


#ordem padrão
ordem1 = a, b, c
ordem2 = b, c, a
ordem3 = c, a, b
ordem4 = b, a, c

if a < b and b < c:
    print(f"{ordem1}")
elif b < c and c < a:
    print(f"{ordem2}")
elif c < a and b > a:
    print(f"{ordem3}")
elif b < a and c > a:
    print(f"{ordem4}")
else:
    print("Valores inválidos")




