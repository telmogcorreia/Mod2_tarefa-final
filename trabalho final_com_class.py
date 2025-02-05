# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 20:21:06 2025

@author: telmo
"""

from abc import ABC, abstractmethod

class GastoBase(ABC):  # Classe Abstrata vazia
    pass


class Gasto(GastoBase):   # Classe derivada
    def __init__(self):
        self.total_gastos = 0  # Total de gastos a zero, depois soma a quando cada gasto é inserido
        open("dinheiro.txt", "w").close() # Abre e limpa o ficheiro 
                                          # "dinheiro.txt"
                                          
          


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
        gasto = float(input("Digite um gasto (ou '0' para finalizar): "))
        if gasto == 0:
            break # Quando digitar "0" Para o programa
        elif gasto < 0:
            print("Por favor, insira um valor positivo.") # Quando o numero é menor que 0 continua dentro do loop
        else:
            categoria = input("Digite a categoria do gasto: ") # Quando o valor é maior que zero, pergunta qual é a categoria do gasto
            gasto_manager.registrar_gasto(gasto, categoria) # Chama o metodo registar_gasto para registar o gasto e a categoria.
    except ValueError:  # Caso não digite um numero aparece está mensagem
        print("Por favor, insira um número válido.")

with open('dinheiro.txt', 'a') as f:  # Abre o ficheiro para escrever o total
    f.write(f"\nTotal dos gastos: €{gasto_manager.total_gastos:.2f}\n") # Escreve o total no ficheiro
print(f"\nTotal dos gastos: {gasto_manager.total_gastos:.2f}€") # Escreve o total na consola do utilizador
