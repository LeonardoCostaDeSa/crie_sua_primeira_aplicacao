import os

restaurantes = [{'nome':'Praça', 'categoria':'japonesa', 'ativo':False}, 
                {'nome':'Pizza suprema', 'categoria': 'italiana', 'ativo': True},
                {'nome': 'Boa comida', 'categoria': 'Marmita', 'ativo': True}]

def exibir_nome_do_programa():
   '''
   Essa exidbe na tela o nome do programa
   '''
   
print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")
def exibir_opcoes():
    '''
    Essa função exibe ao usuário todas as opções que o programa oferece

    '''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar status do restaurante')
    print('4. Sair\n')
def finalizar_app():
    '''
    Essa função encerra a sessão do app
    '''

    exibir_subtitulo('Finalizando app')
def opcao_invalida():
    '''
    Essa opção será chamada logo que o usuário digitar uma opção inválida
    e chamará a função menu inicial para que o usuário possa tentar novamente
    '''

    exibir_subtitulo('Você digitou uma opção inválida.')
    voltar_ao_menu()
def mudar_status_restaurante():
    '''
    Essa função altera o status do restaurante de ativo para inativo e vice-versa

    Input: recebe o nome do restaurante que o usuário deseja alterar

    Output: retorna uma mensagem de que o status foi alterado
    '''
    
    exibir_subtitulo('Mudar status do restaurante')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja mudar o status: \n')
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_do_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_do_restaurante} foi ativado com sucesso!' if restaurante['ativo'] else f'restaurante {nome_do_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('o restaurante não foi encontrado')
    voltar_ao_menu()
def voltar_ao_menu():
    '''
    Essa função faz o usuário voltar ao menu inicial 

    Input: qualquer tecla apertada pelo usuário
    Output: chama a função main()
    '''
    input('Aperte qualquer tecla para voltar ao menu\n')
    main()
def escolher_opcao():
    '''
    Essa função possibilita oa usuário escolher a opção desejada

    Input: número da opção escolhida
    Output: Chama as funções correspondentes à escolha do 
    
    OBS: Foi feito um try/except para tratar possíveis erros sem quebrar o programa 
    '''
    
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1: 
            cadastrar_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurantes()
        elif opcao_escolhida == 3: 
            mudar_status_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()
def main():
    '''
    Essa é a função principal do sistema. Ela chama três funções para iniciar a interação com o usuário
    '''

    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
def cadastrar_restaurante():
    '''
    Essa função cadastra um novo restaurante no sistema
    
    Input: Recebe o nome do restaurante e suas respectivas categorias e status
    Output: Registra os dados do restaurante na lista de dicionário correspondente
    '''
    exibir_subtitulo('Exibindo restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante: ')
    categoria = input(f'\nDigite o nome da categoria do restaurante {nome_do_restaurante}:')
    dados_do_restaurante = {'nome': nome_do_restaurante, 
                            'categoria': categoria,
                            'ativo': False}
    restaurantes.append(dados_do_restaurante)
    exibir_subtitulo(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    voltar_ao_menu()
def listar_restaurantes():
    '''
    Mostra todos os restaurantes que estão cadastrados 

    Input: --
    Output: Mostra todos os restaurantes cadastrados, suas categorias e o respectivo status
    '''
    exibir_subtitulo('Listando os restaurantes')
    print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status\n')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu()
def exibir_subtitulo(texto):
    '''
    Essa função é usada para apresentar em cada uma das telas, qual a funcionalidade do sistema
    está sendo usada
    '''
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(texto)
    print(linha)
    print('\n')    
if __name__ == '__main__':
    main()