from menu import Menu
from coffee_maker import Cafeteira
from money_machine import CaixaEletronico

# Instâncias das classes
menu = Menu()
caixa = CaixaEletronico()
maquina_de_cafe = Cafeteira()

ligada = True

while ligada:
    opcao = input(f"O que você gostaria? ({menu.pegando_bebidas()}): ").lower()

    if opcao == "off":
        ligada = False

    elif opcao == "resumo":
        maquina_de_cafe.resumo()
        caixa.resumo()

    else:
        bebida = menu.procurando_bebida(opcao)

        if bebida is not None:
            if maquina_de_cafe.se_os_recursos_sao_suficientes(bebida):
                if caixa.efetuar_pagamento(bebida.custo):
                    maquina_de_cafe.fazer_cafe(bebida)