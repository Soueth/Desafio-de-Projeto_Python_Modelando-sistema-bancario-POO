from datetime import datetime
from typing import List, Union, TypeVar
from abc import ABC

from interfaces.transacao_interface import ITransacao
from pessoa_fisica import PessoaFisica, Cliente

class App():
    clientes = []

    def __init__(self) -> None:
        self._acesso: int = 0
        self._cliente: Cliente

    @property
    def acesso(self) -> int:
        return self._acesso
    
    @acesso.setter
    def acesso(self, acesso: int) -> None:
        self._acesso = acesso

    @property
    def cliente(self):
        return self._cliente

    @cliente.setter
    def cliente(self, cliente):
        self._cliente = cliente
        self.clientes.append(cliente)

    def main(self):
        menu = """Escolha uma opção:
            1 - Depositar
            2 - Sacar
            3 - Visualizar historico
            0 - Sair/Finalizar
        """

        while True:
            opcao_cadastro = int(input("""
                Bem-vindo(a) ao nosso banco!!!
                
                |Digite - 1| = Se já tem um cadastro e deseja fazer login.
                |Digite - 2| = Se gostaria de criar um novo usuário.
                |Digite - 3| = Se gostaria de listar todos os usuarios.
                |Digite - 0| = Se gostaria de sair.
            """))

            if opcao_cadastro == 1:
                self.autenticar()

            if opcao_cadastro == 2:
                # self.clientes.append(fazer_cadastro(self.clientes))
                self.cliente = self.fazer_cadastro()

            if opcao_cadastro == 3:
                for i, cliente in enumerate[self.clientes]:
                    print("""Usuario {i} - {cliente.nome} - {cliente.cpf}""")

            if (opcao_cadastro == 0) or (self.acesso == 1):
                break

        while(self.acesso == 1):
            opcao_operacao = int(input("""
                |Digite - 1| = Se gostaria de fazer uma operação.
                |Digite - 2| = Se gostaria de criar uma nova conta.
                |Digite - 3| = Se gostaria de listar suas contas.
                |Digite - 0| = Se gostaria de sair.                       
            """))

            if opcao_operacao == 1:
                while True:
                    conta = self.logar_conta()
                    if conta:
                        break

                while (conta):
                    opcao = int(input(menu))

                    if opcao == 1:
                        valor = float(input("Qual o valor a ser depositado?\n"))
                        conta.depositar = valor

                    elif opcao == 2:
                        while True:
                            valor = float(input("Qual o valor a sar sacado?\n"))
                            outro_saque = conta.sacar - valor

                            if not outro_saque:
                                break
                            
                            print("Gostaria de fazer outro saque?\n")
                            print("     | 0 - NÃO |\n")
                            outro_saque = int(input("     | 1 - SIM |\n"))

                            if outro_saque == 0:
                                break
                    
                    elif opcao == 3:
                        print(conta.historico)

                    elif opcao == 4:
                        break
                    # if opcao == 1:
                    #     valor = float(input("Qual o valor a ser depositado?\n"))
                    #     extrato_deposito = float()
                    #     extrato_deposito, saldo = deposito(saldo, valor, extrato_deposito)

                    # elif opcao == 2:
                    #     while True:
                    #         valor = float(input("Qual o valor a sar sacado?\n"))
                    #         saldo, numero_saques =saque(valor=valor, limite=limite, extrato_saldo=extrato_saldo, saldo=saldo, numero_saques=numero_saques, limite_saques=limite_saques)
                    #         print(f"Seu saldo é de R$ {float(saldo):.2f}")

                    #         if numero_saques >= limite_saques:
                    #             break
                            
                    #         print("Gostaria de fazer outro saque?\n")
                    #         print("     | 0 - NÃO |\n")
                    #         outro_saque = int(input("     | 1 - SIM |\n"))

                    #         if outro_saque == 0:
                    #             break

                    # elif opcao == 3:
                    #     print("===========EXTRATO===========\n")
                    #     vizualizar_extrato(saldo, numero_saques, extrato_deposito = extrato_deposito, extrato_saldo = extrato_saldo)

                    # else:
                    #     break 

            elif opcao_operacao == 2:
                self.criar_conta()

            elif opcao_cadastro == 3:
                print(self.cliente.contas)

            elif opcao_cadastro == 4:
                print("Obrigado por usar nosso serviço!!!")

    def fazer_cadastro(self):
        cpf = str(input('Qual seu CPF (apenas os números)?   '))

        if not self.verifica_CPF(cpf): 
            nome = input("Informe seu nome completo\n")
            
            dia = int(input("O dia do seu nascimento:  "))
            mes = int(input("O mês:  "))
            ano = int(input("Do ano:  "))
            data_nascimento = datetime(ano, mes, dia)
            
            print("Nos informe seu endereço para concluir o cadastro")
            logradouro = str(input("O logradouro:  "))
            numero_residencia = str(input("O nº da residência:  "))
            bairro = str(input("O bairro:  "))
            cidade = str(input("A cidade:  "))
            sigla_estado = str(input("A sigla do Estado:  "))
            endereco = logradouro+", "+numero_residencia+" - "+bairro+" - "+cidade+"/"+sigla_estado
            endereco = endereco
            
            print("Cadastrado!!!")
        
            senha = str(input("Crie uma senha:\n"))

            pessoa_fisica = PessoaFisica(
                endereco = endereco, 
                cpf = cpf, 
                data_nascimento = data_nascimento, 
                nome = nome, 
                senha = senha
            )
            return pessoa_fisica
        else:
            print("Você já está cadastrado!!!")

    def criar_conta(self):
        agencia = str(input('Qual a agência?\t'))

        limite_mudar = input('Seu limite pré-aprovado é de R$ 1000,00! Se gostaria de mudá-lo | Digite 1 |\t') or None
        if limite_mudar == '1':  
            limite = float(input('Qual o valor do limite que gostaria de ter?\t'))
        else:
            limite = 1000.0  

        limite_saques_mudar = input('Seu limite de saques pré-aprovado é de 3 por dia! Se gostaria de mudá-lo | Digite 1 |\t') or None
        if limite_saques_mudar == '1':  
            limite_saques = float(input('Qual o novo limite de saques que gostaria de ter?\t'))
        else:
            limite_saques = 3  

        saldo_inicial = input('Qual o seu saldo inicial? (Se não inserir nada ficará como 0)') or '0' 

        numero = len(self.cliente.contas)

        self.cliente.criar_conta(numero, agencia, limite, limite_saques, float(saldo_inicial))



    def verifica_CPF(self, CPF: str) -> bool: 
        for cliente in self.clientes:
            if cliente._cpf == CPF:
                return True
            
    def verifica_nome(self, nome: str, clientes: list):
        for cliente in clientes:
            if cliente._nome == nome:
                return True

            
    def autenticar(self):
        cpf = str(input("Insira o seu CPF (Apenas os números) "))
        senha = str(input("insira uma senha "))
        
        for cliente in self.clientes:
            if cliente._cpf == cpf:
                true_key = str(cliente.senha)

                if true_key == senha:
                    self.acesso = 1
                    self.cliente = cliente
                    return

                else:
                    print("Senha Incorreta!!\n")

    
        print("Usuário Incorreto ou não existe!!")
            

    def logar_conta(self):
        agencia = str(input("Insira a agência\t"))
        numero = int(input("O número da conta\t"))
        
        for conta in self.cliente.contas:
            if conta.agencia == agencia and conta.numero == numero:
                return conta
            
            else:
                print("Conta não existente!!\n")

        # if agencia in contas:
        #     true_key = int(usuarios.get(username).get("Senha"))
        #     print(true_key)

        #     if true_key == senha:
        #         Acesso_concedido = 1

        #     else:
        #         print("Senha Incorreta!!\n")

