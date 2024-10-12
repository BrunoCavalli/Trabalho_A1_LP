import unittest
from unittest.mock import patch, MagicMock
import pandas as pd
import sys
import os

# Adicionar o diretório Python_scripts ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../Python_scripts')))

from hipotese_1 import hipotese_1_reprovacao, hipotese_1_abandono

# Dados de exemplo
df_mock = pd.DataFrame({
    'Respostas_Pais': ['A', 'B', 'C', 'A', 'B'],
    'Taxa_Reprovacao': ['A', 'B', 'C', 'A', 'C'],
    'Taxa_Abandono': ['A', 'B', 'A', 'C', 'B']
})

class TestHipotese1(unittest.TestCase):

    @patch('hipotese_1.plt.savefig')  # Mockar plt.savefig para evitar salvar o gráfico
    @patch('pandas.read_csv', return_value=df_mock)  # Mockar pandas.read_csv para evitar ler o arquivo real
    def test_hipotese_1_reprovacao(self, mock_read_csv, mock_savefig):
        # Testar se a função roda sem erros
        try:
            hipotese_1_reprovacao()
        except Exception as e:
            self.fail(f"hipotese_1_reprovacao falhou com exceção: {e}")
        
        # Verificar se plt.savefig foi chamado
        mock_savefig.assert_called_once_with('./Graphs/heatmap_reprovacao')

    @patch('hipotese_1.plt.savefig')  # Mockar plt.savefig para evitar salvar o gráfico
    @patch('pandas.read_csv', return_value=df_mock)  # Mockar pandas.read_csv para evitar ler o arquivo real
    def test_hipotese_1_abandono(self, mock_read_csv, mock_savefig):
        # Testar se a função roda sem erros
        try:
            hipotese_1_abandono()
        except Exception as e:
            self.fail(f"hipotese_1_abandono falhou com exceção: {e}")
        
        # Verificar se plt.savefig foi chamado
        mock_savefig.assert_called_once_with('./Graphs/heatmap_abandono')


if __name__ == '__main__':
    unittest.main()
