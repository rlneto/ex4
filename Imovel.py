from Locatario import Locatario
from Locador import Locador
from Mobilia import Mobilia

class Imovel:
    def __init__(self, codigo: int, descricao: str, valor: float, locador: Locador):
        # Criar todos os atributos, incluindo as listas
        ...

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo: int):
        self.__codigo = codigo

    ... Adicionar demais getters
    
    ... Adicionar demais setters
    

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
