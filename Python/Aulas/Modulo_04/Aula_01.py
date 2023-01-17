conteudo = None
with open(file='./banco.csv', mode='r', encoding='utf8') as arquivo:
    conteudo = arquivo.read()
print(conteudo)

conteudo = []
with open(file='./banco.csv', mode='r', encoding='utf8') as arquivo:
    linha = arquivo.readline()  # lê a primeira linha
    while linha:
    conteudo.append(linha)
    linha = arquivo.readline()  # lê uma nova linha, se a linha não existir,
    # salva o valor None
print(conteudo)

:
for linha in conteudo:
    print(linha)

idades = []
with open(file='./banco.csv', mode='r', encoding='utf8') as arquivo:
    linha = arquivo.readline()  # lê o cabeçalho
    linha = arquivo.readline()  # lê a primeira linha
    while linha:
    linha_separada = linha.split(sep=',')  # quebra a string nas virgulas e
    # salva os resultados em uma lista
    idade = linha_separada[0]  # seleciona o primeiro elemento da lista
    idade = int(idade)  # converte o valor de string para integer (inteiro)
    idades.append(idade)  # salva o valor na lista de idades
    linha = arquivo.readline()  # lê uma nova linha, se a linha não existir,
    # salva o valor None
print(idades)
