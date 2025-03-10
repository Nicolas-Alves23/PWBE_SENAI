class Paciente:
    def __init__(self, nome, idade, historico):
        self.nome = nome
        self.idade = idade
        self.historico = historico
        
    def nova_cosulta(self):
        msg = '''
            Olá Bem vindo ao hospital Marinho bom demais
                Temos algumas consultas que podem
                        ser marcadas:


                        1- Clinico Geral
                        2- Cardiologia
                        3- Ginecologia
                        4- Ortopedia 
                        5- Pediatria

                '''
        que_consulta = int(input(msg))
        if que_consulta == 1:
            print("A consulta foi marcada, Clinico Geral")
            self.historico += " Clinico Geral,"
        if que_consulta == 2:
            print("A consulta foi marcada, Cardiologia")
            self.historico += " Cardiologia,"
        if que_consulta == 3:
            print("A consulta foi marcada, Ginecologia")
            self.historico += " Ginecologia,"
        if que_consulta == 4:
            print("A consulta foi marcada, Ortopedia")
            self.historico += " Ortopedia,"
        if que_consulta == 5:
            print("A consulta foi marcada, Pediatria")
            self.historico += " Pediatria,"

    def mostra_historico(self):
        print(f"O HISTORICO\n{self.historico}")


hospital = Paciente("Nicolas", 16, "Ortopedia,")
hospital.nova_cosulta()
hospital.mostra_historico()