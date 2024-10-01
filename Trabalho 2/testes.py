import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Número médio anual total de manchas solares [1700 - agora]
cabecalhos = ['Ano', 'Número Médio', 'Coluna3', 'Coluna4', 'Coluna5']
df = pd.read_csv("Trabalho2/dados.csv", delimiter=';', names=cabecalhos, header=None)

x = np.array(df['Ano'].values)  # Anos
y = np.array(df['Número Médio'].values)  # Número Médio Anual