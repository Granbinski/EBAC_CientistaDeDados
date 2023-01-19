numeros = [1, 2, 3]
numeros_ao_cubo = map(lambda num: num ** 3, numeros)
print(list(numeros_ao_cubo))

emails = [
    'andre.perez@gmail.com',
    'andre.perez@live.com',
    'andre.perez@yahoo.com'
]
def extrair_provedor_email(email): return email.split(sep='@')[-1]


provedores = []
for email in emails:
    provedor = extrair_provedor_email(email)
    provedores.append(provedor)
print(provedores)

provedores = map(extrair_provedor_email, emails)
print(provedores)

provedores = list(map(extrair_provedor_email, emails))
print(provedores)

provedores = map(lambda email: email.split(sep='@')[-1], emails)
print(list(provedores))

anos = [10, 10, 10]
taxas_juros = [0.05, 0.10, 0.15]
valores_iniciais = [1000, 1000, 1000]


def retorno(valor_inicial: float, taxa_juros: float, anos: int) -> float:
    valor_final = valor_inicial
    for ano in range(1, anos+1):
    valor_final = valor_final * (1+taxa_juros)
    return round(valor_final, 2)


cenarios = list(map(retorno, valores_iniciais, taxas_juros, anos))
print(cenarios)
