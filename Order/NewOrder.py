# Trabalho 2 – Loja de Produtos Esportivos
# Disciplina: Redes
# David de Moura Marques
# 20172bsi0505
# 23/01/2022

class NewOrder: 
    def __init__(self, productName, quantity): 
        self.productName = productName
        self.quantity = int(quantity)

    def ToString(self):
        return "product:%s quantity:%s" % (self.productName, self.quantity)

    def __repr__(self):
        return "<product:%s quantity:%s>" % (self.productName, self.quantity)

    def __str__(self):
        return "product:%s quantity:%s" % (self.productName, self.quantity)
