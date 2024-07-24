'''
pegar a frase
separar as palavras em unidades
saber qual palavra o usuário deseja consultar
verificar quantas vezes a palavra está presente na frase  

'''

texto = '''
O candidato relembrou o dia do atentado. 
Ele comentou que as pessoas na plateia não o abandonaram, mesmo após ouvirem
 os tiros, e fez uma homenagem a Corey Comperatore, que foi baleado e morreu.

Trump também chamou Kamala Harris de mentirosa. Ele criticou a 
postura da democrata como vice-presidente e citou a Ucrânia como exemplo. 
Segundo o ex-presidente, uma vitória de Kamala seria "desastrosa".

Ao se referir à desistência de Joe Biden de concorrer à reeleição, Trump 
disse que o presidente desistiu porque perderia.

"Ele não queria sair, mas fizeram ele sair. Disseram pra ele 'você não 
consegue vencer' [...] Se começarmos a abrir vantagem para Kamala, eles vão trazer
 um terceiro candidato?"

Como nos discursos anteriores, o ex-presidente criticou as políticas econômica
 e de imigração da gestão de Joe Biden.
'''

contagem_palavras = {}
palavras = texto.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)