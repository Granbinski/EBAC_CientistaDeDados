with open(file='idades.csv', mode='w', encoding='utf8') as fp:
    linha = 'idade' + '\n'
    fp.write(linha)
    for idade in idades:
    linha = str(idade) + '\n'
    fp.write(linha)


with open(file='idades.csv', mode='a', encoding='utf8') as fp:
    for idade in idades:
    linha = str(idade + 100) + '\n'
    fp.write(linha)

with open(file='./banco-texto.txt', mode='r', encoding='utf8') as leitura:
    with open(file='./banco-csv.csv', mode='w', encoding='utf8') as escrita:
    linha = leitura.readline()
    while linha:
    escrita.write(linha)
    linha = leitura.readline()
