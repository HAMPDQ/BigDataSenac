def reservar_acesso_live(banco_dados, id_pedido, id_evento, qtd_acessos):
    """
    Reserva acessos para um evento Live PPV e registra a compra no carrinho.

    Retorna:
        True  -> reserva realizada e compra registrada.
        False -> dados inválidos, pedido inexistente/fechado ou slots insuficientes.
    """

    # 1. Validar a existência do evento e a quantidade solicitada.
    eventos = banco_dados.get("eventos_live", {})
    if id_evento not in eventos or qtd_acessos <= 0:
        return False

    # 2. Validar o pedido e garantir que ainda esteja aberto.
    pedidos = banco_dados.get("assinaturas_transacoes", {})
    if id_pedido not in pedidos:
        return False

    pedido = pedidos[id_pedido]
    if pedido.get("status") != "ABERTO":
        return False

    evento = eventos[id_evento]
    slots_disponiveis = evento.get("slots_servidor", 0)

    # 3. Verificar a disponibilidade antes de alterar qualquer dado.
    if slots_disponiveis < qtd_acessos:
        print(
            f"ALERTA: não há acessos suficientes para o evento "
            f"'{evento.get('evento', 'Evento Live')}'. "
            f"Disponíveis: {slots_disponiveis} | Solicitados: {qtd_acessos}."
        )
        return False

    # 4. Calcular o subtotal e preparar o item do carrinho.
    preco = evento["preco"]
    subtotal = round(preco * qtd_acessos, 2)

    item_carrinho = {
        "categoria": "LIVE_PPV",
        "descricao": evento["evento"],
        "qtd": qtd_acessos,
        "subtotal": subtotal
    }

    # 5. Confirmar a reserva dos slots e registrar a compra.
    evento["slots_servidor"] -= qtd_acessos
    pedido["carrinho"].append(item_carrinho)

    pedido["valor_bruto"] = round(pedido["valor_bruto"] + subtotal, 2)
    pedido["valor_liquido"] = round(
        pedido["valor_bruto"] - pedido["valor_desconto"], 2
    )

    return True
