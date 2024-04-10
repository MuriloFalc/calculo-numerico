import matplotlib.pyplot as plt
import numpy as np
from auto import regressao_linear
from auto import regressao_quadratica

def main():
    pontos_iniciais = [[0,1,2,3,4], [1,1.8, 1.3, 2.5, 6.5]]
    
    for individuo in pontos_iniciais:
        print(individuo)
        
    x = [0,1,2,3,4]  # Lista de coordenadas X
    y = [1,1.8, 1.3, 2.5, 6.5]  # Lista de coordenadas Y
    
    plt.scatter(np.array(x), np.array(y))
    
    def quadratica():
        # Realizar regressão quadrática
        coefs = regressao_quadratica(np.array(x), np.array(y))
        
        # Equação do polinômio
        equacao2 = f'f(x) = {coefs[0]:.2f}x^2 + {coefs[1]:.2f}x + {coefs[2]:.2f}'
        print("Equação do polinômio quadrático:", equacao2)
        
        # Plotar a curva quadrática
        x_quadratico = np.linspace(min(x), max(x), 100)
        y_quadratico = coefs[0]*x_quadratico**2 + coefs[1]*x_quadratico + coefs[2]
        plt.plot(x_quadratico, y_quadratico, color='red', label=equacao2)
    
    def linear():
        # Realizar regressão linear
        a, b = regressao_linear(x, y)
        
        # Equação da reta
        equacao1 = f'f(x) = {a:.2f}x + {b:.2f}'
        print("Equação da reta:", equacao1)
        
        # Plotar a reta
        x_reta = np.linspace(min(x), max(x), 100)
        y_reta = a * x_reta + b
        plt.plot(x_reta, y_reta, color='green', label=equacao1)
    
    linear()
    quadratica()    
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.axis((0, 7, 0, 7))
    plt.legend()
    plt.show()
    
main()