from Locatario import Locatario
from Locador import Locador
from Mobilia import Mobilia

class Imovel:
    def __init__(self, codigo: int, descricao: str, valor: float, locador: Locador ):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__valor = valor
        self.__locador = locador
        self.__locatarios = list()
        self.__mobilias = list()

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

    @property
    def locatarios(self):
        return self.__locatarios

    @property
    def mobilias(self):
        return self.__mobilias

    def incluir_locatario(self, locatario: Locatario):
        if isinstance(locatario, Locatario) and locatario not in self.locatarios:
            self.__locatarios.append(locatario)
        else:
            print("Seu tanso!")
    def excluir_locatario(self, codigo_locatario: int):
        for tanso in self.locatarios:
            if tanso.codigo == codigo_locatario:
                self.__locatarios.pop(self.__locatarios.index(tanso))
                break

    def incluir_mobilia(self, codigo_mobilia: int, descricao_mobilia: str):
        self.__mobilias.append(Mobilia(codigo_mobilia, descricao_mobilia))

    def excluir_mobilia(self, codigo_mobilia: int):
        for mobilia in self.mobilias:
            if mobilia.codigo == codigo_mobilia:
                self.__mobilias.pop(self.__mobilias.index(mobilia))
                break

    def find_locatario_by_codigo(self, codigo_locatario: int):
        for tanso in self.locatarios:
            if tanso.codigo == codigo_locatario:
                return tanso
