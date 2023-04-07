from Imovel import Imovel


class Imobiliaria:
    def __init__(self):
        self.__imoveis = []

    @property
    def imoveis(self):
        return self.__imoveis

    def incluir_imovel(self, imovel: Imovel):
        # Nao esqueca de garantir que o objeto recebido pertence a classe Imovel...
        # Nao permitir insercao de Imoveis duplicados!
        ...

    def excluir_imovel(self, imovel: Imovel):
       ...
