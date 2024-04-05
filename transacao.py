from datetime import date

# from conta import Conta
from interfaces.transacao_interface import ITransacao

class Transacao(ITransacao):
    pass
    # def __init__(self, data: date, valor: float, conta: Conta) -> None:
    #     super().__init__(data, valor)

    # @classmethod
    # def registrar(
    #     self, 
    #     conta: Conta, 
    #     valor: float, 
    #     data: date
    # ) -> ITransacao:
    #     return Transacao(data = data, valor = valor, conta = Conta)