class ContaBancaria:
    def __init__(self, numero_da_conta, nome, saldo):
        self.numero = numero_da_conta
        self.titular = nome
        self.saldo = saldo
    def saque(self):
        vc_quer_sacar = int(input("Você quer sacar quantos reais ? \n"))
        self.saldo -= vc_quer_sacar
        print(f"R${self.saldo}")
    def depositar(self):
        vc_quer_depositar = int(input("Você quer depositar quantos reais ? \n"))
        self.saldo += vc_quer_depositar
        print(f"R${self.saldo}")
        
conta = ContaBancaria(12345, "Nicolas", 6500.00)
print("Bem vindo ao Banco qui gostozin")
escolha= int(input("O que vc deseja fazer \n 1-Sacar \n 2-Depositar"))
if escolha == 1:
    conta.saque()
elif escolha == 2:
    conta.depositar()
else:
    print("Erro de entrada")