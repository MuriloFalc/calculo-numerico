import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import auto
from auto import regressao_quadratica
from auto import regressao_linear
from auto import main
"""
    nomePlanilha = '2024'
    caminhoArquivo = 'Pasta1.xlsx'
    dadosExc = pd.read_excel(caminhoArquivo, sheet_name=nomePlanilha)
    print(dadosExc)
"""
def main():
    n = 12

    x = [2567.20, 3159.40, 4153.40, 2746.80, 2147.80, 900.4, 478.20, 168.20, 316, 358.80, 546.80, 1507.20] #precipitação
    y = [854, 838, 1200, 677, 539, 425, 291, 348, 244, 218, 230, 207] #casos de dengue

    plt.scatter(np.array(x), np.array(y)) 

    def quadratica():
            # Realizar regressão quadrática
            coefs = regressao_quadratica(np.array(x), np.array(y))
            
            # Equação do polinômio
            equacao2 = f'f(x) = {coefs[0]:f}x^2 + {coefs[1]:f}x + {coefs[2]:f}'
            print("Equação do polinômio quadrático:", equacao2)
            
            # Plotar a curva quadrática
            x_quadratico = np.linspace(min(x), max(x), 100)
            y_quadratico = coefs[0]*x_quadratico**2 + coefs[1]*x_quadratico + coefs[2]
            plt.plot(x_quadratico, y_quadratico, color='red', label=equacao2)
            
    def linear():
        # Realizar regressão linear
        a, b = regressao_linear(x, y)
        
        # Equação da reta
        equacao1 = f'f(x) = {a:f}x + {b:f}'
        print("Equação da reta:", equacao1)
        
        # Plotar a reta
        x_reta = np.linspace(min(x), max(x), 100)
        y_reta = a * x_reta + b
        plt.plot(x_reta, y_reta, color='green', label=equacao1)
    
    def getFunLin(x1):
        a, b = regressao_linear(x, y)
        y1 = a*x1 + b
        print(y1)
    
    def getFunQua(x1):
        a, b = regressao_quadratica(x, y)
        y1 = a*x1**2 + b*x1 + c
        print(y1)
    
    jan = 2567.20
    
    linear()
    getFunLin(jan)
    getFunQua(jan)
    quadratica()
    plt.xlabel('Precipitação acumulada no mês - Pará')
    plt.ylabel('Casos de dengue no estado')
    plt.axis((0, max(x)+ 1, 0, max(y)+ 1))
    plt.legend()
    plt.show()

main()