from models.processo import Processo

class Procedure:
    def __init__(self):
        self.processes = []
        self.average_response_time = 0

    def adicionar_processo(self, processo):
        self.processes.append(processo)

    def calcular_tempos(self):
        pass

    def imprimirProcessos(self):
        for processo in self.processes:
            print(f"{self.__class__.__name__} =>Processo {processo.name}: {processo.arrival_time}")
