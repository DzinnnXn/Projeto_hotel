import os
from Classes import *
def main():
    hotel = Hotel("Nome do Hotel")
    s = 0
    while s == 0:
        print("\nMenu:")
        print("1. Cadastrar Quarto")
        print("2. Detalhes dos Quartos")
        print("3. Sair")

        escolha = input("Escolha uma opção: ")
        try:
            
            if escolha == "1":
                numero_quarto = input("Digite o número do quarto: ")
                tipo_quarto = input("Escolha o tipo de quarto \n1- simples \n2- simples casal \n3- duplo \n4- duplo casal \n5- luxo \n6- master: ")
                
                if tipo_quarto == 1:
                    quarto = Ap_simples(numero_quarto)
                    hotel.ad_apartamento(quarto)
                    print(f"Quarto {quarto.numero} cadastrado com sucesso!")
                    
                elif tipo_quarto == 2:
                    quarto = Ap_simples_casal(numero_quarto)
                    hotel.ad_apartamento(quarto)
                    print(f"Quarto {quarto.numero} cadastrado com sucesso!")
                    
                elif tipo_quarto == 3:
                    quarto = Ap_duplo(numero_quarto)
                    hotel.ad_apartamento(quarto)
                    print(f"Quarto {quarto.numero} cadastrado com sucesso!")
                    
                elif tipo_quarto == 4:
                    quarto = Ap_duplo_casal(numero_quarto)
                    hotel.ad_apartamento(quarto)
                    print(f"Quarto {quarto.numero} cadastrado com sucesso!")
                    
                elif tipo_quarto == 5:
                    quarto = Ap_luxo(numero_quarto)
                    hotel.ad_apartamento(quarto)
                    print(f"Quarto {quarto.numero} cadastrado com sucesso!")
                
                elif tipo_quarto == 6:
                    quarto = Ap_master(numero_quarto)
                    hotel.ad_apartamento(quarto)
                    print(f"Quarto {quarto.numero} cadastrado com sucesso!")
                    
                else:
                    print("Tipo de quarto inválido.")
                    continue
        
                
            elif escolha == "2":
                print("Detalhes dos Quartos")
                numero = int(input("Digite o numero do quarto: "))
                obt_detalhes_simples = Ap_simples
                obt_detalhes_simples.detalhes_simples(numero)
                #//
                obt_detalhes_simples_casal = Ap_simples_casal
                obt_detalhes_simples_casal.detalhes_simples_casal(numero)
                #//
                obt_detalhes_duplo = Ap_duplo
                obt_detalhes_duplo.detalhes_duplo(numero)
                #//
                obt_detalhes_duplo_casal = Ap_duplo_casal
                obt_detalhes_duplo_casal.detalhes_duplo_casal(numero)
                #//
                obt_detalhes_luxo = Ap_luxo
                obt_detalhes_luxo.detalhes_luxo(numero)
                #//
                obt_detalhes_master = Ap_master
                obt_detalhes_master.detalhes_master(numero)
                os.system("pause")
                os.system("cls")
                    
            elif escolha == "3":
                print("Saindo do programa.")
                break
            else:
                print("Opção inválida. Escolha novamente.")
        
        except Exception as erro:
            print(f"Erro encontrado", erro)


