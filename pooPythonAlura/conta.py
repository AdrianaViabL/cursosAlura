class Conta:

    def __init__(self, numero, titular, saldo, limite, codigo_banco='001'):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = codigo_banco

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular}')

    def __pode_sacar(self, valor):
        return valor <= (self.__saldo + self.__limite)

    def sacar(self, valor):
        if self.__pode_sacar(valor=valor):
            self.__saldo -= valor
            return 'saque efetuado'
        return 'saldo insuficiente para saque'

    def depositar(self, valor):
        self.__saldo += valor

    def transferir(self, valor, destino):  # deixando de forma implicita que a conta de origem é
        # a ja instanciada dentro do self
        self.sacar(valor=valor)
        destino.depositar(valor=valor)

    def get_saldo(self):  # forma mais simples de acessar os dados de uma variavel encapsulada
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property  # transformando esse metodo em uma propriedade da variavel limite, podendo ser acessado sem precisar do
    # () no final
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor):
        self.__limite = valor

    @staticmethod  # transformando em um metodo estatico, ou seja, pode ser acessado sem a criação do objeto Conta
    def codigo_banco():
        return '001'
