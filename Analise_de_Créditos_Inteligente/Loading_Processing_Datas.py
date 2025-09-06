import pandas as pd
import os
import xml.etree.ElementTree as ET

def carregar_dados(caminho_arquivo):
    """
    Carrega os dados de empresas a partir de um arquivo,
    identificando o formato pela extensão e lidando com JSON Lines e XML.
    """
    if not os.path.exists(caminho_arquivo):
        print(f"Erro: O arquivo {caminho_arquivo} não foi encontrado.")
        return None

    extensao = caminho_arquivo.split('.')[-1].lower()

    try:
        if extensao == 'csv':
            return pd.read_csv(caminho_arquivo)
        elif extensao == 'json':
            return pd.read_json(caminho_arquivo, lines=True)
        elif extensao == 'parquet':
            return pd.read_parquet(caminho_arquivo)
        elif extensao == 'xml':
            tree = ET.parse(caminho_arquivo)
            root = tree.getroot()
            lista_empresas = []
            
            # O arquivo usa a tag 'row' para cada empresa
            for row_elem in root.findall('row'):
                # Usar findtext() é mais seguro e evita o erro 'NoneType'
                empresa = {
                    'Empresa': row_elem.findtext('Empresa'),
                    'Receita Anual': int(row_elem.findtext('Receita_Anual')) if row_elem.findtext('Receita_Anual') else None,
                    'Dívida Total': int(row_elem.findtext('Dívida_Total')) if row_elem.findtext('Dívida_Total') else None,
                    'Prazo de Pagamento (dias)': int(row_elem.findtext('Prazo_de_Pagamento_dias')) if row_elem.findtext('Prazo_de_Pagamento_dias') else None,
                    'Setor': row_elem.findtext('Setor'),
                    'Rating': row_elem.findtext('Rating'),
                    'Notícias Recentes': row_elem.findtext('Notícias_Recentes'),
                }
                lista_empresas.append(empresa)
            return pd.DataFrame(lista_empresas)
        else:
            print(f"Formato de arquivo '{extensao}' não suportado.")
            return None
    except Exception as e:
        print(f"Erro ao carregar o arquivo {caminho_arquivo}: {e}")
        return None

# Lembre-se de rodar 'pip install pyarrow' para que o arquivo .parquet funcione.
# Depois, você pode testar o código da seguinte forma:
df_json = carregar_dados('dadoscreditoficticios.json')
df_parquet = carregar_dados('dadoscreditoficticios.parquet')