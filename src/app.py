import os
import sys
import streamlit as st

# Adiciona o caminho da pasta src ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from extract import ler_arquivo
from transform import clean_data, faturamento_total

def main():
    st.title("Dashboard Superstore")

    # Carregar dados (mantém no estado da sessão)
    if st.button("Carregar Dados"):
        df = ler_arquivo()
        if df is not None:
            st.session_state.df = df
            st.success("Dados carregados com sucesso!")
            st.write(df.head())
        else:
            st.error("Erro ao carregar os dados!")

    # Verifica se os dados foram carregados
    if "df" in st.session_state:
        df = st.session_state.df

        if st.button("Limpar Dados"):
            df_limpo = clean_data(df)
            st.session_state.df = df_limpo  # Atualiza o df na sessão
            st.success("Dados limpos!")
            st.write(df_limpo.head())

        if st.button("Calcular Faturamento Total"):
            total = faturamento_total(df)
            st.success(f"Faturamento Total: R$ {total:,.2f}")

if __name__ == "__main__":
    main()
