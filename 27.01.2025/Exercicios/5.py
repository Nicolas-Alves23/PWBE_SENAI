class Funcionario:
    def __init__(self,  nome, salario, cargo):
        self.nome = nome    
        self.salario_bruto = salario
        self.cargo = cargo
    def salario_liqui(self):
        desconto =  self.salario_bruto / 25
        beneficio =  self.salario_bruto / 95
        final_salario =  beneficio+(self.salario_bruto - desconto)
        print(f"O salário final é R${final_salario:.2f}")
funcio = Funcionario("Nicolas", 5000.00, "Gerente de TI")
funcio.salario_liqui()