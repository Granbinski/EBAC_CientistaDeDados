# Classes

from time import sleep


class Pessoa(object):
    def __init__(self):
        pass

# Atributos


class Pessoa(object):
    def __init__(self, nome: str, idade: int, documento: str):
    self.nome = nome
    self.idade = idade
    self.documento = documento

# Metodos


class Pessoa(object):
    def __init__(self, nome: str, idade: int, documento: str = None):
        self.nome = nome
        self.idade = idade
        self.documento = documento

    def dormir(self, horas: int) -> None:
        for horas in range(1, doras+1):
            print(f'Dormir por {horas} horas')
            sleep(1)

    def falar(self, texto: str) -> None:
        print(texto)

    def __str__(self) -> str:
        return f'{self.nome}, {self.idade} anos e ' + \
            f'documento numero{self.documento}'
