import pandas as pd


def gerar_relatorio_pandas_csv(
    banco_dados, nome_arquivo="telemetria_vendas_pipoca.csv"
):
    try:
        if not banco_dados["assinaturas_transacoes"]:
            print("Sem transações no histórico para computar relatórios.")
            return False

        # Converte o dicionário de pedidos em formato analítico 2D DataFrame
        df = pd.DataFrame.from_dict(
            banco_dados["assinaturas_transacoes"], orient="index"
        )

        print("\nTELEMETRIA DE VENDAS DO PIPOCA.AI (PANDAS DATAFRAME):")
        print(df.to_string())

        # Mostra indicador do caixa geral consolidado
        print(
            f"\nFATURAMENTO TOTAL ACUMULADO: R$ {banco_dados['faturamento_total']:.2f}"
        )

        # Exporta como base CSV
        df.to_csv(nome_arquivo, index_label="id_pedido")
        print(f"Arquivo '{nome_arquivo}' exportado com sucesso no diretório de dados!")
        return True
    except Exception as e:
        print(f"Falha crítica no pipeline Pandas: {e}")
        return False
