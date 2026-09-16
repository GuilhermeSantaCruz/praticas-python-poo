class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"O livro {self.titulo}, do autor {self.autor}, tem {self.paginas} páginas."    


l1 = Livro("O poder do silêncio", "Eckhart Tolle", 112)    
print(l1)

l2 = Livro("A arte da guerra", "Sun Tzu", 160)
print(l2)