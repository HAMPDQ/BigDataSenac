def eh_bissexto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True
            else:
                return False
        else:
            return False
    
    else:
        return False



try:
    ano = int(input("Digite um ano para saber se ele é bissexto: "))

except ValueError:
    print("Você precisa digitar um ano válido.")


else:
    if eh_bissexto(ano):
        print(f"O ano {ano} É bissexto")
    else:
        print(f"O ano {ano} NÃO é bissexto")