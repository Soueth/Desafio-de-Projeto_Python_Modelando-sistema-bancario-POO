from datetime import date

from .conta import Conta
from interfaces.cliente_interface import ICliente

class PessoaFisica(ICliente):
    def __init__(
        self, 
        endereco: str, 
        conta: Conta, 
        cpf: str, 
        nome: str, 
        data_nascimento: date,
        senha: str
    ):
        super().__init__(endereco, conta)
        self._cpf: str = cpf
        self._nome: str = nome
        self._data_nascimento: date = data_nascimento
        self._senha = senha
