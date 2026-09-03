class CaixaEletronico:

    MOEDA = "R$"

    VALORES_MOEDAS = {
        "25": 0.25,
        "10": 0.10,
        "5": 0.05,
        "1": 0.01
    }

    def __init__(self):
        self.lucro = 0
        self.dinheiro_recebido = 0

    def resumo(self):
        """Mostrando o lucro atual"""
        print(f"Dinheiro: {self.MOEDA}{self.lucro}")

    def processando_moedas(self):
        """Retorna o total de dinheiro com base nas moedas que foram inseridas."""
        print("Insira moedas.")
        for moeda in self.VALORES_MOEDAS:
            self.dinheiro_recebido += int(input(f"Quantas moedas de {moeda} centavo(s)?: ")) * self.VALORES_MOEDAS[moeda]
        return self.dinheiro_recebido

    def efetuar_pagamento(self, custo):
        """Retorna True se o pagamento tiver sido aceito, ou False se tiver sido insuficiente."""
        self.processando_moedas()
        if self.dinheiro_recebido >= custo:
            troco = round(self.dinheiro_recebido - custo, 2)
            print(f"Aqui tem {self.MOEDA}{troco} de troco.")
            self.lucro += custo
            self.dinheiro_recebido = 0
            return True
        else:
            print("Desculpe, não há dinheiro suficiente aqui. Dinheiro reembolsado.")
            self.dinheiro_recebido = 0
            return False