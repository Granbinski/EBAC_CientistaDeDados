valor_inicial, taxa_juros_anual, anos = 1000.00, 0.05, 10
valor_final = valor_inicial
for ano in range(1, anos+1):
    valor_final = valor_final * (1 + taxa_juros_anual)
valor_final = round(valor_final, 2)
print(f'Para um valor inicial de R$ {valor_inicial} ' +
      f'e uma taxa de juros anual de {taxa_juros_anual}, ' +
      f'em {anos} anos você terá R$ {valor_final}'
      )
valor_inicial, taxa_juros_anual, anos = 1020.00, 0.03, 10
valor_final = valor_inicial
for ano in range(1, anos+1):
    valor_final = valor_final * (1 + taxa_juros_anual)
valor_final = round(valor_final, 2)
print(f'Para um valor inicial de R$ {valor_inicial} ' +
      f'e uma taxa de juros anual de {taxa_juros_anual}, ' +
      f'em {anos} anos você terá R$ {valor_final}'
      )


def imprime(mensagem: str):
    print(mensagem)


texto = 'Fala pessoal, meu nome é André Perez!'

imprime(mensagem='Fala pessoal, meu nome é André Perez!')


def maiusculo(texto: str) -> str:
    text_maiusculo = texto.upper()
    return text_maiusculo


nome = 'André Perez'
print(nome)
nome_maiusculo = maiusculo(texto=nome)
print(nome_maiusculo)


def extrair_usuario_email_provedor(email: str) -> (str, str):
    email_separado = email.split(sep='@')
    usuario = email_separado[0]
    provedor = email_separado[1]
    return usuario, provedor


email = 'andre.perez@gmail.com'
usuario, provedor = extrair_usuario_email_provedor(email=email)
print(usuario)
print(provedor)


def pi() -> float:
    return 3.14159265359


pi = pi()
print(pi)


def imprime_pi() -> None:
    print(3.14159265359)
    return None


imprime_pi()


def escreve_arquivo_csv(nome: str, cabecalho: str, conteudos: list) -> bool:
    try:
    with open(file=nome, mode='w', encoding='utf8') as fp:
    linha = cabecalho + '\n'
    fp.write(linha)
    for conteudo in conteudos:
    linha = str(conteudo) + '\n'
    fp.write(linha)
    except Exception as exc:

    print(exc)
    return False
    return True


nome = 'idades-funcao-erro.csv'
cabecalho = 'idade'
# conteudos = [30, 33, 35, 30, 59, 35, 36, 39, 41, 43]
conteudos = 10
escreveu_com_sucesso = escreve_arquivo_csv(
    nome=nome,
    cabecalho=cabecalho,
    conteudos=conteudos
)
print(escreveu_com_sucesso)

nome = 'idades-funcao-erro.csv'
cabecalho = 'idade'
# conteudos = [30, 33, 35, 30, 59, 35, 36, 39, 41, 43]
conteudos = 10
escreveu_com_sucesso = escreve_arquivo_csv(
    nome=nome,
    cabecalho=cabecalho,
    conteudos=conteudos
)
print(escreveu_com_sucesso)


def juros_compostos_anual(
    valor_inicial: float,
    taxa_juros_anual: float,
    anos: int
) -> float:
    valor_final = valor_inicial
    for ano in range(1, anos+1):
    valor_final = valor_final * (1 + taxa_juros_anual)
    valor_final = round(valor_final, 2)
    print(f'Para um valor inicial de R$ {valor_inicial} ' +
          f'e uma taxa de juros anual de {taxa_juros_anual}, ' +
          f'em {anos} anos você terá R$ {valor_final}'
          )
    return valor_final


valor_inicial, taxa_juros_anual, anos = 1000.00, 0.05, 10
valor_final = juros_compostos_anual(
    valor_inicial=valor_inicial,
    taxa_juros_anual=taxa_juros_anual,
    anos=anos
)
valor_inicial, taxa_juros_anual, anos = 1020.00, 0.03, 10
valor_final = juros_compostos_anual(
    valor_inicial=valor_inicial,
    taxa_juros_anual=taxa_juros_anual,
    anos=anos
)
