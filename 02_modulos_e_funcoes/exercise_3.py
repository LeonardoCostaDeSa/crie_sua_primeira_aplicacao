'''
3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar
 se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

'''

import os

login = 'Leonardo Costa'
password = 61295

request_login = input('Digite o login: \n')
request_password = int(input('Digite a senha: \n'))

if login == request_login and password == request_password:
    os.system('cls')
    print('Acesso liberado')
else:
    os.system('cls')
    print('Senha ou login inválidos. Tente novamente')

