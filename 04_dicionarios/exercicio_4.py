chaves = [{'chave': 54}, {'chave': 26}, {'chave': 63}]
pergunta = int(input('Digite um número: '))


def verificar_chave(valor, lista_de_dicionario):
    for dicionario in lista_de_dicionario:
        if valor in dicionario.values():
            return True
    return False


mensagem = 'Chave correta' if verificar_chave(pergunta, chaves) else 'Chave incorreta'

print(mensagem)

# mensagem = 'Chave correta' else 'Chave incorreta'
