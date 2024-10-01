import numpy as np
import matplotlib.pyplot as plt

def convolucao_manual(x, h, n_x, n_h):
    """
    Realiza a convolução manualmente entre dois sinais discretos x e h,
    seguindo o processo "rebate, desloca, multiplica e soma".
    """

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

    # Plota os sinais antes de iniciar a convolução
    plot_signals(x,n_x, h_rebatido,n_h_rebatido, y)
    
    
    for i in range(len_y):
        n_h_shifted = n_h_rebatido + i # Desloca para a direita (1, 2, 3, ...)
        # Etapa 2: Multiplica e soma os sinais deslocados
        # for em n_h_shifted
        for n in n_x:
            if n in n_h_shifted:
                y[i] += x[n_x.tolist().index(n)] * h_rebatido[n_h_shifted.tolist().index(n)]
                
                
        # Atualiza a plotagem após cada iteração
        update_plot(x, h_rebatido, n_h_shifted, y, i)

    
    

    plt.show()  # Mostra a figura final após a animação

def plot_signals(x,n_x, h_rebatido,n_h_rebatido, y):
    """
    Configura a figura para os sinais e o resultado da convolução.
    """
    plt.figure(figsize=(12, 8))

    # Gráfico do primeiro sinal
    plt.subplot(3, 1, 1)
    plt.stem(range(len(x)), x, basefmt=" ")
    plt.title("Sinal x[n]")
    plt.xlabel("n")
    plt.ylabel("x[n]")
    plt.grid()

    # Gráfico do segundo sinal (h[n] rebatido)
    plt.subplot(3, 1, 2)
    plt.stem(n_h_rebatido, h_rebatido, basefmt=" ")
    plt.title("Sinal h[n] Rebatido")
    plt.xlabel("n")
    plt.ylabel("h[n]")
    plt.grid()

    # Gráfico do sinal resultante da convolução
    plt.subplot(3, 1, 3)
    plt.stem(range(len(y)), y, basefmt=" ")
    plt.title("Sinal resultante da convolução y[n]")
    plt.xlabel("n")
    plt.ylabel("y[n]")
    plt.grid()

    plt.tight_layout()
    # Pausa para visualização inicial

def update_plot(x, h_rebatido, n_h_shifted, y, step ):
    """
    Atualiza a plotagem do sinal rebatido h(n) e do sinal resultante da convolução.
    """
    plt.subplot(3, 1, 2)
    plt.cla()  # Limpa o gráfico atual
    plt.stem( n_h_shifted, h_rebatido, basefmt=" ")
    plt.title(f"Sinal h[n] Rebatido (Deslocado - Passo {step})")
    plt.xlabel("n")
    plt.ylabel("h[n]")
    plt.grid()

    plt.subplot(3, 1, 3)
    plt.cla()  # Limpa o gráfico atual do sinal resultante
    plt.stem(range(len(y)), y, basefmt=" ")
    plt.title(f"Sinal resultante da convolução y[n] (Passo {step})")
    plt.xlabel("n")
    plt.ylabel("y[n]")
    plt.grid()

    plt.tight_layout()
    plt.pause(0.5)  # Pausa para visualização durante a atualização

# Exemplo de uso

# Definição do sinal x[n]
x = np.array([1, -1, 2])
n_x = np.array([0, 1, 5])

# Definição do sinal h[n]
alpha = 0.6
n_h = np.arange(10)  # Considera um intervalo para capturar o decaimento
h = alpha ** n_h  # Sinal exponencial decrescente

# Convolução manual
convolucao_manual(x, h, n_x, n_h)
