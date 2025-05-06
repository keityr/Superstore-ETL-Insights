
from extract import ler_arquivo
import pandas as pd

def clean_data(df):
    """
    Realiza limpezas básicas no DataFrame.
    Exemplo: remover nulos, corrigir tipos, etc.
    
    Args:
        df (pd.DataFrame): DataFrame de entrada
        
    Returns:
        pd.DataFrame: DataFrame limpo
    """
    df = df.dropna() 
    return df


def faturamento_total(df):
    total = (df['Sales'] * df['Quantity']).sum()
    return total



if __name__ == "__main__":
    df = ler_arquivo()
    if df is not None:
        total = faturamento_total(df)
        print(f"Faturamento total: R$ {total:,.2f}")
    else:
        print("Erro ao carregar o DataFrame.")
