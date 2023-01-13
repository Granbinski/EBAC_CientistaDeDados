# Booleanos

usuario = 'inacio.granbinski'
senha = 'inacio123'

usuario_cadastro = 'andre.perez'
senha_cadastro = 'inacio321'

verdadeiro = True
print(verdadeiro)

falso = False
print(falso)

print('\n')
print('=' * 20)
print('\n')

saldo_em_conta = 200
valor_do_saque = 100

pode_executar_saque = valor_do_saque <= saldo_em_conta
print(pode_executar_saque)

print('\n')
print('=' * 20)
print('\n')

codigo_de_seguranca = '852'
codido_sec_cadastrado = '010'

pode_pagar = codigo_de_seguranca == codido_sec_cadastrado
print(pode_pagar)

print('\n')
print('=' * 20)
print('\n')

print(True | True)
print(True | False)
print(False | False)
print(False | True)

print('\n')
print('=' * 20)
print('\n')

print(True & True)
print(True & False)
print(False & False)
print(False & True)


print('\n')
print('=' * 20)
print('\n')

print(not True)
print(not False)

print('\n')
print('=' * 20)
print('\n')

# Conversao

idade = 19
tipo_sangue = '-0'
filhos = 0
telefone_fixo = None
telefone_fixo2 = ''

print(bool(idade))
print(bool(tipo_sangue))
print(bool(filhos))
print(bool(telefone_fixo))
print(bool(telefone_fixo2))

print('\n')
print('=' * 20)
print('\n')

usuario_igual = usuario == usuario_cadastro
senha_igual = senha == senha_cadastro

print(usuario_igual)
print(senha_igual)

conceder_acesso = usuario_igual & senha_igual
print(f'O acesso e {conceder_acesso}')
