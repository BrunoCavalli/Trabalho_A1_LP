import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import warnings
import sys
import os

# Adicionar o diretório Python_scripts ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../Python_scripts')))

from hipotese_4 import hipotese_4

# Dados de exemplo
df_mock = pd.DataFrame({
    'Tipo_Escola': ['A', 'B', 'C', 'A', 'C'],
    'Media': [7.5, 8.0, 6.5, 9.0, 7.0]
})

class TestHipotese4(unittest.TestCase):

    @patch('hipotese_4.plt.savefig')  # Mockar plt.savefig para evitar salvar o gráfico
    @patch('pandas.read_csv', return_value=df_mock)  # Mockar pandas.read_csv para evitar ler o arquivo real
    def test_hipotese_4(self, mock_read_csv, mock_savefig):
        # Suprimir os warnings de SettingWithCopyWarning
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", category=pd.errors.SettingWithCopyWarning)
            # Testar se a função roda sem erros
            try:
                hipotese_4()
            except Exception as e:
                self.fail(f"hipotese_4 falhou com exceção: {e}")
        
        # Verificar se plt.savefig foi chamado
        mock_savefig.assert_called_once_with('./Graphs/boxplot_tipo')


if __name__ == '__main__':
    unittest.main()
