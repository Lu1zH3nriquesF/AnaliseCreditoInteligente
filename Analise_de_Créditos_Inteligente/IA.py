import google.generativeai as genai
from Loading_Processing_Datas import carregar_dados
import os
from dotenv import load_dotenv


def configurar_ia(api_key):
    """Configura a API do Google Generative AI."""
    genai.configure(api_key=api_key)
    # Aqui você pode testar a conexão para garantir que está funcionando.
    # Ex: for m in genai.list_models(): print(m.name)

def analisar_empresa(empresa, df_dados):
    """
    Realiza a análise de uma empresa usando um modelo de IA.
    """
    dados_empresa = df_dados[df_dados['Empresa'] == empresa]
    if dados_empresa.empty:
        return "Empresa não encontrada nos dados."

    dados = dados_empresa.iloc[0].to_dict()

    prompt = f"""
    Você é um analista de crédito experiente. Analise a situação da empresa {dados['Empresa']} para determinar o risco de crédito.
    Dados Financeiros:
    - Receita Anual: R${dados['Receita Anual']}
    - Dívida Total: R${dados['Dívida Total']}
    - Prazo Médio de Pagamento: {dados['Prazo de Pagamento (dias)']} dias
    - Setor: {dados['Setor']}
    - Rating de Crédito: {dados['Rating']}
    Notícias Recentes:
    {dados['Notícias Recentes']}

    Gere uma análise concisa, destacando os riscos e oportunidades. Inclua uma recomendação preliminar (aprovado ou recusado).
    """

    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Erro ao gerar a análise: {e}"
    
    
# Script principal
if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    configurar_ia(api_key)
    
      # Ou outro formato



    # while True:
    #     empresa_para_analisar = input("\nDigite o nome da empresa para análise (ou 'sair' para fechar): ")
    #     if empresa_para_analisar.lower() == 'sair':
    #         break
            
    #     escloher_formato = input("1 = .csv \n2 = .json \n3 = .parquet\n4 = .xml\nEscolha um formato de arquivo: \n")
    #     if escloher_formato == '1':
    #         caminho_dados = "dadoscreditoficticios.csv"
    #     elif escloher_formato == '2':
    #         caminho_dados = "dadoscreditoficticios.json"
    #     elif escloher_formato == '3':
    #         caminho_dados = "dadoscreditoficticios.parquet"
    #     elif escloher_formato == '4':
    #         caminho_dados = "dadoscreditoficticios.xml"
    #     else:
    #         raise "Digite uma das opções de formato acima"
            
    #     df_empresas = carregar_dados(caminho_dados)
    #     analise = analisar_empresa(empresa_para_analisar, df_empresas)
    #     print("----------------- Análise do Assistente -----------------")
    #     print(analise)
    #     print("---------------------------------------------------------")