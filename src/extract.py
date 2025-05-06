import pandas as pd
import os 

# Função para ler o arquivo Excel e transformar em DataFrame

def ler_arquivo():

    try:
        arquivo_xls = 'Superstore.xls'
        pasta = 'data'
        if arquivo_xls.endswith('.xls'):
            caminho_arquivo = os.path.join(os.getcwd(), pasta, arquivo_xls)
            pd.set_option('display.max_columns', None)
            df = pd.read_excel(caminho_arquivo)
            return df
        else:
            raise ValueError("Formato de arquivo não suportado. Use Supertore.xls ")

    except FileNotFoundError:
        print('Arquivo não encontrado')
        return None
    
    except Exception as e:
        print(f'Ocorreu um erro: {e}')
        return None

arquivo_lido = ler_arquivo()


