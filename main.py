# NOME: GUILHERME HENRIQUE EDUARDO DE LARA PERES

# Para  obter  os  pontos  relativos  a  este  trabalho,  você  deverá  criar  um  programa,  utilizando  a
# linguagem  Python, C, ou C++.  Este  programa,  quando  executado,  irá  apresentar  os  resultados  de
# operações que serão realizadas entre dois conjuntos de dados.
# O  programa  que  você  desenvolverá  irá  receber  como  entrada um arquivo de texto  (.txt)
# contendo vários conjuntos de dados e várias operações. Estas operações e dados estarão representadas
# em um arquivo de textos contendo apenas os dados referentes as operações que devem ser realizadas
# segundo a seguinte regra fixa: a primeira linha do arquivo de texto de entrada conterá o número de
# operações  que  estão  descritas  no  arquivo,  este  número  de  operações  será  um  inteiro;  as  linhas
# seguintes  seguirão  sempre  o  mesmo  padrão  de  três  linhas:  a  primeira  linha  apresenta  o  código  da
# operação  (U para união, I para interseção, D para diferença e C produto cartesiano),  a  segunda  e
# terceira linhas conterão os elementos dos conjuntos separados por virgulas. A seguir está um exemplo
# das linhas que podem existir em um arquivo de testes para o programa que você irá desenvolver:
# 4
# U
# 3, 5, 67, 7
# 1, 2, 3, 4
# I
# 1, 2, 3, 4, 5
# 4, 5
# D
# 1, A, C, 34
# A, C, D, 23
# C
# 3, 4, 5, 5, A, B, R
# 1, B, C, D, 1
# Neste exemplo temos 4 operações uma união (U), uma interseção (I), um diferença (D) e um
# produto cartesiano (C). A união, definida por U, deverá ser executada sobre os conjuntos {𝟑,𝟓,𝟔𝟕,𝟕} e
# {𝟏,𝟐,𝟑,𝟒}, cujos elementos estão explicitados nas linhas posteriores a definição da operção (U).
# A resposta do seu programa deverá conter a operação realizada, descrita por extenso, os dados
# dos conjuntos identificados, e o resultado da operação. No caso da união a linha de saída deverá conter
# a informação e a formatação mostrada a seguir:
# União: conjunto 1 {3,5,67,7}, conjunto 2 {1,2,3,4}. Resultado: {3,5,67,7,1,2,4}
# Seu programa deverá mostrar a saída no terminal, ou em um arquivo de textos. Em qualquer
# um dos casos, a saída será composta por uma linha de saída para cada operação constante no arquivo
# de  textos  de  entrada  formatada  segundo  o  exemplo  de  saída  acima.  Observe  as  letras  maiúsculas  e
# minúsculas, e os pontos utilizados na formatação da linha de saída apresenta acima.
# No  caso  do  texto  de  exemplo,  teremos  4  linhas,  e  apenas  4  linhas  de  saída,  formatadas  e
# pontuadas conforme o exemplo de saída acima. O uso de linhas extras na saída, ou erros de formatação,
# implicam em perda de pontos como pode ser visto na rubrica de avaliação constante neste documento.
# Para que seu programa possa ser testado você deve criar, no mínimo, três arquivos de entrada
# contendo um número diferente de operações, operações com dados diferentes, e operações em ordem
# diferentes.  Os  arquivos  de  entrada  criados  para  os  seus  testes  devem  estar  disponíveis  tanto  no
# ambiente repl.it quanto no ambiente Github.
# Observe que o professor irá testar seu programa com os arquivos de testes que você criar e com,
# no mínimo um arquivo de testes criado pelo próprio professor.

def trabalhar_conjuntos(arquivo):
    with open(arquivo) as teste:  # Apenas lendo o documento
        linhas = teste.readlines()
    conteudo = [x.rstrip('\n').replace(' ', '') for x in linhas]
    for val in conteudo:
        if val == '':
            conteudo.remove(val)
    
    contador = 0
    novo = {}
    for i in range(0, len(conteudo) -2, 3):  # Criei um dicionário para armazenar os valores
        if conteudo[i].isalpha():
            novo[conteudo[i].rstrip(' ').upper() + f'{contador}'] = [
            [int(x) if x.isnumeric() else x for x in conteudo[i + 1].split(sep=',')],
            [int(x) if x.isnumeric() else x for x in conteudo[i + 2].split(sep=',')]
        ]
        contador += 1

    diferentes = [] # Removi os valores que se repetem
    for item in novo:
        for x in range(2):
            for valor in novo[item][x]:
                if valor not in diferentes:
                    diferentes.append(valor)
            novo[item][x] = diferentes.copy()
            diferentes.clear()
    teste.close()
    return novo


def verifica(operacao, conjunto1, conjunto2):
    if operacao == 'U':
        uniao = []
        for valor in conjunto1:
            uniao.append(valor)
        for valor in conjunto2:
            if valor not in uniao:
                uniao.append(valor)
        uniao.sort(key=lambda val: ([str,int].index(type(val)), val)) # Organizando o resultado para uma melhor leitura
        return f'União: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {uniao}'
    elif operacao == 'I':
        intersec = []
        for valor in conjunto1:
            if valor in conjunto2:
                intersec.append(valor)
        intersec.sort(key=lambda val: ([str,int].index(type(val)), val))
        return f'Interseção: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {intersec}'
    elif operacao == 'D':
        diference = []
        for valor in conjunto1:
            if valor not in conjunto2:
                diference.append(valor)
        diference.sort(key=lambda val: ([str,int].index(type(val)), val))
        return f'Diferença: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {diference}'
    elif operacao == 'C':
        cartesiano = []
        for v1 in conjunto1:
            for v2 in conjunto2:
                cartesiano.append((v1, v2))
        return f'Produto Cartesiano: conjunto 1 {conjunto1}, conjunto 2 {conjunto2}. Resultado: {cartesiano}'
    else:
        return False

dicionario = trabalhar_conjuntos('teste1.txt')  # Digite Aqui o nome do arquivo que deseja ler
for key in dicionario:
    if verifica(key[0], dicionario[key][0], dicionario[key][1]):
        print(verifica(key[0], dicionario[key][0], dicionario[key][1]))
        print()
