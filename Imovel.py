from Locatario import Locatario
from Locador import Locador
from Mobilia import Mobilia

class Imovel:
    def __init__(self, codigo: int, descricao: str, valor: float, locador: Locador):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__valor = valor
        self.__locador = locador

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, nuevo: str):
        self.__descricao = nuevo

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, nuevo: float):
        self.__valor = nuevo

    @property
    def locador(self):
        return self.__locador

    @locador.setter
    def locador(self, locador: Locador):
        self.__locador = locador

    def incluir_locatario(self, locatario: Locatario):

        # Nao esqueca de garantir que o objeto recebido pertence a classe Locatario...
        # Nao permitir insercao de Locatarios duplicados!
        ...

    def excluir_locatario(self, codigo_locatario: int):
        ...

    def incluir_mobilia(self, codigo_mobilia: int, descricao_mobilia: str):
        ... Nao permitir insercao de Mobilias duplicadas!

    def excluir_mobilia(self, codigo_mobilia: int):
        ...

    def find_locatario_by_codigo(self, codigo_locatario: int):
        # Procura na lista de locatarios se existe um Locatario com este codigo 
        # Se encontrar, retorna o Locatario encontrado
        ...
