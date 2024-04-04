import decimal
from model.servico import Servico

class Pacote:
    def __init__(self, service: list, price: decimal, intervalo:int, qtdDevezes:int, periodo:int):
        self.service = service
        self.price = price
        self.intervalo = intervalo
        self.qtdDevezes = qtdDevezes
        self.periodo = periodo
