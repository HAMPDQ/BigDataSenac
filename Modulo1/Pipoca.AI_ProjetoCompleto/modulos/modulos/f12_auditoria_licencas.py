def verificar_esgotamento_licencas(banco_dados):
    itens_criticos = []
    for dados in banco_dados["loja_digital"].values():
        if dados["licencas_estoque"] <= dados["alerta_minimo"]:
            itens_criticos.append(dados["item"])

    return itens_criticos


if __name__ == "__main__":
    bd_teste = {
        "loja_digital": {
            501: {
                "item": "Pacote 1000 PipocaCoins",
                "preco": 19.90,
                "licencas_estoque": 10,
                "alerta_minimo": 15,
            }
        }
    }
    print(verificar_esgotamento_licencas(bd_teste))
