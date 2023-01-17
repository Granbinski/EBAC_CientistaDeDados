if True:
    print("Verdadeiro")
else:
    print("Falso")

codigo_de_seguranca = '291'
codigo_de_seguranca_cadastro = '010'
pode_efetuar_pagamento = codigo_de_seguranca == codigo_de_seguranca_cadastro
print(pode_efetuar_pagamento)

if pode_efetuar_pagamento:
    print("Pagamento efetuado")
else:
    print("Erro: Código de segurança inválido")

if codigo_de_seguranca == codigo_de_seguranca_cadastro:
    print("Pagamento efetuado")
else:
    print("Erro: Código de segurança inválido")

codigo_de_seguranca = '852'
codigo_de_seguranca_cadastro = '852'
senha = '7783'
senha_cadastro = '7783'

if (codigo_de_seguranca == codigo_de_seguranca_cadastro) & \
        (senha == senha_cadastro):
    print("Pagamento efetuado")
else:
    print("Erro: Pagamento não efetuado")

if (codigo_de_seguranca != codigo_de_seguranca_cadastro) | \
        (senha != senha_cadastro):
    print("Erro: Pagamento não efetuado")
else:
    print("Pagamento efetuado")

codigo_de_seguranca = '802'
codigo_de_seguranca_cadastro = '852'
senha = '7703'
senha_cadastro = '7783'


if (codigo_de_seguranca == codigo_de_seguranca_cadastro) & \
        (senha == senha_cadastro):
    print("Pagamento efetuado")
elif (codigo_de_seguranca != codigo_de_seguranca_cadastro) & \
        (senha == senha_cadastro):
    print("Erro: Código de segurança inválido")
elif (codigo_de_seguranca == codigo_de_seguranca_cadastro) & \
        (senha != senha_cadastro):
    print("Erro: Senha inválida inválida")
else:
    print("Erro: Código de segurança e senha inválidos")

# Estrutura condicional try /except / finally

preco = 132.85
pessoas = 0
valor_por_pessoa = preco / pessoas

nome = 'Andre Perez'
idade = True

apresentacao = 'Fala pessoal, meu nome é ' + nome + \
    ' e eu tenho ' + idade + ' anos'

anos = [2019, 2020, 2021]

ano_atual = anos[3]

cursos = {
    'python': {
        'nome': 'Python para Análise de Dados', 'duracao': 2.5
    },
    'sql': {
        'nome': 'SQL para Análise de Dados', 'duracao': 2
    }
}

curso_atual = cursos['analista']

# Try / Except

preco = 132.85
pessoas = 2
try:
    valor_por_pessoa = preco / pessoas
    print(valor_por_pessoa)
except ZeroDivisionError:
    print('Número de pessoas inválido. ' +
          'Espera-se um valor maior que 0 e obteve-se um valor igual a ' +
          str(pessoas)
          )

anos = [2019, 2020, 2021]
try:
    ano_atual = anos[3]
    print(ano_atual)
except Exception:
    print('Lista de anos é menor que o valor escolhido. ' +
          'Espera-se um valor entre 0 e ' +
          str(len(anos) - 1)
          )

anos = [2019, 2020, 2021]
try:
    ano_atual = anos[3]
    print(ano_atual)
except Exception as exc:
    print('Descrição da exceção: ' + str(exc))
    print('Tipo da exceção: ' + str(type(exc)))
    print('Lista de anos é menor que o valor escolhido. ' +
          'Espera-se um valor entre 0 e ' +
          str(len(anos) - 1)
          )


anos = [2019, 2020, 2021]
try:
    ano_atual = anos[3]
    print(ano_atual)
except IndexError:
print('Lista de anos é menor que o valor escolhido. ' +
      'Espera-se um valor entre 0 e ' +
      str(len(anos) - 1)
      )
except Exception as exc:
    print(exc)
    print('Erro genérico')

# try / except / finally

nome = 'Andre Perez'
idade = 19
try:
    apresentacao = 'Fala pessoal, meu nome é ' + nome + \
        ' e eu tenho ' + idade + ' anos'
    print(apresentacao)
except TypeError:
    idade = str(idade)
finally:
    print('Segunda chance')
    apresentacao = 'Fala pessoal, meu nome é ' + nome + \
        ' e eu tenho ' + idade + ' anos'
    print(apresentacao)

for valor in range(6):
    print(valor)

soma = 0
for valor in range(0, 100000):
    soma = soma + valor
    # print(soma)
print(soma)

for multiplo_dois in range(2, 10, 3):
    print(multiplo_dois)

frutas = ['maca', 'banana', 'laranja', 'uva', 'pera']
for fruta in frutas:
    print(fruta)


frase = 'Fala pessoal, meu nome é André Perez.'
for caracter in frase:
    if (caracter == 'A') | (caracter == 'z'):
    print(f"A letra '{caracter}' está presente na frase.")

credito = {'123': 750, '456': 812, '789': 980}

for chave, valor in credito.items():
    print(f'Para o documento {chave}, ' +
          'o valor do escore de crédito é {valor}.'
          )
    print('\n')

for chave in credito.keys():
    print(chave)
    print(credito[chave])
    print(f'Para o documento {chave}, ' +
          'o valor do escore de crédito é {credito[chave]}.'
          )
    print('\n')

for valor in credito.values():
    print(valor)
    print(f'O valor do escore de crédito é {valor}, ' +
          'mas não temos mais as chaves :(.'
          )
    print('\n')

# break / continue

for i in range(0, 10*10*10*10*10*10):
    print(i)
    if i == 10:
    break

numero = 3
if numero % 2 == 0:
    print(f'O numero {numero} é par')
else:
    print(f'O numero {numero} é impar')


numeros = [361, 553, 194, 13, 510, 33, 135]
for numero in numeros:
    if numero % 2 == 0:
    print(f'O numero {numero} é par')
    break
    else:
    print(f'O numero {numero} é impar')

numeros = [361, 553, 194, 13, 510, 33, 135]
for numero in numeros:
    if numero % 2 == 0:
    print(f'O numero {numero} é par')
    break
    else:
    continue
    print(f'O numero {numero} é impar')
