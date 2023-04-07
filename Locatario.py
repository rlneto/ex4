class Locatario:
    def __init__(self, codigo: int, nome: str, telefone: int):
        self.__codigo = codigo
        self.__nome = nome
        self.__telefone = telefone

        @property
        def codigo(self):
            return self.__codigo

        @codigo.setter
        def codigo(self, nuevo: int):
            self.__codigo = nuevo

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
