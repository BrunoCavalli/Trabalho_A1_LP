import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency
import os


if not os.path.exists("Graphs"):
    os.makedirs("Graphs")

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

# Remove linhas com valores ausentes
df_sea_na = df.dropna()

def hipotese_1_reprovacao():
    """
    Explora a associação entre 'Respostas_Pais' e 'Taxa_Reprovacao' (variáveis qualitativas).

    A função cria uma tabela de contingência, visualiza a relação com um heatmap e calcula o
    teste qui-quadrado para verificar a independência entre as variáveis.
    """
    try:
        # Filtrar as categorias válidas
        categorias_validas = ['A', 'B', 'C']
        df_filtrado = df_sea_na[df_sea_na['Respostas_Pais'].isin(categorias_validas) &
                                df_sea_na['Taxa_Reprovacao'].isin(categorias_validas)]

        # Criar uma tabela de contingência
        tabela_contingencia = pd.crosstab(df_filtrado['Respostas_Pais'], df_filtrado['Taxa_Reprovacao'])
        print("Tabela de Contingência:\n", tabela_contingencia)

        # Visualizar a tabela de contingência com um heatmap
        plt.figure()
        sns.heatmap(tabela_contingencia, annot=True, cmap="Blues", cbar=True)
        plt.title("Heatmap - Associação entre Respostas dos Pais e Taxa de Reprovação")
        plt.xlabel("Taxa de Reprovação")
        plt.ylabel("Respostas dos Pais")

        # Teste qui-quadrado para verificar independência entre as variáveis
        chi2, p, dof, expected = chi2_contingency(tabela_contingencia)
        print(f"Estatística qui-quadrado: {chi2}")
        print(f"Valor-p: {p}")
        if p < 0.05:
            print("As variáveis estão associadas (rejeita-se a hipótese nula de independência).")
        else:
            print("As variáveis não estão associadas (não se rejeita a hipótese nula).")

        plt.savefig("./Graphs/heatmap_reprovacao")

    except KeyError as e:
        print(f"Erro de chave: {e}. Verifique se as colunas estão corretamente nomeadas no dataset.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

def hipotese_1_abandono():
    """
    Explora a relação entre as respostas dos pais (qualitativa) e a taxa de abandono (qualitativa).

    A função filtra as respostas válidas ('A', 'B', 'C'), exibe a contagem dessas categorias e gera um heatmap
    para visualizar a relação entre essas categorias e a taxa de abandono.
    """
    try:
        # Filtrando valores inválidos da coluna 'Respostas_Pais' e 'Taxa_Abandono'
        categorias_validas = ['A', 'B', 'C']
        df_filtrado = df_sea_na[df_sea_na['Respostas_Pais'].isin(categorias_validas) & 
                                df_sea_na['Taxa_Abandono'].isin(categorias_validas)]

        # Exibe a contagem de cada categoria
        print(df_filtrado["Respostas_Pais"].value_counts())

        # Criar a tabela de contingência
        tabela_contingencia = pd.crosstab(df_filtrado['Respostas_Pais'], df_filtrado['Taxa_Abandono'])
        print("Tabela de Contingência:\n", tabela_contingencia)

        # Visualizar a tabela de contingência com um heatmap
        plt.figure()
        sns.heatmap(tabela_contingencia, annot=True, cmap="Blues", cbar=True)
        plt.title("Heatmap - Associação entre Respostas dos Pais e Taxa de Abandono")
        plt.xlabel("Taxa de Abandono")
        plt.ylabel("Respostas dos Pais")

        plt.savefig("./Graphs/heatmap_abandono")

    except KeyError as e:
        print(f"Erro de chave: {e}. Verifique se as colunas estão corretamente nomeadas no dataset.")
    except Exception as e:
        print(f"Erro inesperado: {e}")


