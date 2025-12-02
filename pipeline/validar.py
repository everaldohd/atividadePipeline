"""
Pipeline - Etapa 2: Validar Dados com Pandera
"""

import pandas as pd
import pandera.pandas as pa


def criar_schema():
    """
    Cria o schema de validação para o dataset de clientes.
    
    Returns:
        pa.DataFrameSchema do Pandera
    """
    
    schema = pa.DataFrameSchema({

        "cliente_id": pa.Column(int, nullable=False, unique=True),
        "idade": pa.Column(int, pa.Check.in_range(18, 80)),
        "renda_mensal": pa.Column(float, pa.Check.in_range(1000, 50000)),
        
        # Estas validações já estão prontas como exemplo:
        "tempo_conta_meses": pa.Column(int, pa.Check.in_range(1, 240)),
        "num_produtos": pa.Column(int, pa.Check.in_range(1, 5)),
        "tem_cartao_credito": pa.Column(int, pa.Check.isin([0, 1])),

        "score_credito": pa.Column(float, pa.Check.in_range(300, 850)),
        
        "respondeu_campanha": pa.Column(int, pa.Check.isin([0, 1])),
        
    })
    
    return schema


def validar_dados(df):
    """
    Valida o DataFrame usando o schema definido.
    
    Args:
        df: DataFrame a ser validado
        
    Returns:
        DataFrame validado (ou levanta exceção se inválido)
    """
    schema = criar_schema()
    
    print("Validando dados...")
    
    try:
        df_validado = schema.validate(df)
        print("✅ Dados válidos!")
        return df_validado
    except pa.errors.SchemaError as e:
        print("❌ Dados inválidos!")
        print(f"Erro: {e}")
        raise


# Teste local
if __name__ == "__main__":
    # Carregar dados para teste
    df = pd.read_csv("data/clientes_campanha.csv")
    
    # Tentar validar
    try:
        df_validado = validar_dados(df)
        print(f"\n{len(df_validado)} registros validados com sucesso!")
    except Exception as e:
        print(f"\nFalha na validação. Verifique os TODOs!")