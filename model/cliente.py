from model.usuario import Usuario
from model.agendamento import Agendamento
class Cliente(Usuario):
    def __init__(self, name, phoneNumber, birthdayDate, cpf, email, usuario, senha):
        super().__init__(usuario, senha, name)
        self.phoneNumber = phoneNumber
        self.birthdayDate = birthdayDate
        self.cpf = cpf
        self.email = email
        self.agendamento = []

    # como chamar os metodos de agendamento aqui?

    
    def realizar_agendamento(self):
        agendamento = Agendamento(self)
        agendamento.realizar_agendamento()
        self.agendamento.append(agendamento)
        print("Agendamento realizado com sucesso!")