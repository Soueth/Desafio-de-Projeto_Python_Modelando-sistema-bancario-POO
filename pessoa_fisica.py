from datetime import date
from typing import Union

from cliente import Cliente

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

    @property
    def senha(self):
        return self._senha
    
    @property
    def nome(self):
        return self.nome

    @property
    def data_nascimento(self):
        return self._data_nascimento
    
    @property
    def cpf(self):
        return self._cpf