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
        categorias_validas = ['A', 'B', 'C']
        df_filtrado = df_sea_na[df_sea_na['Respostas_Pais'].isin(categorias_validas) &
                                df_sea_na['Taxa_Reprovacao'].isin(categorias_validas)]

        tabela_contingencia = pd.crosstab(df_filtrado['Respostas_Pais'], df_filtrado['Taxa_Reprovacao'])
        print("Tabela de Contingência:\n", tabela_contingencia)

        plt.figure(figsize=(12, 8))
        sns.heatmap(tabela_contingencia, annot=True, fmt="d", cmap="Blues", cbar=True)
        plt.title("Heatmap - Association Between Parental Encouragement to Study and Failure Rates", 
                  loc="center",
                  pad=20,
                  fontweight="bold"
        )

        # Ajustar margens para espaço suficiente nos eixos
        plt.subplots_adjust(left=0.3, right=0.9, top=0.85, bottom=0.15)

        # Títulos dos eixos em negrito
        plt.xlabel("Have you already repeated a year?", fontweight="bold")
        plt.ylabel("How often do your parents or guardians \nusually encourage you to study?", 
                   fontweight="bold", 
                   labelpad=20)

        # Rótulos do eixo X
        plt.xticks(
            ticks=np.arange(len(tabela_contingencia.columns)) + 0.5,
            labels=["Never", "Just once", "More than once"]
        )

        # Rótulos do eixo Y (copiando formatação do eixo X)
        plt.yticks(
            ticks=np.arange(len(tabela_contingencia.index)) + 0.5,
            labels=["Never or\nalmost never", "Sometimes", "Always or\nalmost always"],
            rotation=0  # Deixa o texto do eixo Y alinhado horizontalmente como no eixo X
        )

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
    Explora a associação entre 'Respostas_Pais' e 'Taxa_Abandono' (variáveis qualitativas).

    A função cria uma tabela de contingência, visualiza a relação com um heatmap e calcula o
    teste qui-quadrado para verificar a independência entre as variáveis.
    """
    try:
        categorias_validas = ['A', 'B', 'C']
        df_filtrado = df_sea_na[df_sea_na['Respostas_Pais'].isin(categorias_validas) &
                                df_sea_na['Taxa_Abandono'].isin(categorias_validas)]

        tabela_contingencia = pd.crosstab(df_filtrado['Respostas_Pais'], df_filtrado['Taxa_Abandono'])
        print("Tabela de Contingência:\n", tabela_contingencia)

        plt.figure(figsize=(12, 8))
        sns.heatmap(tabela_contingencia, annot=True, fmt="d", cmap="Blues", cbar=True)
        plt.title("Heatmap - Association Between Parental Encouragement to Study and Dropout Rates", 
                  loc="center",
                  pad=20,
                  fontweight="bold"
        )

        # Ajustar margens para espaço suficiente nos eixos
        plt.subplots_adjust(left=0.3, right=0.9, top=0.85, bottom=0.15)

        # Títulos dos eixos em negrito
        plt.xlabel("Have you ever dropped out of school and stopped attending until the end of the school year?", fontweight="bold")
        plt.ylabel("How often do your parents or guardians \nusually encourage you to study?", 
                   fontweight="bold", 
                   labelpad=20)

        # Rótulos do eixo X
        plt.xticks(
            ticks=np.arange(len(tabela_contingencia.columns)) + 0.5,
            labels=["Never", "Just once", "More than once"]
        )

        # Rótulos do eixo Y (copiando formatação do eixo X)
        plt.yticks(
            ticks=np.arange(len(tabela_contingencia.index)) + 0.5,
            labels=["Never or\nalmost never", "Sometimes", "Always or\nalmost always"],
            rotation=0  # Deixa o texto do eixo Y alinhado horizontalmente como no eixo X
        )

        chi2, p, dof, expected = chi2_contingency(tabela_contingencia)
        print(f"Estatística qui-quadrado: {chi2}")
        print(f"Valor-p: {p}")
        if p < 0.05:
            print("As variáveis estão associadas (rejeita-se a hipótese nula de independência).")
        else:
            print("As variáveis não estão associadas (não se rejeita a hipótese nula).")

        plt.savefig("./Graphs/heatmap_abandono")

    except KeyError as e:
        print(f"Erro de chave: {e}. Verifique se as colunas estão corretamente nomeadas no dataset.")
    except Exception as e:
        print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    hipotese_1_reprovacao()
    hipotese_1_abandono()
