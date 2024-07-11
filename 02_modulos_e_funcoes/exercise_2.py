'''
2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else 
para classificar a idade em categorias de acordo com as seguintes condições:

Criança: 0 a 12 anos;
Adolescente: 13 a 18 anos;
Adulto: acima de 18 anos.

'''
import os

user_age = int(input('Digite sua idade\n'))

if user_age <=12:
    os.system('cls')
    print('Criança')
elif user_age >= 13 and user_age < 18:
    os.system('cls')
    print('Adolescente')
else:
    os.system('cls')
    print('adulto')
