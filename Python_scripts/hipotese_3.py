import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency
import os

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

region_order = ["N", "NE", "SE", "S", "CO"]
df_sea_na["Regiao"] = pd.Categorical(df_sea_na["Regiao"], categories=region_order, ordered=True)

# Definir a ordem personalizada dos estados
uf_order = [
    "AC", "AM", "PA", "RO", "TO",  # Região Norte
    "AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE",  # Região Nordeste
    "ES", "MG", "RJ", "SP",  # Região Sudeste
    "PR", "RS", "SC",  # Região Sul
    "DF", "GO", "MS", "MT"  # Região Centro-Oeste
]
df_sea_na["UF"] = pd.Categorical(df_sea_na["UF"], categories=uf_order, ordered=True)

# Funções de visualização
def hipotese_3_regiao_media_violinplot():
    try:
        plt.figure()
        sns.violinplot(
            x="Regiao", y="Media", data=df_sea_na, 
            bw_adjust=0.5, cut=1, linewidth=1, palette="Set3"
        )
        plt.title("Violinplot: Região da Escola vs Média")
        plt.xlabel("Região da Escola")
        plt.ylabel("Média")
        plt.savefig("./Graphs/violinplot_regiao_media")
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
        sns.violinplot(x='UF', y='Media', data=df_sea_na, bw_adjust=.5, cut=1, linewidth=1, palette="coolwarm")

        # Adiciona título e rótulos
        plt.title('Distribuição da Média por UF')
        plt.xlabel('UF')
        plt.ylabel('Média')

        plt.savefig("./Graphs/violinplot_uf_media")

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
        plt.figure(figsize=(10, 6))
        sns.heatmap(tabela_contingencia, annot=True, fmt="d", cmap="Blues", cbar=True)        
        plt.title("Heatmap - Associação entre Nível Socioeconômico e Região da Escola")
        plt.xlabel("Região da Escola")
        plt.ylabel("Nível Socioeconômico")



        plt.savefig("./Graphs/heatmap_regiao_socio")

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

        # Converte a coluna 'Localizacao' para códigos numéricos
        df_sea_na['Localizacao_Cod'] = df_sea_na['Localizacao'].cat.codes

        # Calcula a correlação entre 'Localizacao_Cod' e 'Media'
        correlacao = df_sea_na["Localizacao_Cod"].corr(df_sea_na["Media"])
        print(f"Correlação entre 'Localizacao' e 'Media': {correlacao}")

        # Gera o boxplot
        plt.figure(figsize=(10, 6))
        sns.violinplot(x='Localizacao', y='Media', data=df_sea_na, bw_adjust=.5, cut=1, linewidth=1, palette="coolwarm")
        plt.title('Distribuição da Média por Localizacao')
        plt.xlabel('Localizacao')
        plt.ylabel('Média')

        plt.savefig("./Graphs/violinplot_loc")

    except KeyError as e:
        print(f"Erro de chave: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")
