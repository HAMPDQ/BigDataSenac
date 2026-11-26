def remover_ultimo_item_carrinho(banco_dados, id_pedido):
    if id_pedido not in banco_dados["assinaturas_transacoes"]:
        return False

    pedido = banco_dados["assinaturas_transacoes"][id_pedido]

    if pedido["status"] != "ABERTO" or len(pedido["carrinho"]) == 0:
        return False

    item_removido = pedido["carrinho"].pop()

    pedido["valor_bruto"] = round(max(0.0, pedido["valor_bruto"] - item_removido["subtotal"]), 2)
    pedido["valor_liquido"] = round(max(0.0, pedido["valor_bruto"] - pedido["valor_desconto"]), 2)

    return True