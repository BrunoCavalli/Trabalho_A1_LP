import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import warnings
import sys
import os

# Adicionar o diretório Python_scripts ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../Python_scripts')))

from hipotese_3 import (
    hipotese_3_regiao_media_boxplot,
    hipotese_3_UF_media,
    hipotese_3_2_regiao_nivel_socio,
    hipotese_3_3
)

# Dados de exemplo
df_mock = pd.DataFrame({
    'Regiao': ['Norte', 'Sul', 'Nordeste', 'Sudeste', 'Centro-Oeste'],
    'UF': ['AC', 'RS', 'BA', 'SP', 'DF'],
    'Media': [7.5, 8.0, 6.5, 9.0, 7.0],
    'Nivel_Socioeconomico': ['Baixo', 'Médio', 'Baixo', 'Alto', 'Médio'],
    'Localizacao': ['Rural', 'Urbana', 'Rural', 'Urbana', 'Rural']
})

class TestHipotese3(unittest.TestCase):

    @patch('hipotese_3.plt.savefig')  # Mockar plt.savefig para evitar salvar o gráfico
    @patch('pandas.read_csv', return_value=df_mock)  # Mockar pandas.read_csv para evitar ler o arquivo real
    def test_hipotese_3_regiao_media_boxplot(self, mock_read_csv, mock_savefig):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=pd.errors.SettingWithCopyWarning)
            # Testar se a função roda sem erros
            try:
                hipotese_3_regiao_media_boxplot()
            except Exception as e:
                self.fail(f"hipotese_3_regiao_media_boxplot falhou com exceção: {e}")
            
            # Verificar se plt.savefig foi chamado
            mock_savefig.assert_called_once_with('./Graphs/boxplot_regia_media')

    @patch('hipotese_3.plt.savefig')  # Mockar plt.savefig para evitar salvar o gráfico
    @patch('pandas.read_csv', return_value=df_mock)  # Mockar pandas.read_csv para evitar ler o arquivo real
    def test_hipotese_3_UF_media(self, mock_read_csv, mock_savefig):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=pd.errors.SettingWithCopyWarning)
            # Testar se a função roda sem erros
            try:
                hipotese_3_UF_media()
            except Exception as e:
                self.fail(f"hipotese_3_UF_media falhou com exceção: {e}")
            
            # Verificar se plt.savefig foi chamado
            mock_savefig.assert_called_once_with('./Graphs/boxplot_uf_media')

    @patch('hipotese_3.plt.savefig')  # Mockar plt.savefig para evitar salvar o gráfico
    @patch('pandas.read_csv', return_value=df_mock)  # Mockar pandas.read_csv para evitar ler o arquivo real
    def test_hipotese_3_2_regiao_nivel_socio(self, mock_read_csv, mock_savefig):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=pd.errors.SettingWithCopyWarning)
            # Testar se a função roda sem erros
            try:
                hipotese_3_2_regiao_nivel_socio()
            except Exception as e:
                self.fail(f"hipotese_3_2_regiao_nivel_socio falhou com exceção: {e}")
            
            # Verificar se plt.savefig foi chamado
            mock_savefig.assert_called_once_with('./Graphs/heatmap_regiao_socio')

    @patch('hipotese_3.plt.savefig')  # Mockar plt.savefig para evitar salvar o gráfico
    @patch('pandas.read_csv', return_value=df_mock)  # Mockar pandas.read_csv para evitar ler o arquivo real
    def test_hipotese_3_3(self, mock_read_csv, mock_savefig):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=pd.errors.SettingWithCopyWarning)
            # Testar se a função roda sem erros
            try:
                hipotese_3_3()
            except Exception as e:
                self.fail(f"hipotese_3_3 falhou com exceção: {e}")
            
            # Verificar se plt.savefig foi chamado
            mock_savefig.assert_called_once_with('./Graphs/boxplot_loc')


if __name__ == '__main__':
    unittest.main()

