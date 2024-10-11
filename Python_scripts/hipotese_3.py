import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency


# Carrega o dataset
df = pd.read_csv("./Data/data_saeb.csv", low_memory=False)

# Remove linhas com valores ausentes
df_sea_na = df.dropna()



def hipotese_3_regiao_media_boxplot():
    """
    Gera um boxplot para visualizar a relação entre a região da escola (tratada como categoria)
    e a média de desempenho dos alunos (Média).
    """
    # Converte a coluna 'Regiao_Escola' para categórica
    df_sea_na["Regiao"] = df_sea_na["Regiao"].astype('category')

    # Gera o boxplot para visualizar a relação entre a Região da Escola e a Média
    plt.figure()
    sns.boxplot(x="Regiao", y="Media", data=df_sea_na)

    # Adiciona título e rótulos
    plt.title("Boxplot: Região da Escola vs Média")
    plt.xlabel("Região da Escola")
    plt.ylabel("Média")




def hipotese_3_UF_media():
    """
    Gera um boxplot para visualizar a relação entre a UF da escola (tratada como categoria)
    e a média de desempenho dos alunos (Média).
    """
    df_sea_na['UF'] = df_sea_na['UF'].astype('category')
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='UF', y='Media', data=df_sea_na)
    plt.title('Distribuição da Média por UF')
    plt.xlabel('UF')
    plt.ylabel('Média')

def hipotese_3_2_regiao_nivel_socio():
    """
    Gera uma tabela de contigencia com o nivel socio economico(qualitativa) e a regiao da escola(qualitativa)
    """

    # Filtrando valores inválidos da coluna 'Regiao' e 'Nivel_Socioeconomico'
    df_filtrado = df_sea_na[df_sea_na["Regiao"].notna() & df_sea_na["Nivel_Socioeconomico"].notna()]

    # Exibe a contagem de cada categoria
    print(df_filtrado["Regiao"].value_counts())

    # Gera a tabela de contingência
    tabela_contingencia = pd.crosstab(df_filtrado["Nivel_Socioeconomico"], df_filtrado["Regiao"])
    print("Tabela de Contingência:\n", tabela_contingencia)
    
    # Visualizar a tabela de contingência com um heatmap
    plt.figure()
    sns.heatmap(tabela_contingencia, annot=True, cmap="Blues", cbar=True)
    plt.title("Heatmap - Associação entre Nivel Socio Economico e Regiao da Escola")
    plt.xlabel("Regiao da Escola")
    plt.ylabel("Nivel Socio Economico")

def hipotese_3_3():

    df_sea_na['Localizacao'] = df_sea_na['Localizacao'].astype('category')

    correlacao = df_sea_na["Localizacao"].corr(df["Media"])
    print(f"Correlação entre 'Localizacao' e 'Media': {correlacao}")

    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Localizacao', y='Media', data=df_sea_na)
    plt.title('Distribuição da Média por Localizacao')
    plt.xlabel('Localizacao')
    plt.ylabel('Média')

plt.show()
