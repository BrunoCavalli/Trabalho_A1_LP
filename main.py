import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency
from Python_scripts.hipotese_1 import hipotese_1_reprovacao, hipotese_1_abondono
from Python_scripts.hipotese_2 import hipotese_2, hipotese_2_2
from Python_scripts.hipotese_3 import hipotese_3_regiao_media_boxplot, hipotese_3_UF_media, hipotese_3_2_regiao_nivel_socio, hipotese_3_3
from Python_scripts.hipotese_4 import hipotese_4

# Carrega o dataset 
df = pd.read_csv("./Data/data_saeb.csv", low_memory=False)


# Carrega as funções que realizam as análises de cada hipótese
hipotese_1_reprovacao()
hipotese_1_abondono()
hipotese_2()
hipotese_2_2()
hipotese_3_regiao_media_boxplot()
hipotese_3_UF_media()
hipotese_3_2_regiao_nivel_socio()
hipotese_3_3()
hipotese_4
plt.show()