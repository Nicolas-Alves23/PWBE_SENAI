class Livro:
    def __init__(self, titulo, autor, n_pag):
        self.titulo = titulo
        self.autor = autor
        self.n_pag = n_pag
        self.emprestar = True
    def emprestarr(self):
            self.emprestar = False
            print("livro pego emprestado")

    def devolver(self):
            self.emprestar =True
            print("livro devolvido ")

    def verificar(self):
        if self.emprestar == True:
            print("Livro pode ser emprestado")
        else:
            print("livro já esta emprestado")
    
livro = Livro("Nicolas e suas aventuras", "Nicolas", 678)
while True:
    oq_fazer = int(input("Oq você quer fazer \n 1 = Pegar emprestado \n 2 = verificar se da para pegar emprestado \n 3 = devolver \n 4 = sair\n"))
    if oq_fazer == 1:
        livro.emprestarr()
    elif oq_fazer ==2:
        livro.verificar()
    elif oq_fazer == 3:
        livro.devolver()
    elif oq_fazer == 4:
         break