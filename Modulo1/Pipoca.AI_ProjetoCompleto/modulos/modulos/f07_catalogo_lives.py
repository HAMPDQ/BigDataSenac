def listar_eventos_live(banco_dados):
    for id_evento, dados in banco_dados["eventos_live"].items():
        print(f"ID do evento: {id_evento}")
        print(f"Nome do evento: {dados['evento']}")
        print(f"Preço: R$ {dados['preco']:.2f}")

        if dados["slots_servidor"] > 0:
            print(f"Slots disponíveis: {dados['slots_servidor']}")
        else:
            print("Servidor lotado!")
        print("-" * 40)


if __name__ == "__main__":
    bd_teste = {
        "eventos_live": {
            101: {
                "evento": "Final Mundial Valorant 2026 (POV Pro)",
                "preco": 39.90,
                "slots_servidor": 500,
            }
        }
    }
    listar_eventos_live(bd_teste)
