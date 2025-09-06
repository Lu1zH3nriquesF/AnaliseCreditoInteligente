import streamlit as st
import pandas as pd
from Loading_Processing_Datas import carregar_dados
from IA import analisar_empresa, configurar_ia
from simular_cenario import simular_cenario
import os
from dotenv import load_dotenv

st.title("Assistente de Análise de Crédito Inteligente")

# Carrega os dados uma vez
# Você pode ter um seletor para escolher o formato do arquivo
caminho_arquivo = st.sidebar.selectbox(
    "Selecione o arquivo de dados:",
    ["dadoscreditoficticios.csv", "dadoscreditoficticios.json", "dadoscreditoficticios.parquet", "dadoscreditoficticios.xml"]
)

if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    configurar_ia(api_key)

# Lógica para carregar o DataFrame
df = None
if caminho_arquivo:
    st.info(f"Carregando dados de: {caminho_arquivo}")
    df = carregar_dados(caminho_arquivo)
    if df is not None:
        st.success("Dados carregados com sucesso!")
        st.write("Visão geral dos dados:", df.sort_values(by="Rating", ascending=True))
        
        # Cria a interface para análise
        st.subheader("Análise de Empresa")
        lista_empresas = df['Empresa'].tolist()
        empresa_selecionada = st.selectbox(
            "Selecione a empresa para análise:",
            options=lista_empresas
        )

        if st.button("Gerar Análise Completa"):
            with st.spinner("Gerando análise com a IA..."):
                analise = analisar_empresa(empresa_selecionada, df)
                st.markdown("---")
                st.markdown(f"**Análise para {empresa_selecionada}:**")
                st.write(analise)

        # Cria a interface para simulação
        st.subheader("Simulação de Cenários")
        col1, col2 = st.columns(2)
        with col1:
            nova_receita = st.number_input("Nova Receita Anual:", value=0.0)
        with col2:
            nova_divida = st.number_input("Nova Dívida Total:", value=0.0)
            
        if st.button("Simular Cenário"):
            parametros_simulados = {
                'Receita Anual': nova_receita,
                'Dívida Total': nova_divida,
            }
            with st.spinner("Simulando e gerando nova análise..."):
                analise_simulada = simular_cenario(empresa_selecionada, df, parametros_simulados)
                st.markdown("---")
                st.markdown(f"**Análise de Cenário Simulado para {empresa_selecionada}:**")
                st.write(analise_simulada)
                
        
        