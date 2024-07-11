import os

user_request = int(input('Qual número deseja averiguar? \n'))

if user_request % 2 == 0:
    os.system('cls')
    print('Número é par')
else:
    os.system('cls')
    print('número é ímpar')