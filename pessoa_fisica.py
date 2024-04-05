from datetime import date
from typing import Union

from cliente import Cliente
from conta import Conta

class PessoaFisica(Cliente):
    def __init__(
        self, 
        endereco: str, 
        cpf: str, 
        nome: str, 
        data_nascimento: date,
        senha: str
    ):
        super().__init__(endereco)
        self._cpf: str = cpf
        self._nome: str = nome
        self._data_nascimento: date = data_nascimento
        self._senha = senha
