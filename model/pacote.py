from decimal import Decimal

class Pacote:
    def __init__(self, services: list, price: Decimal, intervalo: int, qtdDevezes: int, periodo: int):
        self.services = services
        self.price = price
        self.intervalo = intervalo
        self.qtdDevezes = qtdDevezes
        self.periodo = periodo

    

    def adicionar_servico(self, service):
        self.services.append(service)

    def calcular_duracao_total(self):
        duracao_total = sum(service.durationTime for service in self.services)
        return duracao_total

    def remover_servico(self, service_name):
        for service in self.services:
            if service.name == service_name:
                self.services.remove(service)
                print(f"Serviço '{service_name}' removido do pacote com sucesso!")
                return
        print(f"Serviço '{service_name}' não encontrado no pacote.")
