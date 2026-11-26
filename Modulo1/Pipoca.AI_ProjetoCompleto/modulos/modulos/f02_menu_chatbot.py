"""
Menu Interativo do Chatbot
Pipoca.AI
"""


def exibir_menu_chatbot(nickname):
    """
    Exibe menu principal do chatbot.
    Argumentos:
        nickname (str): Nome escolhido pelo usuário (Já validado).
    Retorna:
        int: Opção entre 0 e 9.
    Retorna: -1 em caso de erro.
    """
    print("\n" + "=" * 55)
    print(f"🤖 Olá 👋, @{nickname}! Como posso lhe ajudar hoje?")
    print("\n🍿 Bem-vindo ao menu de opções 🍿:")
    print("=" * 55)

    print("[1] Assinar Plano de Streaming (SaaS)")
    print("[2] Comprar Acesso Live Event (Pay-Per-View)")
    print("[3] Comprar na Loja Digital (Coins, Passes, 8K)")
    print("[4] Ver Resumo do Carrinho Digital")
    print("[5] Remover Último Item do Carrinho")
    print("[6] Aplicar Descontos e Finalizar Checkout")
    print("[7] Solicitar Reembolso (Anti-Churn)")
    print("[8] Operações de Servidor / Auditoria de Licenças")
    print("[9] Gerar Relatório Analytics (Pandas + CSV)")
    print("[0] Trocar Usuário / Sair")

    try:
        opcao = int(input("Escolha uma opção (0-9): "))

        if 0 <= opcao <= 9:
            return opcao
        else:
            print("Opção não encontrada, tente novamente.")
            return -1

    except ValueError:
        print("Digite apenas números.")
        return -1
