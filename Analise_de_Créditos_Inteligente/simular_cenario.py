import google.generativeai as genai
from dotenv import load_dotenv
import pandas as pd
import os
from IA import configurar_ia


def simular_cenario(empresa, df_dados, parametros_simulados):
    """
    Simula um cenário de crédito ajustando os parâmetros de uma empresa e gera uma nova análise.
    
    Args:
        empresa (str): O nome da empresa para simular.
        df_dados (pd.DataFrame): O DataFrame com os dados das empresas.
        parametros_simulados (dict): Um dicionário com os parâmetros a serem alterados.
                                    Ex: {'Receita Anual': 10000000, 'Dívida Total': 500000}
    """
    dados_empresa_originais = df_dados[df_dados['Empresa'] == empresa]
    
    if dados_empresa_originais.empty:
        return "Empresa não encontrada para simulação."

    # Criar uma cópia dos dados para a simulação
    dados_para_simular = dados_empresa_originais.iloc[0].to_dict()

    # Atualizar os dados com os parâmetros simulados
    dados_para_simular.update(parametros_simulados)

    # Criar um prompt focado na simulação
    prompt = f"""
    Você é um analista de crédito experiente. Analise o seguinte cenário hipotético para a empresa {dados_para_simular['Empresa']}.
    Considere apenas os dados abaixo.
    
    Cenário Simulado:
    - Receita Anual: R${dados_para_simular.get('Receita Anual', 'N/A')}
    - Dívida Total: R${dados_para_simular.get('Dívida Total', 'N/A')}
    - Prazo Médio de Pagamento: {dados_para_simular.get('Prazo de Pagamento (dias)', 'N/A')} dias
    - Setor: {dados_para_simular.get('Setor', 'N/A')}
    - Rating de Crédito: {dados_para_simular.get('Rating', 'N/A')}
    Notícias Recentes:
    {dados_para_simular.get('Notícias Recentes', 'Nenhuma notícia nova.')}

    Com base apenas nestes dados, qual seria sua análise de risco?
    Gere uma recomendação preliminar (aprovado ou recusado) e justifique sua decisão.
    """

    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Erro ao simular o cenário: {e}"
    
if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    configurar_ia(api_key)

# Exemplo de uso
# Vamos supor que queremos ver o que acontece se a Empresa Alfa dobrar sua receita
# parametros_simulados = {
#     'Receita Anual': 10000000,
#     'Dívida Total': 500000,
# }

# dados_exemplo = {
#     'Empresa': ['Empresa Alfa'],
#     'Receita Anual': [5000000],
#     'Dívida Total': [1000000],
#     'Prazo de Pagamento (dias)': [45],
#     'Setor': ['Tecnologia'],
#     'Rating': ['A+'],
#     'Notícias Recentes': ['A empresa fechou um grande contrato e espera crescimento de 20% no próximo trimestre.']
# }
# df_exemplo = pd.DataFrame(dados_exemplo)

# analise_simulada = simular_cenario('Empresa Alfa', df_exemplo, parametros_simulados)
# print("----------------- Análise do Cenário Simulado -----------------")
# print(analise_simulada)
# print("---------------------------------------------------------------")