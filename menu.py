class ItemMenu:
    """Criando cada item disponível no menu."""
    def __init__(self, nome, agua, leite, cafe, custo):
        self.nome = nome
        self.custo = custo
        self.ingredientes = {
            "agua": agua,
            "leite": leite,
            "cafe": cafe
        }


class Menu:
    """Criando o menu com as bebidas."""
    def __init__(self):
        self.menu = [
            ItemMenu(nome="latte", agua=200, leite=150, cafe=24, custo=2.5),
            ItemMenu(nome="espresso", agua=50, leite=0, cafe=18, custo=1.5),
            ItemMenu(nome="cappuccino", agua=250, leite=50, cafe=24, custo=3),
        ]

    def pegando_bebidas(self):
        """Retorna o nome de todos os itens disponíveis no menu."""
        opcoes = ""
        for item in self.menu:
            opcoes += f"{item.nome}/"
        return opcoes

    def procurando_bebida(self, nome_pedido):
        """Procura no menu uma bebida específica pelo nome. Retorna a bebida caso ela exista, caso contrário, retorna 'None'"""
        for item in self.menu:
            if item.nome == nome_pedido:
                return item
        print("Desculpe, esse item não está disponível.")