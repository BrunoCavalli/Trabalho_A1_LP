import pandas as pd
import numpy as np

def load_datasets():
    """
    Carrega os datasets 'TS_ESCOLA.csv' e 'TS_ALUNO_34EM.csv' e exibe as primeiras linhas do DataFrame df2.

    Retorna:
        df2 (DataFrame): Dados das escolas.
        df3 (DataFrame): Dados dos alunos.
    """
    try:
        df2 = pd.read_csv("./Data/TS_ESCOLA.csv", sep=";", encoding="latin1")
        df3 = pd.read_csv("./Data/TS_ALUNO_34EM.csv", sep=";", encoding="latin1")
        print(df2.head())
        return df2, df3
    except FileNotFoundError as e:
        print(f"Erro: {e}. Verifique se o caminho do arquivo está correto.")
        return pd.DataFrame(), pd.DataFrame()  # Retorna DataFrames vazios em caso de erro
    except Exception as e:
        print(f"Erro ao carregar os datasets: {e}")
        return pd.DataFrame(), pd.DataFrame()

def create_dataframes(df2, df3):
    """
    Cria DataFrames para as variáveis específicas a partir dos DataFrames fornecidos.

    Retorna:
        Tupla de DataFrames contendo variáveis como 'Respostas_Pais', 'Tipo_Escola', 'Taxa_Reprovacao', etc.
    """
    try:
        id_regiao_mapping = {
            1: "N", 2: "NE", 3: "SE", 4: "S", 5: "CO"}
        uf_mapping = {
            12: 'AC', 27: 'AL', 13: 'AM', 16: 'AP', 29: 'BA', 23: 'CE', 53: 'DF',
            32: 'ES', 52: 'GO', 21: 'MA', 31: 'MG', 50: 'MS', 51: 'MT', 15: 'PA',
            25: 'PB', 26: 'PE', 22: 'PI', 41: 'PR', 33: 'RJ', 24: 'RN', 43: 'RS',
            11: 'RO', 14: 'RR', 42: 'SC', 35: 'SP', 28: 'SE', 17: 'TO'
        }

        tipo_regiao = {
            1: "Urbana", 2: "Rural"
        }



        resposta_pais = df3[["TX_RESP_Q09c"]].rename(columns={"TX_RESP_Q09c": "Respostas_Pais"})
        tipo_escola_df = df3[["TX_RESP_Q17"]].rename(columns={"TX_RESP_Q17": "Tipo_Escola"})
        taxa_reprovacao = df3[["TX_RESP_Q18"]].rename(columns={"TX_RESP_Q18": "Taxa_Reprovacao"})
        taxa_abondono = df3[["TX_RESP_Q19"]].rename(columns={"TX_RESP_Q19": "Taxa_Abandono"})
        nivel_socioeco = df2[["NIVEL_SOCIO_ECONOMICO"]].rename(columns={"NIVEL_SOCIO_ECONOMICO": "Nivel_Socioeconomico"})
        id_regiao = df2[["ID_REGIAO"]].rename(columns={"ID_REGIAO": "Regiao"})
        id_regiao["Regiao"] = id_regiao["Regiao"].map(id_regiao_mapping)
        med_lp = df2[["MEDIA_EM_LP"]].rename(columns={"MEDIA_EM_LP": "Media_LP"})
        med_mt = df2[["MEDIA_EM_MT"]].rename(columns={"MEDIA_EM_MT": "Media_MT"})
        med_geral = pd.DataFrame((df2["MEDIA_EM_LP"] + df2["MEDIA_EM_MT"]) / 2, columns=["Media"])
        num_matriculados = df2[["NU_MATRICULADOS_CENSO_EMT"]].rename(columns={"NU_MATRICULADOS_CENSO_EMT": "Num_Matriculados"})
        taxa_participacao = df2[["TAXA_PARTICIPACAO_EM"]].rename(columns={"TAXA_PARTICIPACAO_EM": "Taxa_Participacao"})
        id_localizacao = df2[["ID_LOCALIZACAO"]].rename(columns={"ID_LOCALIZACAO": "Localizacao"})
        id_localizacao["Localizacao"] = id_localizacao["Localizacao"].map(tipo_regiao)
        id_uf = df2[["ID_UF"]].rename(columns={"ID_UF": "UF"})
        id_uf["UF"] = id_uf["UF"].map(uf_mapping)

        return (resposta_pais, tipo_escola_df, nivel_socioeco, id_regiao, taxa_reprovacao, med_lp, med_mt, 
                med_geral, num_matriculados, taxa_participacao, taxa_abondono, id_localizacao, id_uf)
    except KeyError as e:
        print(f"Erro: Coluna {e} não encontrada nos DataFrames.")
        return [pd.DataFrame()] * 13

