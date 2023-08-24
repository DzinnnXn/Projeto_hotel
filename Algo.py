import os 
from Classes import *

def main():
    s = 0
    while s == 0:
        print("1- Cadastrar ")
        print("2- Escolher Quarto ")
        print("3- Sair")
        menu = int(input("Escolha: "))
        match menu:
            case 1:
                os.system("cls")
                print("Cadastrar \n")
                nome = input("Digite seu nome: ")
                cpf = int(input("Digite o seu cpf: "))
                cads = Hotel(nome, cpf)
                cads.cadastrar_quarto(nome, cpf)
                os.system("pause")
                os.system("cls")
                main()

            case 2:
                os.system("cls")
                print("Quartos")
                aps = Quartos()
                aps.detalhes_quarto()

            case 3:
                break

            case _:
                print("Opção Inválida")