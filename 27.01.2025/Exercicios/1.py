class Circulo:
    def __init__(self, raio):
        self.raio = raio
        self.pi = 3.14159
    def calculo_area(self):
        area = self.pi*(self.raio**2)
        print(f"A área do circulo é {area:.2f}")
    def calculo_perimetro(self):
        perimetro = 2*self.pi*self.raio
        print(f"O perimetro é {perimetro:.2f}")
    
O_circulo = Circulo(5)
O_circulo.calculo_area()
O_circulo.calculo_perimetro()