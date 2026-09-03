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
        # Condição de desligamento: encerra o loop principal
        ligada = False

    elif opcao == "resumo":
        # Condição de relatório: mostra o estado atual da máquina, sem vender nada
        maquina_de_cafe.resumo()
        caixa.resumo()

    else:
        # Passo 1: a bebida pedida existe no menu?
        bebida = menu.procurando_bebida(opcao)

        if bebida is not None:
            # Passo 2: há ingredientes suficientes para essa bebida?
            if maquina_de_cafe.se_os_recursos_sao_suficientes(bebida):

                # Passo 3: o pagamento foi suficiente?
                if caixa.efetuar_pagamento(bebida.custo):

                    # Passo 4: só produz o café se passou pelos 3 passos anteriores
                    maquina_de_cafe.fazer_cafe(bebida)
