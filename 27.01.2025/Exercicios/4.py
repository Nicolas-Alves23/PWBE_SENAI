class Aluno:
    def __init__(self, nome, matricula, notas):
        self.nome = nome
        self.matricula = matricula
        self.notas = notas
    def situacao(self):
        n1 = float(input("Me passe uma nota = "))
        n2 = float(input("Me passe uma nota = "))
        n3 = float(input("Me passe uma nota = "))
        n4 = float(input("Me passe uma nota = "))
        n5 = float(input("Me passe uma nota = "))

        media = (n1 + n2 + n3 + n4 + n5) / 5
        if media >= 5:
            print (f"{self.nome} está Aprovado")    
        elif media >= 2.5 and media < 5:
            print(f"{self.nome} está Recuperação")
        elif media < 2.5:
            print(f"{self.nome} está Reprovado")
aluno = Aluno("Nicolas", 12345, "5 notas em banco")
aluno.situacao()
