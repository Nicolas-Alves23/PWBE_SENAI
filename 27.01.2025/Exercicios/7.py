import math
class Triangulo:
    def __init__(self, ld1, ld2, ld3):
        self.ld1 = ld1
        self.ld2 = ld2
        self.ld3 = ld3
    
    def tringulo_valido(self):
        if self.ld1 + self.ld2 > self.ld3:
            return True
        if self.ld3 + self.ld2 > self.ld1:
            return True
        if self.ld2 + self.ld3 > self.ld2:
            return True
        else:
            return False
        
    def area_do_triangulo(self):
        semi_perimetro = (self.ld1 + self.ld2 + self.ld3) / 2
        raiz_quadrada = semi_perimetro * (semi_perimetro - self.ld1) * (semi_perimetro - self.ld2) * (semi_perimetro * self.ld3)
        resultado = math.sqrt(raiz_quadrada)
        print(f"{resultado:.2f}")

triangulo = Triangulo(5, 5, 5 )
triangulo.tringulo_valido()
triangulo.area_do_triangulo()