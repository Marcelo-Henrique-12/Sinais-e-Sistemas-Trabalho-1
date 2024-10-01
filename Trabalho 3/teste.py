import numpy as np
import matplotlib.pyplot as plt

def convolucao_manual(x, h, n_x, n_h):
    # Tamanho dos sinais
    len_x = len(x)
    len_h = len(h)

    # Tamanho do sinal resultante
    len_y = len_x + len_h - 1
    
    # Inicializa o sinal resultante com zeros
    y = np.zeros(len_y)
    
    # Etapa 1: Rebate o sinal h(n) para h(-n)
    h_rebatido = h[::-1]  # Inverte os valores de h(n) para h(-n)
    n_h_rebatido = -n_h[::-1]  # Rebate os índices de h(n) para h(-n)

    # Plot do sinal h[n] rebatido
    plt.figure(figsize=(6, 4))
    plt.stem(n_h_rebatido, h_rebatido, basefmt=" ")
    plt.title("Sinal h[n] Rebatido")
    plt.xlabel("n")
    plt.ylabel("h[-n]")
    plt.grid()
    plt.show()

    # Etapa 2: Desloca h_rebatido para a direita e plota
    deslocamentos = 5  # Número de deslocamentos desejados
    for i in range(deslocamentos):
        plt.figure(figsize=(6, 4))
        # Desloca n_h_rebatido para a direita
        n_h_shifted = n_h_rebatido + (i + 1)  # Desloca para a direita (1, 2, 3, ...)
        
        plt.stem(n_h_shifted, h_rebatido, basefmt=" ")
        plt.title(f"Sinal h[n] Rebatido (Deslocado para a direita - Passo {i + 1})")
        plt.xlabel("n")
        plt.ylabel("h[-n]")
        plt.grid()
        plt.show()

# Definição do sinal x[n]
x = np.array([1, -1, 2])
n_x = np.array([0, 1, 2])

# Definição do sinal h[n]
alpha = 0.6
n_h = np.arange(10)  # Considera um intervalo para capturar o decaimento
h = alpha ** n_h  # Sinal exponencial decrescente

# Convolução manual
convolucao_manual(x, h, n_x, n_h)
