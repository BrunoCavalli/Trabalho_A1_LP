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

def hipotese_3_regiao_media_boxplot():
    """
    Gera um boxplot para visualizar a relação entre a região da escola (tratada como categoria)
    e a média de desempenho dos alunos (coluna 'Media').
    """
    try:
        # Converte a coluna 'Regiao' para categórica
        df_sea_na["Regiao"] = df_sea_na["Regiao"].astype('category')

        # Gera o boxplot para visualizar a relação entre a Região da Escola e a Média
        plt.figure()
        sns.boxplot(x="Regiao", y="Media", data=df_sea_na)

        # Adiciona título e rótulos
        plt.title("Boxplot: Região da Escola vs Média")
        plt.xlabel("Região da Escola")
        plt.ylabel("Média")

    except KeyError as e:
        print(f"Erro de chave: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

def hipotese_3_UF_media():
    """
    Gera um boxplot para visualizar a relação entre a UF da escola (tratada como categoria)
    e a média de desempenho dos alunos (coluna 'Media').
    """
    try:
        # Converte a coluna 'UF' para categórica
        df_sea_na['UF'] = df_sea_na['UF'].astype('category')

        # Gera o boxplot
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='UF', y='Media', data=df_sea_na)

        # Adiciona título e rótulos
        plt.title('Distribuição da Média por UF')
        plt.xlabel('UF')
        plt.ylabel('Média')

    except KeyError as e:
        print(f"Erro de chave: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

def hipotese_3_2_regiao_nivel_socio():
    """
    Gera uma tabela de contingência entre o nível socioeconômico (qualitativa) e a região da escola (qualitativa).
    """
    try:
        # Filtrando valores não nulos nas colunas 'Regiao' e 'Nivel_Socioeconomico'
        df_filtrado = df_sea_na[df_sea_na["Regiao"].notna() & df_sea_na["Nivel_Socioeconomico"].notna()]

        # Exibe a contagem de cada categoria de 'Regiao'
        print(df_filtrado["Regiao"].value_counts())

        # Gera a tabela de contingência
        tabela_contingencia = pd.crosstab(df_filtrado["Nivel_Socioeconomico"], df_filtrado["Regiao"])
        print("Tabela de Contingência:\n", tabela_contingencia)

        # Visualizar a tabela de contingência com um heatmap
        plt.figure()
        sns.heatmap(tabela_contingencia, annot=True, cmap="Blues", cbar=True)
        plt.title("Heatmap - Associação entre Nível Socioeconômico e Região da Escola")
        plt.xlabel("Região da Escola")
        plt.ylabel("Nível Socioeconômico")

    except KeyError as e:
        print(f"Erro de chave: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

def hipotese_3_3():
    """
    Explora a correlação entre a localização da escola (coluna 'Localizacao') e a média de desempenho dos alunos (coluna 'Media').
    """
    try:
        # Converte a coluna 'Localizacao' para categórica
        df_sea_na['Localizacao'] = df_sea_na['Localizacao'].astype('category')

        # Calcula a correlação entre 'Localizacao' e 'Media'
        correlacao = df_sea_na["Localizacao"].corr(df["Media"])
        print(f"Correlação entre 'Localizacao' e 'Media': {correlacao}")

        # Gera o boxplot
        plt.figure(figsize=(10, 6))
        sns.boxplot(x='Localizacao', y='Media', data=df_sea_na)
        plt.title('Distribuição da Média por Localizacao')
        plt.xlabel('Localizacao')
        plt.ylabel('Média')

    except KeyError as e:
        print(f"Erro de chave: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

