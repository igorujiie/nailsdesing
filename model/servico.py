class Servico:
    def __init__(self, name, durationTime, price):
        self.name = name
        self.durationTime = durationTime
        self.price = price

    # o que significa essas anotacoes?
    

    @classmethod
    def criar_servico(cls, lista_servicos):
        name = input("Digite o nome do serviço: ")
        durationTime = int(input("Digite a duração do serviço em horas: "))
        price = float(input("Digite o preço do serviço: "))

        for servico in lista_servicos:
            if servico.name == name:
                print("O serviço já está cadastrado.")
                return
        novo_servico = cls(name, durationTime, price)
        lista_servicos.append(novo_servico)
        print("Serviço cadastrado com sucesso!")

    def atualizar_dados(self):
        self.name = input("Novo nome do serviço (ou deixe em branco para manter o atual): ").strip() or self.name
        self.durationTime = int(input("Nova duração do serviço em horas (ou deixe em branco para manter a atual): ").strip() or self.durationTime)
        self.price = float(input("Novo preço do serviço (ou deixe em branco para manter o atual): ").strip() or self.price)
        print("Dados do serviço alterados com sucesso!")

    @staticmethod
    def excluir_servico(lista_servicos):
        name = input("Digite o nome do serviço que deseja excluir: ")
        for servico in lista_servicos:
            if servico.name == name:
                lista_servicos.remove(servico)
                print("Serviço excluído com sucesso!")
                return
        print("Serviço não encontrado.")
