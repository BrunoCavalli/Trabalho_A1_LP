import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency

# Carrega o dataset
df = pd.read_csv("./Data/data_saeb.csv", low_memory=False)

# Remove linhas com valores ausentes
df_sea_na = df.dropna()


def hipotese_2_LP():
    """
    Explora a relação entre o número de matriculados e a média dos alunos em Língua Portuguesa (Media_LP).

    A função categoriza a coluna 'Num_Matriculados' em intervalos (bins), exibe a contagem de matriculados por categoria
    e gera um boxplot para visualizar a relação entre as categorias de matriculados e a média dos alunos em LP, alem de calcular o correl.
    """
    # Categorizando a coluna "Num_Matriculados" em intervalos (bins)
    df_sea_na["Matriculados"] = pd.cut(df_sea_na["Num_Matriculados"], bins=10)

    # Exibe a contagem de categorias de "Matriculados"
    print(df_sea_na[["Num_Matriculados", "Matriculados"]].value_counts())

    # Calcula a correlação entre "Num_Matriculados" e "Media_LP"
    correlacao = df_sea_na["Num_Matriculados"].corr(df["Media_LP"])
    print(f"Correlação entre 'Num_Matriculados' e 'Media_LP': {correlacao}")

    # Gera o boxplot para visualizar a relação entre as categorias de "Matriculados" e "Media_LP"
    plt.figure()
    sns.boxplot(x=df_sea_na["Matriculados"], y="Media_LP", data=df)
    plt.title("Relação entre Matriculados e Média de LP")


def hipotese_2_MT():
    """
    Explora a relação entre o número de matriculados e a média dos alunos em Matemática (Media_MT).

    A função categoriza a coluna 'Num_Matriculados' em intervalos (bins), exibe a contagem de matriculados por categoria
    e gera um boxplot para visualizar a relação entre as categorias de matriculados e a média dos alunos em Matemática, alem de calcular o correl.
    """
    # Categorizando a coluna "Num_Matriculados" em intervalos (bins)
    df_sea_na["Matriculados"] = pd.cut(df_sea_na["Num_Matriculados"], bins=10)

    # Exibe a contagem de categorias de "Matriculados"
    print(df_sea_na[["Num_Matriculados", "Matriculados"]].value_counts())

    # Calcula a correlação entre "Num_Matriculados" e "Media_MT"
    correlacao = df_sea_na["Num_Matriculados"].corr(df["Media_MT"])
    print(f"Correlação entre 'Num_Matriculados' e 'Media_MT': {correlacao}")

    # Gera o boxplot para visualizar a relação entre as categorias de "Matriculados" e "Media_MT"
    plt.figure()
    sns.boxplot(x=df_sea_na["Matriculados"], y="Media_MT", data=df)
    plt.title("Relação entre Matriculados e Média de Matemática")



def hipotese_2_2_LP():
    """
    Explora a relação entre a Taxa de Participação e a média dos alunos em Língua Portuguesa (Media_LP).
    """
    # Categorizando a coluna "Taxa_Participacao" em intervalos (bins)
    df_sea_na["Matriculados"] = pd.cut(df_sea_na["Taxa_Participacao"], bins=5)

    # Exibe a contagem de categorias de "Taxa_Participacao"
    print(df_sea_na[["Taxa_Participacao", "Matriculados"]].value_counts())

    # Calcula a correlação entre "Taxa_Participacao" e "Media_LP"
    correlacao = df_sea_na["Taxa_Participacao"].corr(df["Media_LP"])
    print(f"Correlação entre 'Taxa_Participacao' e 'Media_LP': {correlacao}")

    # Cria uma nova figura para o boxplot
    plt.figure()
    sns.boxplot(x=df_sea_na["Matriculados"], y="Media_LP", data=df)
    plt.title("Relação entre Taxa de Participação e Média de LP")


