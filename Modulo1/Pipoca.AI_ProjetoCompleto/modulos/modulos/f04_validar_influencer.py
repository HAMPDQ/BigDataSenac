# def pra importar
# variavel codigo cupom eh igual elas mesma
# porém coloquer o strip para tirar todos os espaços
# e o upper pra deixar tudo maiusculo
# if se o codigo estiver dentro do bancos de dados de cupons ativos
# vai retornar verdadeiro
# else se não estiver no banco de dados de cupons ativos
#


def validar_cupom_influencer(banco_dados, codigo_cupom):
    if not codigo_cupom:
        return False

    codigo_cupom = codigo_cupom.strip().upper()

    if codigo_cupom in banco_dados["cupons_ativos"]:
        return True
    else:
        return False
