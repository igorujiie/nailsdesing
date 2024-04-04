from model.cliente import Cliente
from model.servico import Servico
from datetime import date

class Agendamento:
    def __init__(self, data:date ,client, service:list = None, pacote:list = None):
        self.client = client
        self.service = service
        self.data = date
        self.pacote = pacote
