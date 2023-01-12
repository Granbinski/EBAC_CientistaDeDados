# STrings

# sua empresa
lat = '-22.005320'
lon = '47.891040'

# startup adiquirida
latlon = '-22.005320;-47.891040'

nome_aula = "Aula 04, Modulo 01, Strings"
print(nome_aula)
print(type(nome_aula))

string_vazia = ""
print(string_vazia)
print(type(string_vazia))

# concatenacao

nome = 'Inacio'
sobrenome = "Granbinski"
apresentacao = 'Ola, meu nome e ' + nome + " " + sobrenome + "."
print(apresentacao)
apresentacao = f'Ola, meu nome e {nome} {sobrenome}.'
print(apresentacao)


# Fatiamento

email = 'inacioteste@gmail.com'

print('0: ' + email[0])
print('11: ' + email[11])
print('-1: ' + email[-1])
print('-2: ' + email[-2])


# Fatiamento por intervalo

email_usuario = email[0:11]
print(email_usuario)

email_provedor = email[12:-1]
print(email_provedor)

# Metodos

endereco = "Avenida Paulista, 1811, São Paulo, São Paulo, Brasil."

print(endereco.upper())
posicao = endereco.find('Brasil')
print(posicao)

print(endereco.replace('Avenida', 'Av'))
