def contratar_plano_streaming(banco_dados, id_pedido, id_plano, meses_fidelidade):
    planos = banco_dados.get("planos_streaming", {})
    pedidos = banco_dados.get("assinaturas_transacoes", {})

    if id_plano not in planos or meses_fidelidade < 1:
        return False

    if id_pedido not in pedidos:
        return False

    pedido = pedidos[id_pedido]
    plano = planos[id_plano]

    nome_do_plano = plano["nome"]
    mensalidade = plano["mensalidade"]

    subtotal = mensalidade * meses_fidelidade

    if meses_fidelidade >= 12:
        subtotal = subtotal * 0.85

    subtotal = round(subtotal, 2)

    item = {
        "categoria": "STREAMING",
        "descricao": f"{nome_do_plano} ({meses_fidelidade}m)",
        "qtd": meses_fidelidade,
        "subtotal": subtotal
    }

    if "carrinho" not in pedido:
        pedido["carrinho"] = []

    pedido["carrinho"].append(item)
    pedido["valor_bruto"] = round(pedido.get("valor_bruto", 0.0) + subtotal, 2)
    pedido["valor_liquido"] = round(pedido["valor_bruto"] - pedido.get("valor_desconto", 0.0), 2)

    return True