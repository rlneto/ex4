class Locador:
    def __init__(self, cpf: int, nome: str, telefone: int, endereco: str):
        self.__cpf = cpf
        self.__nome = nome
        self.__telefone = telefone
        self.__endereco = endereco

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nuevo: str):
        self.__nome = nuevo

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, nuevo: int):
        self.__telefone = nuevo

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, nuevo: str):
        self.__endereco = nuevo

