import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Carrega o dataset
df = pd.read_csv("./Data/data_saeb.csv")

# Remove linhas com valores ausentes
df_sea_na = df.dropna()

# Categorizando a coluna "Num_Matriculados" em intervalos (bins)
df_sea_na["Matriculados"] = pd.cut(df_sea_na["Num_Matriculados"], bins=10)

# Exibe a contagem de categorias de "Matriculados"
print(df_sea_na[["Num_Matriculados", "Matriculados"]].value_counts())

# Calcula a correlação entre "Num_Matriculados" e "Media_LP"
correlacao = df_sea_na["Num_Matriculados"].corr(df["Media_LP"])
print(f"Correlação entre 'Num_Matriculados' e 'Media_LP': {correlacao}")

# Gera o boxplot para visualizar a relação entre as categorias de "Matriculados" e "Media_LP"
sns.boxplot(x=df_sea_na["Matriculados"], y="Media_LP", data=df)
plt.show()
