class Mobilia:
    def __init__(self, codigo: int, descricao: str):
        self.__codigo = codigo
        self.__descricao = descricao

        @property
        def codigo(self):
            return self.__codigo

        @codigo.setter
        def codigo(self, nuevo: int):
            self.__codigo = nuevo

        @property
        def descricao(self):
            return self.__codigo

        @descricao.setter
        def descricao(self, nuevo: str):
            self.__descricao = nuevo
