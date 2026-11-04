from abc import ABC, abstractclassmethod,
abstratctproperty
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, Transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome=nome
        self.data_nascimeno=data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self_saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

        @classmethod
        def nova_conta(cls, cliente, numero):
            return cls(numero,cliente)

        @property
        def saldo(self):
            return self.self_saldo
        
        @property
        def numero(self):
            return self._numero
        
        @property
        def agencia(self):
            return self.agencia
        
        @property
        def cliente(self):
            return self.cliente
        
        @property
        def historico(self):
            return self.historico
        

        def sacar(self, valor):
            saldo = self.saldo
            excedeu_saldo = valor > saldo

            if excedeu_saldo:
                print("\n @@@ Operação Falhou! Você não tem saldo suficiente. @@@")

            elif valor > 0:
                self.saldo -= valor
                print("\n === Saque Realizado com Sucesso! ===")
            
            else:
                print("\n@@@ Operação Falhou! O valor é informado é inválido! @@@")
            
            return False
        
        def depositar(self, valor):
            if valor > 0:
                self._saldo += valor
                print("\n === Depósito realizado com sucesso! ===")
            else:
                print("\n @@@ Operação falhou! O valor informado é inválido. @@@")
            
            return True
    
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero,cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"]== saque.__name__])
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n @@@ Operação Falhou! O valor do Saque Excede o limite! @@@")
        
        elif excedeu_saques:
            print("\n @@@ Operação Falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""
        Agência: \t{self.agencia}
        C/C:\t\t{self.numero}
        Titular:\t{self.cliente.nome}
"""

class Historico:


class Transacao(ABC):

class saque(Transacao):

class Deposito(Transacao):

