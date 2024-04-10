class Usuario:
    def __init__(self, name, user, password):
        self.name = name
        self.user = user
        self.password = password


class Usuario:
    def __init__(self, name, user, password):
        self.name = name
        self.user = user
        self.password = password
        self.logged_in = False

    @classmethod
    def cadastrar(cls, name, user, password):
        return cls(name, user, password)

    def login(self, user, password):
        if self.user == user and self.password == password:
            self.logged_in = True
            return True
        else:
            return False


