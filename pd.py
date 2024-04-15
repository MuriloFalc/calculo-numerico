import pandas as pd
import matplotlib.pyplot as plt

def plot_from_excel(filename):
    # Carrega o arquivo xlsx em um DataFrame do Pandas
    df = pd.read_excel(filename)
    
    # Extrai os dados das colunas para o eixo x e para o eixo y
    x_values = df.iloc[:, 0]  # Primeira coluna
    y_values = df.iloc[:, 1]  # Segunda coluna
    
    # Cria o gráfico
    plt.plot(x_values, y_values)
    
    # Adiciona rótulos aos eixos
    plt.xlabel(df.columns[0])  # Rótulo da primeira coluna
    plt.ylabel(df.columns[1])  # Rótulo da segunda coluna
    
    # Exibe o gráfico
    plt.show()

# Caminho para o arquivo xlsx
filename = "Pasta1.xlsx"

# Chama a função para plotar o gráfico
plot_from_excel(filename)


tab = pd.read_excel('Pasta1.xlsx')
print(tab)