class Hotel:
    def __init__(self, nome):
        self.nome = nome
        self.aps = []

    def ad_apartamento(self, ape):
        self.aps.append(ape)

class Quartos:
    def __init__(self, numero, capacidade, preco):
        self.numero = numero
        self.capacidade = capacidade
        self.preco = preco
        self.esta_reservado = False

    def esta_disponivel(self):
        return not self.esta_reservado

    def obter_detalhes_quarto(self):
        return f"Apartamento Número{self.numero} - Capacidade: {self.capacidade} pessoas, Preço: {self.preco} por noite"

class Ap_simples(Quartos):
    def __init__(self, numero):
        super().__init__(numero, capacidade=1, preco=130)

    def detalhes_simples(self):
        print("Apartamento Simples\n1 cama de solteiro, 1 banheiro, frigobar, internet e TV \n")

class Ap_simples_casal(Quartos):
    def __init__(self, numero):
        super().__init__(numero, capacidade=2, preco=150)
   
    def detalhes_simples_casal(self):
        print("Apartamento Simples Casal\n1 cama de casal, 1 banheiro, frigobar, internet e TV\n")

class Ap_duplo(Quartos):
    def __init__(self, numero):
        super().__init__(numero, capacidade=2, preco=180)

    def detalhes_duplo(self):
        print("Apartamento Duplo\n2 camas de solteiro, 1 banheiro, frigobar, internet e TV\n")

class Ap_duplo_casal(Quartos):
    def __init__(self, numero):
        super().__init__(numero, capacidade=2, preco=200)

    def detalhes_duplo_casal(self):
        print("Apartamento Duplo Casal\n1 cama de casal (Queen Size), 1 banheiro,  frigobar, internet, TV e Ar Condicionado\n")

class Ap_luxo(Quartos):
    def __init__(self, numero):
        super().__init__(numero, capacidade=4, preco=250)

    def detalhes_luxo(self):
        print("Apartamento Luxo\n2 camas de casal(Queen Size), 2 banheiro, 1 geladeira, 1 suíte, Ar Condicionado, Cozinha, internet e TV\n")

class Ap_master(Quartos):
    def __init__(self, numero):
        super().__init__(numero, capacidade=4, preco=300)

    def detalhes_master(self):
        print("Apartamento Master\n2 camas de casal (King size), 2 banheiros, 1 suíte, 1 hidromassagem, 1 geladeira, cozinha, internet, Ar Condicionado e TV\n")
