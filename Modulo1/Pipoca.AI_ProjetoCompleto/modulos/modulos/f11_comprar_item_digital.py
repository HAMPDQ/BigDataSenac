def comprar_item_digital(banco_dados, id_pedido, id_item, qtd):
    loja_digital = banco_dados.get("loja_digital", {})
    if id_item not in loja_digital or qtd <= 0:
        return False

    item = loja_digital[id_item]
    if item["licencas_estoque"] < qtd:
        return False

    pedido = banco_dados.get("assinaturas_transacoes", {}).get(id_pedido)
    if pedido is None or pedido.get("status") != "ABERTO":
        return False

    subtotal = round(item["preco"] * qtd, 2)
    pedido["carrinho"].append(
        {
            "categoria": "LOJA_DIGITAL",
            "descricao": item["item"],
            "qtd": qtd,
            "subtotal": subtotal,
        }
    )

    item["licencas_estoque"] -= qtd
    pedido["valor_bruto"] = round(pedido["valor_bruto"] + subtotal, 2)
    pedido["valor_liquido"] = round(pedido["valor_bruto"] - pedido["valor_desconto"], 2)

    return True
