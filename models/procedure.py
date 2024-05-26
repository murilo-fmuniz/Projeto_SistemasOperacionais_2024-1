from models.processo import Processo

class Procedure:
    def __init__(self, n_process):
        self.processes = []
        self.average_response_time = 0
        self.current_process = None
        self.queue_counter = 0
        self.procedure_queue = []
        self.completed_processes = 0
        self.n_processes = n_process

    def adicionar_processo(self, processo):
        self.processes.append(processo)
        self.procedure_queue.append(processo)

    def calcular_tempos(self):
        pass

    def imprimirProcessos(self):
        for processo in self.processes:
            print(f"{self.__class__.__name__} =>Processo {processo.name}: {processo.arrival_time}")
