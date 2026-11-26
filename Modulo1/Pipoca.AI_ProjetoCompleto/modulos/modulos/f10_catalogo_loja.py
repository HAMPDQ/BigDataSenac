def listar_loja_digital(banco_dados):
    for id_item, dados in banco_dados["loja_digital"].items():
        print(
            f"id: {id_item} | item: {dados['item']} | preço R$ {dados['preco']:.2f} | estoque: {dados['licencas_estoque']}"
        )


if __name__ == "__main__":
    bd_teste = {
        "loja_digital": {
            501: {
                "item": "Pacote 1000 PipocaCoins (Moeda Virtual)",
                "preco": 19.90,
                "licencas_estoque": 100,
                "alerta_minimo": 15,
            }
        }
    }
    listar_loja_digital(bd_teste)
