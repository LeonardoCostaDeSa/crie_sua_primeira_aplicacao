'''
Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
Terceiro Quadrante: os valores de x e y devem ser menores que zero;
Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
Caso contrário: o ponto está localizado no eixo ou origem.
'''
import os
valor_de_x = int(input('Digite o valor de x: \n'))
valor_de_y = int(input('Digite o valor de y: \n'))

if valor_de_x > 0 and valor_de_y > 0:
    os.system('cls')
    print('Primeiro Quadrante')
elif valor_de_x < 0 and valor_de_y > 0:
    os.system('cls')
    print('Segundo Quadrante')
elif valor_de_x < 0 and valor_de_y < 0:
    os.system('cls')
    print('Terceiro Quadrante')
elif valor_de_x > 0 and valor_de_y < 0:
    os.system('cls')
    print('Quarto Quadrante')
else:
    os.system('cls')
    print('O ponto está localizado no eixo ou origem')
