import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Coloque aqui o caminho correto para o arquivo CSV baixado
path = "bolsa.csv"

# Leitura do arquivo CSV
df_bolsa = pd.read_csv(path)

# Pegando apenas a coluna de fechamento da bolsa
df_bolsa_fechamento = df_bolsa[['Close']]

# Define a lista de ordens N para aplicar o filtro MA
ordens = [3, 5, 10]

# Configurando a figura para ter 4 subplots
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# Plot original (subplot 1)
axs[0, 0].plot(df_bolsa_fechamento['Close'].values[:50], label='Original', color='blue')
axs[0, 0].set_title('Original')
axs[0, 0].set_xlabel('Dias')
axs[0, 0].set_ylabel('Fechamento')
axs[0, 0].legend()
axs[0, 0].grid()

# Loop para plotar os MA em subplots diferentes
for i, N in enumerate(ordens):
    row = (i + 1) // 2
    col = (i + 1) % 2

    # Calcula a média móvel com janela de tamanho N
    df_bolsa_fechamento[f'MA_{N}'] = df_bolsa_fechamento['Close'].rolling(window=N).mean()
    
    # Plotando o filtro MA de ordem N
    axs[row, col].plot(df_bolsa_fechamento['Close'].values[:50], label='Original', color='blue', linestyle='--', alpha=0.5)
    axs[row, col].plot(df_bolsa_fechamento[f'MA_{N}'].values[:50], label=f'MA Ordem {N}', color='red')
    axs[row, col].set_title(f'Média Móvel Ordem {N}')
    axs[row, col].set_xlabel('Dias')
    axs[row, col].set_ylabel('Fechamento')
    axs[row, col].legend()
    axs[row, col].grid()

# Ajusta o layout para evitar sobreposição de textos
plt.tight_layout()

# Mostrando o gráfico
plt.show()