def hipotese_2_2_MT():
    """
    Explora a relação entre a Taxa de Participação e a média dos alunos em Matemática (Media_MT).
    """
    # Categorizando a coluna "Taxa_Participacao" em intervalos (bins)
    df_sea_na["Matriculados"] = pd.cut(df_sea_na["Taxa_Participacao"], bins=5)

    # Exibe a contagem de categorias de "Taxa_Participacao"
    print(df_sea_na[["Taxa_Participacao", "Matriculados"]].value_counts())

    # Calcula a correlação entre "Taxa_Participacao" e "Media_MT"
    correlacao = df_sea_na["Taxa_Participacao"].corr(df["Media_MT"])
    print(f"Correlação entre 'Taxa_Participacao' e 'Media_MT': {correlacao}")

    # Cria uma nova figura para o boxplot
    plt.figure()
    sns.boxplot(x=df_sea_na["Matriculados"], y="Media_MT", data=df)
    plt.title("Relação entre Taxa de Participação e Média de Matemática")



def hipotese_1_reprovacao():
    """
    Explora a associação entre 'Respostas_Pais' e 'Taxa_Reprovacao' (variáveis qualitativas).

    A função cria uma tabela de contingência, visualiza a relação com um heatmap e calcula o
    teste qui-quadrado para verificar a independência entre as variáveis.
    """
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


def hipotese_1_abondono():
    """
    Explora a relação entre as respostas dos pais (qualitativa) e a média dos alunos em matematica (Media_MT)

    A função filtra as respostas válidas ('A', 'B', 'C'), exibe a contagem dessas categorias e gera um boxplot
    para visualizar a relação entre essas categorias e a média de LP dos alunos.
    """
    # Filtrando valores inválidos da coluna 'Respostas_Pais'
    categorias_validas = ['A', 'B', 'C']
    df_filtrado = df_sea_na[df_sea_na['Respostas_Pais'].isin(categorias_validas) & 
                            df_sea_na['Taxa_Abandono'].isin(categorias_validas)]

    # Exibe a contagem de cada categoria
    print(df_filtrado["Respostas_Pais"].value_counts())

    tabela_contingencia = pd.crosstab(df_filtrado['Respostas_Pais'], df_filtrado['Taxa_Abandono'])
    print("Tabela de Contingência:\n", tabela_contingencia)

    # Gera o heatplot para visualizar a relação entre a variável qualitativa e "Media_MT"
    plt.figure()
    sns.heatmap(tabela_contingencia, annot=True, cmap="Blues", cbar=True)
    plt.title("Heatmap - Associação entre Respostas dos Pais e Taxa de Abandono")
    plt.xlabel("Taxa de Abandono")
    plt.ylabel("Respostas dos Pais")



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




def hipotese_3_regiao_media_boxplot_LP():
    """
    Gera um boxplot para visualizar a relação entre a região da escola (tratada como categoria)
    e a média de desempenho dos alunos (Média de LP).
    """
    # Converte a coluna 'Regiao_Escola' para categórica
    df_sea_na["Regiao"] = df_sea_na["Regiao"].astype('category')

    # Gera o boxplot para visualizar a relação entre a Região da Escola e a Média de LP
    plt.figure()
    sns.boxplot(x="Regiao", y="Media_LP", data=df_sea_na)

    # Adiciona título e rótulos
    plt.title("Boxplot: Região da Escola vs Média de LP")
    plt.xlabel("Região da Escola")
    plt.ylabel("Média de LP")



def hipotese_3_regiao_media_boxplot_MT():
    """
    Gera um boxplot para visualizar a relação entre a região da escola (tratada como categoria)
    e a média de desempenho dos alunos (Média de MT).
    """
    # Converte a coluna 'Regiao_Escola' para categórica
    df_sea_na["Regiao"] = df_sea_na["Regiao"].astype('category')

    # Gera o boxplot para visualizar a relação entre a Região da Escola e a Média de MT
    plt.figure()
    sns.boxplot(x="Regiao", y="Media_MT", data=df_sea_na)

    # Adiciona título e rótulos
    plt.title("Boxplot: Região da Escola vs Média de MT")
    plt.xlabel("Região da Escola")
    plt.ylabel("Média de MT")


def hipotese_3_UF_media_LP():
    """
    Gera um boxplot para visualizar a relação entre a UF da escola (tratada como categoria)
    e a média de desempenho dos alunos (Média de MT).
    """
    df_sea_na['UF'] = df_sea_na['UF'].astype('category')
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='UF', y='Media_MT', data=df_sea_na)
    plt.title('Distribuição da Média de Matemática por UF')
    plt.xlabel('UF')
    plt.ylabel('Média de Matemática')

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

plt.show()
