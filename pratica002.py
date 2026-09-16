class Produto:
    def __init__(self, nome, preco = 0):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"O produto {self.nome} com o valor de R${self.preco:,.2f} foi criado com sucesso."

p1 = Produto("computador", 3500)
print(p1)

p2 = Produto("Impressora", 1200)
print(p2)

p3 = Produto("Xadrez", 120)
print(p3)

p4 = Produto("Casa")
print(p4)