# def fazer_cadastro():
#     CPF = int(input("Qual o seu CPF (Apenas os números)?\n"))

#     if not verifica_CPF(CPF): 
#         valores = {}

#         name = input("Informe seu nome completo\n")
#         valores["Nome"] = name
        
#         dia = int(input("O dia do seu nascimento:  "))
#         mes = int(input("O mês:  "))
#         ano = int(input("Do ano:  "))
#         valores["Data de Nascimento"] = datetime(ano, mes, dia)
        
#         print("Nos informe seu endereço para concluir o cadastro")
#         logradouro = str(input("O logradouro:  "))
#         numero_residencia = str(input("O nº da residência:  "))
#         bairro = str(input("O bairro:  "))
#         cidade = str(input("A cidade:  "))
#         sigla_estado = str(input("A sigla do Estado:  "))
#         endereco = logradouro+", "+numero_residencia+" - "+bairro+" - "+cidade+"/"+sigla_estado
#         valores["Endereço"] = endereco
        
#         print("Cadastrado!!!")
      
#         senha = input("Crie uma senha:\n")
#         valores["Senha"] = senha
#         pessoa_fisica = PessoaFisica(**valores)
#         clientes.append(pessoa_fisica)
#     else:
#         print("Você já está cadastrado!!!")

#     return CPF

# def verifica_CPF(CPF: str) -> bool: 
#     for user in clientes:
#         if user._cpf == CPF:
#             return True

app = App()

app.main()