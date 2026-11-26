# Função 17 - Solicitar reembolso


def solicitar_reembolso(banco_dados, id_pedido):
    try:
        pedido = banco_dados["assinaturas_transacoes"][id_pedido]
    except KeyError:
        return False

    if pedido["status"] == "REEMBOLSADO":
        return False

    if pedido["status"] == "PAGO":
        banco_dados["faturamento_total"] = round(
            max(0.0, banco_dados["faturamento_total"] - pedido["valor_liquido"]), 2
        )

    pedido["carrinho"].clear()
    pedido["valor_bruto"] = 0.0
    pedido["valor_desconto"] = 0.0
    pedido["valor_liquido"] = 0.0
    pedido["status"] = "REEMBOLSADO"
    return True
