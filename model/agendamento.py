from model.cliente import Cliente
from model.servico import Servico
from datetime import date

from datetime import datetime

class Agendamento:
    def __init__(self, client, service: list = None, pacote: list = None):
        self.client = client
        self.service = service
        self.data = None
        self.pacote = pacote

    def realizar_agendamento(self):
        if self.client is None:
            print("Erro: Cliente não especificado.")
            return

        if self.service is None and self.pacote is None:
            print("Erro: Nenhum serviço ou pacote especificado.")
            return

        while True:
            try:
                data_input = input("Digite a data do agendamento (formato DD-MM-YYYY): ")
                self.data = datetime.strptime(data_input, "%d-%m-%Y").date()
                break
            except ValueError:
                print("Erro: Formato de data inválido. Use o formato DD-MM-YYYY.")

        print("Agendamento realizado com sucesso!")

