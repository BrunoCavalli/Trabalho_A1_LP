import pandas as pd
import numpy as np

def load_datasets():
    df2 = pd.read_csv("./Data/TS_ESCOLA.csv", sep=";", encoding="latin1")
    df3 = pd.read_csv("./Data/TS_ALUNO_34EM.csv", sep=";", encoding="latin1")
    return df2, df3

def create_dataframes(df2, df3):
    resposta_pais = pd.DataFrame(df3["TX_RESP_Q09c"])
    resposta_pais.columns = ["Respostas_Pais"]

    tipo_escola_df = pd.DataFrame(df3["TX_RESP_Q17"])
    tipo_escola_df.columns = ["Tipo_Escola"]

    taxa_reprovacao = pd.DataFrame(df3["TX_RESP_Q18"])
    taxa_reprovacao.columns = ["Taxa_Reprovacao"]

    taxa_abondono = pd.DataFrame(df3["TX_RESP_Q19"])
    taxa_abondono.columns = ["Taxa_Abandono"]

    nivel_socioeco = pd.DataFrame(df2["NIVEL_SOCIO_ECONOMICO"])
    nivel_socioeco.columns = ["Nivel_Socioeconomico"]

    id_regiao = pd.DataFrame(df2["ID_REGIAO"])
    id_regiao.columns = ["Regiao"]

    med_lp = pd.DataFrame(df2["MEDIA_EM_LP"])
    med_lp.columns = ["Media_LP"]

    med_mt = pd.DataFrame(df2["MEDIA_EM_MT"])
    med_mt.columns = ["Media_MT"]

    num_matriculados = pd.DataFrame(df2["NU_MATRICULADOS_CENSO_EMT"])
    num_matriculados.columns = ["Num_Matriculados"]

    taxa_participacao = pd.DataFrame(df2["TAXA_PARTICIPACAO_EM"])
    taxa_participacao.columns = ["Taxa_Participacao"]

    id_localizacao = pd.DataFrame(df2["ID_LOCALIZACAO"])
    id_localizacao.columns = ["Localizacao"]

    id_uf = pd.DataFrame(df2["ID_UF"])
    id_uf.columns = ["UF"]

    return (resposta_pais, tipo_escola_df, nivel_socioeco, id_regiao, taxa_reprovacao, med_lp, med_mt, 
            num_matriculados, taxa_participacao, taxa_abondono, id_localizacao, id_uf)

def set_indices(resposta_pais, tipo_escola_df, nivel_socioeco, id_regiao, taxa_reprovacao, med_lp, med_mt, num_matriculados, taxa_participacao, taxa_abondono, id_localizacao, id_uf):
    resposta_pais.index.name = "Resposta"
    tipo_escola_df.index.name = "Publica_Privada"
    taxa_reprovacao.index.name = "Taxa_Reprovacao"
    med_lp.index.name = "Media_LP"
    med_mt.index.name = "Media_MT"
    num_matriculados.index.name = "Num_Matriculados"
    taxa_participacao.index.name = "Taxa_Participacao"
    taxa_abondono.index.name = "Taxa_Abandono"
    id_localizacao.index.name = "Localizacao"
    id_uf.index.name = "UF"
    nivel_socioeco.index.name = "Nivel"
    id_regiao.index.name = "Regiao"

def merge_dataframes(resposta_pais, tipo_escola_df, nivel_socioeco, id_regiao, taxa_reprovacao, med_lp, med_mt, num_matriculados, taxa_participacao, taxa_abondono, id_localizacao, id_uf):
    df_merged = resposta_pais.merge(tipo_escola_df, left_index=True, right_index=True, how="outer") \
                   .merge(nivel_socioeco, left_index=True, right_index=True, how='outer') \
                   .merge(id_regiao, left_index=True, right_index=True, how='outer') \
                   .merge(taxa_reprovacao, left_index=True, right_index=True, how='outer') \
                   .merge(med_lp, left_index=True, right_index=True, how='outer') \
                   .merge(med_mt, left_index=True, right_index=True, how='outer') \
                   .merge(num_matriculados, left_index=True, right_index=True, how='outer') \
                   .merge(taxa_participacao, left_index=True, right_index=True, how='outer') \
                   .merge(taxa_abondono, left_index=True, right_index=True, how='outer') \
                   .merge(id_localizacao, left_index=True, right_index=True, how='outer') \
                   .merge(id_uf, left_index=True, right_index=True, how='outer')
    return df_merged

def save_dataframe(df, filepath):
    df.to_csv(filepath, index=False)

def main():
    df2, df3 = load_datasets()
    (resposta_pais, tipo_escola_df, nivel_socioeco, id_regiao, taxa_reprovacao, med_lp, med_mt, 
     num_matriculados, taxa_participacao, taxa_abondono, id_localizacao, id_uf) = create_dataframes(df2, df3)
    set_indices(resposta_pais, tipo_escola_df, nivel_socioeco, id_regiao, taxa_reprovacao, med_lp, med_mt, num_matriculados, taxa_participacao, taxa_abondono, id_localizacao, id_uf)
    df_merged = merge_dataframes(resposta_pais, tipo_escola_df, nivel_socioeco, id_regiao, taxa_reprovacao, med_lp, med_mt, num_matriculados, taxa_participacao, taxa_abondono, id_localizacao, id_uf)
    save_dataframe(df_merged, "./Data/data_saeb.csv")
    print(df_merged.head())
    print(df_merged.info())

if _name_ == "_main_":
    main()