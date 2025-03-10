class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    def calculo_area(self):
        area = self.altura*self.altura
        print(f"A área do Retangulo é {area:.2f}")
    def calculo_perimetro(self):
        perimetro = (self.altura*2)+(self.largura*2)
        print(f"O perimetro é {perimetro:.2f}")
    
O_Retangulo = Retangulo(5, 9)
O_Retangulo.calculo_area()
O_Retangulo.calculo_perimetro()