import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency

# Importa funções de scripts externos
try:
    from Python_scripts.hipotese_1 import hipotese_1_reprovacao, hipotese_1_abondono
    from Python_scripts.hipotese_2 import hipotese_2, hipotese_2_2
    from Python_scripts.hipotese_3 import (hipotese_3_regiao_media_boxplot, 
                                           hipotese_3_UF_media, 
                                           hipotese_3_2_regiao_nivel_socio, 
                                           hipotese_3_3)
    from Python_scripts.hipotese_4 import hipotese_4
except ImportError as e:
    print(f"Erro ao importar funções: {e}")

# Carrega o dataset com tratamento de erros
try:
    df = pd.read_csv("./Data/data_saeb.csv", low_memory=False)
except FileNotFoundError:
    print("Erro: Arquivo não encontrado. Verifique o caminho do arquivo.")
except pd.errors.EmptyDataError:
    print("Erro: O arquivo está vazio.")
except pd.errors.ParserError:
    print("Erro: Falha ao analisar o arquivo. Verifique a formatação do CSV.")
except Exception as e:
    print(f"Erro inesperado ao carregar o dataset: {e}")

# Executa as funções que realizam as análises de cada hipótese com tratamento de erro
def executa_analises():
    """
    Executa as análises definidas para cada hipótese com tratamento de erro para garantir
    que erros durante a execução sejam tratados adequadamente.
    """
    try:
        hipotese_1_reprovacao()
    except Exception as e:
        print(f"Erro ao executar hipotese_1_reprovacao: {e}")
    
    try:
        hipotese_1_abondono()
    except Exception as e:
        print(f"Erro ao executar hipotese_1_abondono: {e}")
    
    try:
        hipotese_2()
    except Exception as e:
        print(f"Erro ao executar hipotese_2: {e}")
    
    try:
        hipotese_2_2()
    except Exception as e:
        print(f"Erro ao executar hipotese_2_2: {e}")
    
    try:
        hipotese_3_regiao_media_boxplot()
    except Exception as e:
        print(f"Erro ao executar hipotese_3_regiao_media_boxplot: {e}")
    
    try:
        hipotese_3_UF_media()
    except Exception as e:
        print(f"Erro ao executar hipotese_3_UF_media: {e}")
    
    try:
        hipotese_3_2_regiao_nivel_socio()
    except Exception as e:
        print(f"Erro ao executar hipotese_3_2_regiao_nivel_socio: {e}")
    
    try:
        hipotese_3_3()
    except Exception as e:
        print(f"Erro ao executar hipotese_3_3: {e}")
    
    try:
        hipotese_4()
    except Exception as e:
        print(f"Erro ao executar hipotese_4: {e}")

# Chama a função para executar todas as análises
executa_analises()

# Exibe os gráficos gerados pelas análises
plt.show()
