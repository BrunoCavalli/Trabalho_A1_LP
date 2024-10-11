import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency

# Carrega o dataset
df = pd.read_csv("./Data/data_saeb.csv", low_memory=False)

# Remove linhas com valores ausentes
df_sea_na = df.dropna()


def hipotese_4_LP():
    """
    Explora a relação entre tipo de escola (qualitativa) e a média dos alunos em Língua Portuguesa (Media_LP).

    A função filtra as respostas válidas ('A', 'B', 'C'), exibe a contagem dessas categorias e gera um boxplot
    para visualizar a relação entre essas categorias e a média de LP dos alunos.
    """
    # Filtrando valores inválidos da coluna 'Respostas_Pais'
    categorias_validas = ['A', 'B', 'C']
    df_filtrado = df_sea_na[df_sea_na['Tipo_Escola'].isin(categorias_validas)]

    # Exibe a contagem de cada categoria
    print(df_filtrado["Tipo_Escola"].value_counts())

    # Gera o boxplot para visualizar a relação entre a variável qualitativa e "Media_LP"
    plt.figure()
    sns.boxplot(x=df_filtrado["Tipo_Escola"], y=df_filtrado["Media_LP"])

    # Adiciona título e rótulos
    plt.title("Distribuição da Média de LP por tipo de escola")
    plt.xlabel("Tipo de escola")
    plt.ylabel("Média de LP")




def hipotese_4_MT():
    """
    Explora a relação entre tipo de escola (qualitativa) e a média dos alunos em matematica (Media_MT).

    A função filtra as respostas válidas ('A', 'B', 'C'), exibe a contagem dessas categorias e gera um boxplot
    para visualizar a relação entre essas categorias e a média de LP dos alunos.
    """
    # Filtrando valores inválidos da coluna 'Respostas_Pais'
    categorias_validas = ['A', 'B', 'C']
    df_filtrado = df_sea_na[df_sea_na['Tipo_Escola'].isin(categorias_validas)]

    # Exibe a contagem de cada categoria
    print(df_filtrado["Tipo_Escola"].value_counts())

    # Gera o boxplot para visualizar a relação entre a variável qualitativa e "Media_LP"
    plt.figure()
    sns.boxplot(x=df_filtrado["Tipo_Escola"], y=df_filtrado["Media_MT"])

    # Adiciona título e rótulos
    plt.title("Distribuição da Média de MT por tipo de escola")
    plt.xlabel("Tipo de escola")
    plt.ylabel("Média de MT")


plt.show()
