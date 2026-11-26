def listar_planos_streaming(banco_dados):
    print("=" * 50)
    print("          CATÁLOGO DE PLANOS STREAMING")
    print("=" * 50)

    for id_plano, info in banco_dados["planos_streaming"].items():
        print(f"ID do Plano: {id_plano}")
        print(f"Nome: {info['nome']}")
        print(f"Mensalidade: R$ {info['mensalidade']:.2f}")
        print(f"Telas simultâneas: {info['telas_simultaneas']}")
        print("=" * 50)

    print("ATENÇÃO: Contratações de 12 meses ou mais")
    print("recebem 15% de desconto direto no plano.")
    print("=" * 50)


if __name__ == "__main__":
    bd_teste = {
        "planos_streaming": {
            1: {
                "nome": "Plano Pipoca Solo (Full HD)",
                "mensalidade": 29.90,
                "telas_simultaneas": 1,
            }
        }
    }
    listar_planos_streaming(bd_teste)
