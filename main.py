import numpy as np
import matplotlib.pyplot as plt

def sinal_classificado(sinal):
    sinal_invertido = sinal[::-1]
    
    if np.allclose(sinal, sinal_invertido):  # Verifica se é par
        return "Par"
    elif np.allclose(sinal, -sinal_invertido):  # Verifica se é ímpar
        return "Ímpar"
    else:
        return "Sem simetria"

def decompor_sinal(sinal):
    classificacao = sinal_classificado(sinal)
    
    if classificacao == "Par":
        parte_par = sinal
        parte_impar = np.zeros(len(sinal))
    elif classificacao == "Ímpar":
        parte_par = np.zeros(len(sinal))
        parte_impar = sinal
    else:
        sinal_invertido = sinal[::-1]
        parte_par = (sinal + sinal_invertido) / 2
        parte_impar = (sinal - sinal_invertido) / 2
    
    return parte_impar, parte_par, classificacao

def plotar_sinais(sinal, tempo_inicial):
    parte_impar, parte_par, classificacao = decompor_sinal(sinal)
    soma_partes = parte_impar + parte_par
    n = np.arange(tempo_inicial, tempo_inicial + len(sinal))
    
    plt.figure(figsize=(6, 4))  # Tamanho reduzido da figura para ser mais compacto
    
    # Subplot 2x2 para o Sinal Original
    plt.subplot(2, 2, 1)
    plt.stem(n, sinal, label="Sinal Original", basefmt=" ")
    plt.title(f"Sinal Original - {classificacao}")
    plt.xlabel("Tempo (n)")
    plt.ylabel("Amplitude")
    plt.legend()
    
    # Subplot 2x2 para a Parte Ímpar
    plt.subplot(2, 2, 2)
    plt.stem(n, parte_impar, label="Parte Ímpar", basefmt=" ")
    plt.title("Parte Ímpar do Sinal")
    plt.xlabel("Tempo (n)")
    plt.ylabel("Amplitude")
    plt.legend()
    
    # Subplot 2x2 para a Parte Par
    plt.subplot(2, 2, 3)
    plt.stem(n, parte_par, label="Parte Par", basefmt=" ")
    plt.title("Parte Par do Sinal")
    plt.xlabel("Tempo (n)")
    plt.ylabel("Amplitude")
    plt.legend()
    
    # Subplot 2x2 para a Soma das Partes Ímpar e Par
    plt.subplot(2, 2, 4)
    plt.stem(n, soma_partes, label="Soma das Partes Ímpar e Par", basefmt=" ")
    plt.title("Soma das Partes Ímpar e Par")
    plt.xlabel("Tempo (n)")
    plt.ylabel("Amplitude")
    plt.legend()
    
    plt.tight_layout(pad=1.0)  # Ajusta o layout para que os gráficos fiquem compactos
    plt.show()

# Testando com sen(x) e cos(x) no intervalo de -10 a 10
x = np.arange(-10, 11, 1)  # intervalo de -10 a 10 com passos de 1
sinal_seno = np.sin(x)
sinal_cosseno = np.cos(x)
sinal_nao_par_nem_impar = x + 1
tempo_inicial = -10  # Inicia no -10 para alinhar com o array `x`

# Testando com sen(x), sinal ímpar, no intervalo de -10 a 10 
plotar_sinais(sinal_seno, tempo_inicial)

# Testando com cos(x), sinal par, no intervalo de -10 a 10 
plotar_sinais(sinal_cosseno, tempo_inicial)

# Testando com um sinal que não é par nem ímpar
plotar_sinais(sinal_nao_par_nem_impar, tempo_inicial)
