import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Número médio anual total de manchas solares [1700 - agora]
cabecalhos = ['Ano', 'Número Médio', 'Coluna3', 'Coluna4', 'Coluna5']
df = pd.read_csv("Trabalho2/dados.csv", delimiter=';', names=cabecalhos, header=None)

x = np.array(df['Ano'].values)  
y = np.array(df['Número Médio'].values) 


def deteccao_automatica():

    dy_dx = np.gradient(y)  # Primeira derivada
    d2y_dx2 = np.gradient(dy_dx)  # Segunda derivada

    maximos_locais = (np.diff(np.sign(dy_dx)) < 0) & (d2y_dx2[:-1] < 0)
    
    # Máximos locais
    peak_indices = np.where(maximos_locais)[0] + 1  

   
    plt.plot(x, y, color='darkblue', label='N° de manchas solares') # gráfico das manchas solares
    plt.plot(x[peak_indices], y[peak_indices], 'ro', label='Máximo Local')  # Máximos locais

    # Linhas entre os máximos para identificar a diferença de anos
    for i in range(1, len(peak_indices)):
        plt.plot([x[peak_indices[i-1]], x[peak_indices[i]]], [y[peak_indices[i-1]], y[peak_indices[i]]], 'r--', alpha=0.5)
        diff_anos = x[peak_indices[i]] - x[peak_indices[i-1]]
        mid_x = (x[peak_indices[i-1]] + x[peak_indices[i]]) / 2
        mid_y = (y[peak_indices[i-1]] + y[peak_indices[i]]) / 2
        plt.text(mid_x, mid_y, f'{diff_anos} anos', color='black', fontsize=8, ha='center')

    plt.xlabel('Ano')
    plt.ylabel('N° Médio de Manchas Solares')
    plt.title('N° Médio de Manchas Solares x Ano')
    plt.legend()
    plt.show()

    anos_picos = x[peak_indices]
    periodos = np.diff(anos_picos)
    media_periodo = np.mean(periodos)

    print(f'Período médio aproximado de um ponto máximo: {media_periodo:.2f} anos')
    print(f'Diferenças de anos entre os pontos máximos: {periodos}')


def selecao_interativa():
    fig, ax = plt.subplots()
    ax.plot(x, y, color='darkblue', label='Número de manchas solares') 
    plt.xlabel('Ano')
    plt.ylabel('N° Médio de Manchas Solares')
    plt.title('Seleção Interativa de Máximos Locais')
    plt.legend()

    pontos_selecionados = []

    def onclick(event):
        if event.xdata and event.ydata:
            pontos_selecionados.append((event.xdata, event.ydata))
            ax.plot(event.xdata, event.ydata, 'ro')  
            
            # Linhas entre os máximos para identificar a diferença de anos ao selecionar mais de um ponto
            if len(pontos_selecionados) > 1:
                p1 = pontos_selecionados[-2]
                p2 = pontos_selecionados[-1]
                ax.plot([p1[0], p2[0]], [p1[1], p2[1]], 'r--', alpha=0.5) 
                diff_anos = p2[0] - p1[0]
                mid_x = (p1[0] + p2[0]) / 2
                mid_y = (p1[1] + p2[1]) / 2
                ax.text(mid_x, mid_y, f'{diff_anos:.0f} anos', color='black', fontsize=8, ha='center')  
            plt.draw()

    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    plt.show()

    pontos_selecionados = np.array([p[0] for p in pontos_selecionados])  
    pontos_selecionados.sort() 
    periodos = np.diff(pontos_selecionados) 
    media_periodo = np.mean(periodos) if len(periodos) > 0 else 0  
    
    print(f'Período médio aproximado dos pontos máximos selecionados : {media_periodo:.2f} anos')


print("Escolha a opção de visualização:")
print("1 - Detecção Automática de Máximos Locais")
print("2 - Seleção Interativa de Máximos Locais")
escolha = input("Digite 1 ou 2: ")

if escolha == '1':
    deteccao_automatica()
elif escolha == '2':
    selecao_interativa()
else:
    print("Opção inválida!")
