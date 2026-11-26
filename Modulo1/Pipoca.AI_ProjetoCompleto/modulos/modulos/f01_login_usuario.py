'''
Autenticação de Usuário
Pipoca.AI
'''

def autenticar_usuario():
    '''
    Solicita email e nickname do usuário.
    Retorna:
        tuple[str, str]: (email, nickname)
    '''

    print("=" * 55)
    print("🍿 Bem-vindo ao PIPOCA.AI 🍿")
    print("Seu hub de entretenimento digital")
    print("=" * 55)

    while True:

        email = input("\nDigite seu e-mail: ").strip()
        nickname = input("Digite seu nickname: ").strip()

        #.strip() ajuda eliminando os espaços da direita e esquerda que o usuário dê. Assim, evitando erros.
        
        if "@" in email and "." in email and len(nickname) > 0:
            return email, nickname
        else:
            print(
            "Dados incorretos"
            "\nVerifique o e-mail e informe um nickname válido."
            )