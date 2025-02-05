# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 20:04:25 2025

@author: telmo
"""

from abc import ABC, abstractmethod

class GastoBase(ABC):  # Classe Abstrata vazia
    pass


class Gasto(GastoBase):   # Classe Derivada
    def __init__(self):
        self.total_gastos = 0  # Total de gastos a zero, depois soma a quando cada gasto é inserido
        with open("dinheiro.txt", "w") as f: # Abre e escreve o cabeçalho do fichiro "dinheiro.txt"
            f.write("Aqui estão os seus gastos e categorias.\n")
            f.write("\n")
            f.write("\n")
                    
                                                  
    def registrar_gasto(self, valor, categoria):
        self.total_gastos += valor # Soma gasto ao total de gastos
        with open("dinheiro.txt", "a") as f: # Abre o ficheiro e escreve os novos gastos e categorias
            f.write(f"Gasto: {valor:.2f}€ - Categoria: {categoria}\n") # Escreve 


# --------    Programa principal     ------

gasto_manager = Gasto() 

print("Neste documento pode apontar os seus gastos\ne as categorias.")
print("\n")
print("Vamos a isso:")
print("\n")

while True: 
    try:
        valor = float(input("Digite um gasto (ou '0' para finalizar): "))
        if valor == 0:
            break # Quando digitar "0" Pará o programa
        elif valor < 0:
            print("Por favor, insira um valor positivo.") # Quando o numero é menor que '0' continua dentro do loop
        else:
            categoria = input("Digite a categoria do gasto: ") # Quando o valor é maior que zero, pergunta qual é a categoria do gasto
            gasto_manager.registrar_gasto(valor, categoria) # Chama o metodo registar_gasto para registar o gasto e a categoria.
    except ValueError:  # Caso não digite um numero aparece está mensagem
        print("Por favor, insira um número válido.")

with open('dinheiro.txt', 'a') as f:  # Abre o ficheiro para escrever o total
    f.write(f"\nTotal dos gastos: {gasto_manager.total_gastos:.2f}€") # Escreve o total no ficheiro
print(f"\nTotal dos gastos: {gasto_manager.total_gastos:.2f}€") # Escreve o total na consola do utilizador
