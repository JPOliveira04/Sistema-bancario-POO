class Cliente:
    def __init__(self, nome):
        self.nome = nome


class ContaBancaria:
    def __init__(self, cliente, limite=500, limite_saques=3):
        self.cliente = cliente
        self.saldo = 0
        self.limite = limite
        self.limite_saques = limite_saques
        self.numero_saques = 0
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido para saque.")
        elif valor > self.saldo:
            print("Saldo insuficiente.")
        elif valor > self.limite:
            print(f"Saque superior ao limite permitido de R$ {self.limite:.2f}.")
        elif self.numero_saques >= self.limite_saques:
            print("Número máximo de saques diários atingido.")
        else:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            self.numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    def mostrar_extrato(self):
        print("\n--- Extrato ---")
        if not self.extrato:
            print("Nenhuma movimentação realizada.")
        else:
            for mov in self.extrato:
                print(mov)
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print("----------------\n")


def menu():
    nome = input("Digite seu nome: ")
    cliente = Cliente(nome)
    conta = ContaBancaria(cliente)

    while True:
        print(f"\n=== Sistema Bancário === (Cliente: {cliente.nome})")
        print("[1] Depositar")
        print("[2] Sacar")
        print("[3] Extrato")
        print("[4] Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: R$ "))
            conta.depositar(valor)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: R$ "))
            conta.sacar(valor)

        elif opcao == "3":
            conta.mostrar_extrato()

        elif opcao == "4":
            print("Obrigado por utilizar o sistema. Até logo!")
            break

        else:
            print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    menu()
