def exibir_resumo_pedido(banco_dados, id_pedido):
    if id_pedido not in banco_dados["assinaturas_transacoes"]:
        print("Pedido não encontrado.")
        return

    p = banco_dados["assinaturas_transacoes"][id_pedido]
    print("\n" + "=" * 50)
    print(f"EXTRATO DO PEDIDO #{id_pedido} | {p['nickname']} ({p['email_usuario']})")
    print(f"Status: {p['status']} | Pagamento: {p['metodo_pagamento']}")
    print("=" * 50)

    if not p["carrinho"]:
        print("  Carrinho vazio.")
    else:
        for idx, item in enumerate(p["carrinho"], 1):
            print(f"  {idx}. [{item['categoria']}] {item['descricao']} (x{item['qtd']}) -> R$ {item['subtotal']:.2f}")

    print("-" * 50)
    print(f"Valor Bruto:   R$ {p['valor_bruto']:.2f}")
    print(f"Desconto:      R$ {p['valor_desconto']:.2f}")
    print(f"Valor Líquido: R$ {p['valor_liquido']:.2f}")
    print("=" * 50)