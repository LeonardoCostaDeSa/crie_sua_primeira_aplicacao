import os

restaurantes = [{'nome':'Praça', 'categoria':'japonesa', 'ativo':False}, 
                {'nome':'Pizza suprema', 'categoria': 'italiana', 'ativo': True},
                {'nome': 'Boa comida', 'categoria': 'Marmita', 'ativo': True}]

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")
def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alterar status do restaurante')
    print('4. Sair\n')
def finalizar_app():
    exibir_subtitulo('Finalizando app')
def opcao_invalida():
    exibir_subtitulo('Você digitou uma opção inválida.')
    voltar_ao_menu()
def mudar_status_restaurante():
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
    input('Aperte qualquer tecla para voltar ao menu\n')
    main()
def escolher_opcao():
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
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()
def cadastrar_restaurante():
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
    exibir_subtitulo('Listando os restaurantes')
    print(f'{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status\n')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu()
def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(texto)
    print(linha)
    print('\n')    
if __name__ == '__main__':
    main()