import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Carrega o dataset
try:
    df = pd.read_csv("./Data/data_saeb.csv", low_memory=False)
except FileNotFoundError:
    print("Erro: Arquivo não encontrado. Verifique o caminho do arquivo.")
except Exception as e:
    print(f"Erro inesperado: {e}")

# Remove linhas com valores ausentes
df_sea_na = df.dropna()

def plot_boxplot_outliers(data, x_col, y_col, title, output_path):
    """
    Gera boxplots com pontos atípicos destacados: verde para acima do limite superior
    e vermelho para abaixo do limite inferior.
    """
    try:
        plt.figure(figsize=(12, 6))

        # Gerar o boxplot sem os outliers padrão, com uma cor fixa para as caixas
        ax = sns.boxplot(
            x=x_col, y=y_col, data=data, showfliers=False, color="lightblue"
        )

        # Calcula os limites superior e inferior de cada boxplot
        grouped = data.groupby(x_col)[y_col]
        q1 = grouped.quantile(0.25)
        q3 = grouped.quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        # Adiciona os outliers coloridos
        for i, category in enumerate(grouped.groups.keys()):
            y_data = data[data[x_col] == category][y_col]
            x_positions = [i] * len(y_data)

            # Define as cores dos outliers
            outliers_above = y_data > upper_bound[category]
            outliers_below = y_data < lower_bound[category]

            plt.scatter(
                np.array(x_positions)[outliers_above],
                y_data[outliers_above],
                color="green",
                label="Acima" if i == 0 else "",
            )
            plt.scatter(
                np.array(x_positions)[outliers_below],
                y_data[outliers_below],
                color="red",
                label="Abaixo" if i == 0 else "",
            )

        plt.title(title)
        plt.xlabel(x_col)
        plt.ylabel(y_col)
        plt.legend(loc="upper right")
        plt.tight_layout()
        plt.savefig(output_path)
        plt.show()

    except KeyError as e:
        print(f"Erro de chave: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

# Função 1 - Relação entre Matriculados e Média
def hipotese_2():
    df_sea_na["Matriculados"] = pd.cut(df_sea_na["Num_Matriculados"], bins=10)
    plot_boxplot_outliers(
        df_sea_na,
        "Matriculados",
        "Media",
        "Relação entre Matriculados e Média",
        "./Graphs/boxplot_matriculados.png",
    )

# Função 2 - Relação entre Taxa de Participação e Média
def hipotese_2_2():
    df_sea_na["Participacao"] = pd.cut(df_sea_na["Taxa_Participacao"], bins=5)
    plot_boxplot_outliers(
        df_sea_na,
        "Participacao",
        "Media",
        "Relação entre Taxa de Participação e Média",
        "./Graphs/boxplot_participacao.png",
    )

# Chama ambas as funções
hipotese_2()
hipotese_2_2()