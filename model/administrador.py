from model.usuario import Usuario

class administrador(Usuario):
    def __init__(self, usuario, senha,name):
        super().__init__(usuario, senha,name)
        

    def subscribe(self):
        pass


    def seeAppointments(self):
        pass

    def doAppointments(self):
        pass

    def excludeAppointments(self):
        pass

    def includeOfficeHours(self):
        pass

    def subscribeClient(self):
        pass

    def subscribeService(self):
        pass

    def subscribePackage(self):
        pass

    def excludeClient(self):
        pass

    def excludeService(self):
        pass

    def excludePackage(self):
        pass

    def includeTimeBlock(self):
        pass