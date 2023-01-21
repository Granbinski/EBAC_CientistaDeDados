from time import sleep


class Pessoa(object):
    def __init__(self, nome: str, idade: int, documento: str = None):
        self.nome = nome
        self.idade = idade
        self.documento = documento

    def dormir(self, horas: int) -> None:
        for hora in range(1, horas + 1):
            print(f'Dormindo por {hora} horas')
            sleep(1)

    def falar(self, texto: str) -> None:
        print(texto)

    def __str__(self) -> str:
        return f'{self.nome}, {self.idade} anos e ' + \
            f'documento numero {self.documento}'


class Universidade(object):
    def __init__(self, nome: str):
        self.nome = nome


class Estudante(Pessoa):
    def __init__(
        self,
        nome: str,
        idade: int,
        documento: str,
        universidade: Universidade
    ):
        super().__init__(nome=nome, idade=idade, documento=documento)
        self.universidade = universidade


usp = Universidade(
    nome='Universidade de São Paulo'
)

andre = Estudante(
    nome='Andre Perez',
    idade=30,
    documento='123',
    universidade=usp
)

print(andre)

print(andre.universidade.nome)
