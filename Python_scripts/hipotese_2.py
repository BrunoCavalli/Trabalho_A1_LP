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

def hipotese_2():
    """
    Explora a relação entre o número de matriculados e a média dos alunos.

    A função categoriza a coluna 'Num_Matriculados' em intervalos (bins), exibe a contagem de matriculados por categoria
    e gera um boxplot para visualizar a relação entre as categorias de matriculados e a média dos alunos, além de calcular a correlação.
    """
    try:
        # Categorizando a coluna "Num_Matriculados" em intervalos (bins)
        df_sea_na["Matriculados"] = pd.cut(df_sea_na["Num_Matriculados"], bins=10)

        # Exibe a contagem de categorias de "Matriculados"
        print(df_sea_na[["Num_Matriculados", "Matriculados"]].value_counts())

        # Calcula a correlação entre "Num_Matriculados" e "Media"
        correlacao = df_sea_na["Num_Matriculados"].corr(df["Media"])
        print(f"Correlação entre 'Num_Matriculados' e 'Media': {correlacao}")

        # Gera o boxplot para visualizar a relação entre as categorias de "Matriculados" e "Media"
        plt.figure()
        sns.boxplot(x=df_sea_na["Matriculados"], y="Media", data=df)
        plt.title("Relação entre Matriculados e Média")
        plt.xlabel("Categorias de Matriculados")
        plt.ylabel("Média")

        plt.savefig("./Graphs/boxplot_matric")

    except KeyError as e:
        print(f"Erro de chave: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

def hipotese_2_2():
    """
    Explora a relação entre a Taxa de Participação e a média dos alunos.
    """
    try:
        # Categorizando a coluna "Taxa_Participacao" em intervalos (bins)
        df_sea_na["Matriculados"] = pd.cut(df_sea_na["Taxa_Participacao"], bins=5)

        # Exibe a contagem de categorias de "Taxa_Participacao"
        print(df_sea_na[["Taxa_Participacao", "Matriculados"]].value_counts())

        # Calcula a correlação entre "Taxa_Participacao" e "Media"
        correlacao = df_sea_na["Taxa_Participacao"].corr(df["Media"])
        print(f"Correlação entre 'Taxa_Participacao' e 'Media': {correlacao}")

        # Gera o boxplot para visualizar a relação entre as categorias de "Taxa_Participacao" e "Media"
        plt.figure()
        sns.boxplot(x=df_sea_na["Matriculados"], y="Media", data=df)
        plt.title("Relação entre Taxa de Participação e Média")
        plt.xlabel("Categorias de Taxa de Participação")
        plt.ylabel("Média")

        plt.savefig("./Graphs/boxplot_part")

    except KeyError as e:
        print(f"Erro de chave: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")







