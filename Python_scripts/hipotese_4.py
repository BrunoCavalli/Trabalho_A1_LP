import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency

# Carrega o dataset
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

# Remove linhas com valores ausentes
df_sea_na = df.dropna()

def hipotese_4():
    """
    Explora a relação entre o tipo de escola (qualitativa) e a média dos alunos em uma disciplina (coluna 'Media').

    A função:
    - Filtra as respostas válidas ('A', 'B', 'C') da coluna 'Tipo_Escola'.
    - Exibe a contagem de categorias válidas.
    - Gera um boxplot para visualizar a relação entre o tipo de escola e a média dos alunos.
    """
    try:
        # Filtrando valores inválidos da coluna 'Tipo_Escola'
        categorias_validas = ['A', 'B', 'C']
        df_filtrado = df_sea_na[df_sea_na['Tipo_Escola'].isin(categorias_validas)]

        # Exibe a contagem de cada categoria
        print(df_filtrado["Tipo_Escola"].value_counts())

        # Verifica se a coluna 'Media' está presente no dataframe
        if 'Media' not in df_filtrado.columns:
            raise KeyError("Erro: A coluna 'Media' não foi encontrada no dataset.")

        # Gera o boxplot para visualizar a relação entre a variável qualitativa e "Media"
        plt.figure()
        sns.boxplot(x=df_filtrado["Tipo_Escola"], y=df_filtrado["Media"])

        # Adiciona título e rótulos
        plt.title("Distribuição da Média por tipo de escola")
        plt.xlabel("Tipo de escola")
        plt.ylabel("Média")

        plt.savefig("./Graphs/boxplot_tipo")

    except KeyError as e:
        print(f"Erro de chave: {e}")
    except ValueError as e:
        print(f"Erro de valor: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

