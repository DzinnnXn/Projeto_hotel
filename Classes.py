Clientes = []

class Hotel:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.aps = []

    def cadastrar_quarto(self, nome, cpf):
        cadastrar = {'Nome': nome, 'Cpf': cpf}
        Clientes.append(cadastrar)
        print(f"Cadastro de {nome} feito com sucesso!")

    def ad_apartamento(self, ape):
        self.aps.append(ape)

class Quartos:
    def __init__(self, numero, capacidade, valor):
        self.numero = numero
        self.capacidade = capacidade
        self.valor = valor

    def detalhes_quarto(self):
        return f"Quarto {self.numero} - Capacidade: {self.capacidade} pessoas, Preço: R${self.valor} por dia"

class Ap_simples(Quartos):
    def __init__(self, numero):
        super().__init__(numero, capacidade=1, preco=130)

    def detalhes():
        print("Apartamento Simples")
        print("1 cama de solteiro, 1 banheiro, frigobar, internet e TV")

class Ap_simples_casal(Quartos):
    def __init__(self, numero):
        super().__init__(numero, capacidade=2, preco=150)
   
    def detalhes():
        print("Apartamento Simples Casal")
        print("1 cama de casal, 1 banheiro, frigobar, internet e TV")

class Ap_duplo(Quartos):
    def __init__(self, numero):
        super().__init__(numero, capacidade=2, preco=180)

    def detalhes():
        print("Apartamento Duplo")
        print("2 camas de solteiro, 1 banheiro, frigobar, internet e TV")

class Ap_duplo_casal(Quartos):
    def __init__(self, numero):
        super().__init__(numero, capacidade=2, preco=200)

    def detalhes():
        print("Apartamento Duplo Casal")
        print("1 cama de casal (Queen Size), 1 banheiro,  frigobar, internet, TV e Ar Condicionado")

class Ap_luxo(Quartos):
    def __init__(self, numero):
        super().__init__(numero, capacidade=4, preco=250)

    def detalhes():
        print("Apartamento Luxo")
        print("2 camas de casal(Queen Size), 2 banheiro, 1 geladeira, 1 suíte, Ar Condicionado, Cozinha, internet e TV")

class Ap_master(Quartos):
    def __init__(self, numero):
        super().__init__(numero, capacidade=4, preco=300)

    def detalhes():
        print("Apartamento Master")
        print("2 camas de casal (King size), 2 banheiros, 1 suíte, 1 hidromassagem, 1 geladeira, cozinha, internet, Ar Condicionado e TV")