def set_indices(resposta_pais, tipo_escola_df, nivel_socioeco, id_regiao, taxa_reprovacao, med_lp, med_mt, med_geral, num_matriculados, taxa_participacao, taxa_abondono, id_localizacao, id_uf):
    """
    Define os nomes dos índices para os DataFrames fornecidos.
    """
    try:
        resposta_pais.index.name = "Resposta"
        tipo_escola_df.index.name = "Publica_Privada"
        taxa_reprovacao.index.name = "Taxa_Reprovacao"
        med_lp.index.name = "Media_LP"
        med_mt.index.name = "Media_MT"
        med_geral.index.name = "Media"
        num_matriculados.index.name = "Num_Matriculados"
        taxa_participacao.index.name = "Taxa_Participacao"
        taxa_abondono.index.name = "Taxa_Abandono"
        id_localizacao.index.name = "Localizacao"
        id_uf.index.name = "UF"
        nivel_socioeco.index.name = "Nivel"
        id_regiao.index.name = "Regiao"
    except Exception as e:
        print(f"Erro ao definir os índices: {e}")

def merge_dataframes(resposta_pais, tipo_escola_df, nivel_socioeco, id_regiao, taxa_reprovacao, med_lp, med_mt, med_geral, num_matriculados, taxa_participacao, taxa_abondono, id_localizacao, id_uf):
    """
    Mescla os DataFrames em um único DataFrame com base nos índices.

    Retorna:
        df_merged (DataFrame): DataFrame resultante da mesclagem.
    """
    try:
        df_merged = resposta_pais.merge(tipo_escola_df, left_index=True, right_index=True, how="outer") \
                       .merge(nivel_socioeco, left_index=True, right_index=True, how='outer') \
                       .merge(id_regiao, left_index=True, right_index=True, how='outer') \
                       .merge(taxa_reprovacao, left_index=True, right_index=True, how='outer') \
                       .merge(med_lp, left_index=True, right_index=True, how='outer') \
                       .merge(med_mt, left_index=True, right_index=True, how='outer') \
                       .merge(med_geral, left_index=True, right_index=True, how="outer") \
                       .merge(num_matriculados, left_index=True, right_index=True, how='outer') \
                       .merge(taxa_participacao, left_index=True, right_index=True, how='outer') \
                       .merge(taxa_abondono, left_index=True, right_index=True, how='outer') \
                       .merge(id_localizacao, left_index=True, right_index=True, how='outer') \
                       .merge(id_uf, left_index=True, right_index=True, how='outer')
        return df_merged
    except Exception as e:
        print(f"Erro ao mesclar os DataFrames: {e}")
        return pd.DataFrame()

def save_dataframe(df, filepath):
    """
    Salva o DataFrame fornecido em um arquivo CSV no caminho especificado.
    """
    try:
        df.to_csv(filepath, index=False)
        print(f"DataFrame salvo com sucesso em {filepath}")
    except Exception as e:
        print(f"Erro ao salvar o DataFrame: {e}")

def main():
    """
    Função principal que executa o processo de carregamento, criação de DataFrames, 
    configuração de índices, mesclagem e salvamento de dados.
    """
    df2, df3 = load_datasets()

    if not df2.empty and not df3.empty:  # Apenas continua se os DataFrames foram carregados corretamente
        (resposta_pais, tipo_escola_df, nivel_socioeco, id_regiao, taxa_reprovacao, med_lp, med_mt, 
        med_geral, num_matriculados, taxa_participacao, taxa_abondono, id_localizacao, id_uf) = create_dataframes(df2, df3)

        set_indices(resposta_pais, tipo_escola_df, nivel_socioeco, id_regiao, taxa_reprovacao, med_lp, med_mt, med_geral, num_matriculados, taxa_participacao, taxa_abondono, id_localizacao, id_uf)

        df_merged = merge_dataframes(resposta_pais, tipo_escola_df, nivel_socioeco, id_regiao, taxa_reprovacao, med_lp, med_mt, med_geral, num_matriculados, taxa_participacao, taxa_abondono, id_localizacao, id_uf)

        save_dataframe(df_merged, "./Data/data_saeb.csv")
        print(df_merged.head())
        print(df_merged.info())

if __name__ == "__main__":
    main()
