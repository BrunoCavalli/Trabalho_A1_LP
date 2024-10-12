import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import warnings
import sys
import os

# Adicionar o diretório Python_scripts ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../Python_scripts')))

from hipotese_2 import hipotese_2, hipotese_2_2

# Dados de exemplo
df_mock = pd.DataFrame({
    'Num_Matriculados': [100, 200, 150, 400, 250],
    'Taxa_Participacao': [50, 60, 55, 70, 65],
    'Media': [7.5, 8.0, 6.5, 9.0, 7.0]
})

class TestHipotese2(unittest.TestCase):

    @patch('hipotese_2.plt.savefig')  # Mockar plt.savefig para evitar salvar o gráfico
    @patch('pandas.read_csv', return_value=df_mock)  # Mockar pandas.read_csv para evitar ler o arquivo real
    def test_hipotese_2(self, mock_read_csv, mock_savefig):
        # Suprimir os warnings de SettingWithCopyWarning
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=pd.errors.SettingWithCopyWarning)
            # Testar se a função roda sem erros
            try:
                hipotese_2()
            except Exception as e:
                self.fail(f"hipotese_2 falhou com exceção: {e}")
        
        # Verificar se plt.savefig foi chamado
        mock_savefig.assert_called_once_with('./Graphs/boxplot_matric')

    @patch('hipotese_2.plt.savefig')  # Mockar plt.savefig para evitar salvar o gráfico
    @patch('pandas.read_csv', return_value=df_mock)  # Mockar pandas.read_csv para evitar ler o arquivo real
    def test_hipotese_2_2(self, mock_read_csv, mock_savefig):
        # Suprimir os warnings de SettingWithCopyWarning
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=pd.errors.SettingWithCopyWarning)
            # Testar se a função roda sem erros
            try:
                hipotese_2_2()
            except Exception as e:
                self.fail(f"hipotese_2_2 falhou com exceção: {e}")
        
        # Verificar se plt.savefig foi chamado
        mock_savefig.assert_called_once_with('./Graphs/boxplot_part')


if __name__ == '__main__':
    unittest.main()

