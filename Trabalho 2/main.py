import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Carrega a planilha e seleciona os dados relevantes para o Trabalho
df = pd.read_csv('dados.csv', sep=';', header=None)

df.columns = ['Data Decimal', 'Número Médio Anual', 'Coluna3', 'Coluna4', 'Coluna5']

x = df['Data Decimal']
y = df['Número Médio Anual']

# Detecta automaticamente os pontos máximos e plota
def deteccao_automatica():
    
    # Primeira Derivada
    dy = np.gradient(y, x)

    # Segunda derivada
    d2y = np.gradient(dy, x)

    # Encontrar pontos de máximo local: derivada primeira muda de positiva para negativa e segunda derivada negativa
    maximos_locais = np.where((np.diff(np.sign(dy)) < 0) & (d2y[:-1] < 0))[0] + 1

    # Criar o gráfico
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, y, label='Número Médio Mensal', color='blue')

    ax.plot(x[maximos_locais], y[maximos_locais], 'ro', label='Máximos Locais')

    for i in range(1, len(maximos_locais)):
        ax.plot([x[maximos_locais[i-1]], x[maximos_locais[i]]],
                [y[maximos_locais[i-1]], y[maximos_locais[i]]],
                'r--', label='Intervalo entre máximos' if i == 1 else "")

        # Adicionar anotação da quantidade de anos entre os máximos
        anos = x[maximos_locais[i]] - x[maximos_locais[i-1]]
        ax.text((x[maximos_locais[i-1]] + x[maximos_locais[i]]) / 2,
                (y[maximos_locais[i-1]] + y[maximos_locais[i]]) / 2,
                f'{anos:.1f} anos',
                color='black', fontsize=9, ha='center', va='bottom')

    ax.set_title('Número Médio Mensal de Manchas Solares')
    ax.set_xlabel('Data Decimal')
    ax.set_ylabel('Número de Manchas Solares')
    ax.legend()
    
    plt.show()

    print("Pontos máximos locais (Data Decimal, Número de Manchas Solares):")
    for i in maximos_locais:
        print(f"({x[i]:.2f}, {y[i]:.2f})")


# Gráfico interativo para o usuário selecionar os pontos máximos
def selecao_interativa():
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, y, label='Número Médio Mensal')

    ax.set_title('Número Médio Mensal de Manchas Solares')
    ax.set_xlabel('Data Decimal')
    ax.set_ylabel('Número de Manchas Solares')
    ax.legend()

    # armazena os pontos clicados
    pontos_maximos = []

    marcacoes = []

    # Função para verificar se um clique está próximo de um ponto já marcado
    def ponto_proximo(ix, iy, pontos, tol=0.1):
        """Verifica se o ponto clicado está próximo de algum ponto já marcado."""
        for (px, py) in pontos:
            if np.sqrt((ix - px)**2 + (iy - py)**2) < tol:
                return (px, py)
        return None

    # Função que será chamada ao clicar no gráfico
    def on_click(event):
        ix, iy = event.xdata, event.ydata
        proximo_ponto = ponto_proximo(ix, iy, pontos_maximos)

        if proximo_ponto:
            pontos_maximos.remove(proximo_ponto)
            
            for marcacao in marcacoes:
                if marcacao[0] == proximo_ponto:
                    marcacao[1].remove() 
                    marcacao[2].remove()  
                    marcacoes.remove(marcacao)
                    break
        else:
            pontos_maximos.append((ix, iy))
            point, = ax.plot(ix, iy, 'ro') 
            text = ax.annotate(f'({ix:.2f}, {iy:.2f})', (ix, iy), textcoords="offset points", xytext=(0,10), ha='center')
            marcacoes.append(((ix, iy), point, text))
        
        fig.canvas.draw()

    cid = fig.canvas.mpl_connect('button_press_event', on_click)

    plt.show()

    print("Pontos máximos selecionados:", pontos_maximos)




# Inicio do código, para selecionar o tipo de operação
print("Escolha o modo de operação:")
print("1 - Detecção Automática de Máximos e Mínimos Locais")
print("2 - Seleção Interativa de Máximos Locais")
escolha = input("Digite 1 ou 2: ")

if escolha == '1':
    deteccao_automatica()
elif escolha == '2':
    selecao_interativa()
else:
    print("Opção inválida!")
