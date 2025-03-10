class Produto:
    def __init__(self, nome, preco, quantidade_estoque):
        self.nome = nome
        self.preco = preco
        self.qtd = quantidade_estoque
        self.lucro_possivel = 0
        self.preco_em_estoque()
    def preco_em_estoque(self):
        self.lucro_possivel = self.preco * self.qtd

    def __str__(self):
        return f"O {self.nome} do valor unitario de R${self.preco}, que temos {self.qtd} em estoque. \n R${self.lucro_possivel}"
    
prod = Produto("Nescau", 8.60, 10)
print(prod)