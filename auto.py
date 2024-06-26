import matplotlib.pyplot as plt
import numpy as np
import random as rdm
import pandas as pd

def manual(n):
    pontos = [] 
    for _ in range(n):
        x = float(input("coordenadas x em n: "))
        y = float(input("coordenadas y em n: "))
        pontos.append([x, y])
    return pontos

def auto(n):
    pontos = [] 
    valores_x = rdm.sample(range(11), n)  # Garantir que os valores de x não se repitam
    for x in valores_x:
        y = rdm.randint(0, 10)
        pontos.append([x, y])
    return pontos

def regressao_linear(x, y):
    # Calcula a regressão linear
    n = len(x)
    soma_x = sum(x)
    soma_y = sum(y)
    soma_x_squared = sum(i**2 for i in x)
    soma_xy = sum(x[i] * y[i] for i in range(n))

    # Coeficientes da regressão linear
    a = (n * soma_xy - soma_x * soma_y) / (n * soma_x_squared - soma_x**2)
    b = (soma_y - a * soma_x) / n

    return a, b

def regressao_quadratica(x, y):
    # Calcula a regressão quadrática
    A = np.vstack([x**2, x, np.ones(len(x))]).T
    coefs = np.linalg.lstsq(A, y, rcond=None)[0]
    return coefs


def main():
    """
        n define a quantidade de pontos a serem gerados ou analisados
    """
    n = 5
    pontos_iniciais = auto(n) #essa função cria pontos aleatrórios
    #pontos_iniciais = manual(n) #essa função permite que o usuario escreva manualmente os pontos
    
        
    x = [p[0] for p in pontos_iniciais]     #Lista de coordenadas X
    y = [p[1] for p in pontos_iniciais]     #Lista de coordenadas Y
    
    print('pontos x:\n', x)
    print('pontos y:\n', y)
    
    # Plotar os pontos
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
    plt.axis((0, max(x)+ 1, 0, max(y)+ 1))
    plt.legend()
    plt.show()
#main()