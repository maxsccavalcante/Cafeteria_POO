class Cafeteira:
    """Criando a máquinha que faz o café"""
    def __init__(self):
        self.recursos = {
            "agua": 300,
            "leite": 200,
            "cafe": 100,
        }

    def resumo(self):
        """Printa um resumo dos recursos da máquina."""
        print(f"Água: {self.recursos['agua']}ml")
        print(f"Leite: {self.recursos['leite']}ml")
        print(f"Café: {self.recursos['cafe']}g")

    def se_os_recursos_sao_suficientes(self, bebida):
        """Retorna True se o pedido consegue ser feito, False se os recursos forem insuficientes."""
        pode_fazer = True
        for item in bebida.ingredientes:
            if bebida.ingredientes[item] > self.recursos[item]:
                print(f"Desculpe, não temos {item} o suficiente.")
                pode_fazer = False
        return pode_fazer

    def fazer_cafe(self, pedido):
        """Deduz os ingredientes necessários dos recursos."""
        for item in pedido.ingredientes:
            self.recursos[item] -= pedido.ingredientes[item]
        print(f"Aqui está o seu {pedido.nome} ☕️. Aproveite!")
