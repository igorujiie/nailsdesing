from model.usuario import Usuario

class Cliente(Usuario):
    def __init__(self, name, phoneNumber, birthdayDate, cpf, email,usuario,senha):
        super().__init__(usuario,senha,name)
        self.phoneNumber = phoneNumber
        self.birthdayDate = birthdayDate
        self.cpf = cpf
        self.email = email
