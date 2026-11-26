def aplicar_descontos_digitais(banco_dados, id_pedido, cupom_influencer_valido):
    if id_pedido not in banco_dados["assinaturas_transacoes"]:
        return 0.0

    pedido = banco_dados["assinaturas_transacoes"][id_pedido]
    percentual = 0.0

    if pedido["assinante_anual"]:
        percentual += 0.10

    if cupom_influencer_valido:
        percentual += 0.10

    pedido["valor_desconto"] = round(pedido["valor_bruto"] * percentual, 2)
    pedido["valor_liquido"] = round(pedido["valor_bruto"] - pedido["valor_desconto"], 2)

    return pedido["valor_liquido"]