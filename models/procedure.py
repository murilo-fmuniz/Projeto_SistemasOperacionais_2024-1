from models.processo import Processo

class Procedure:
    def __init__(self):
        self.processes = []
        self.average_response_time = 0

    def adicionar_processo(self, processo):
        self.processes.append(processo)

    def calcular_tempos(self):
        total_response_time = 0
        current_time = 0
        
        for processo in sorted(self.processes, key=lambda p: p.arrival_time):
            processo.waiting_time = max(0, current_time - processo.arrival_time)
            processo.response_time = processo.waiting_time + processo.execution_time_needed
            total_response_time += processo.response_time
            current_time += processo.execution_time_needed

        self.average_response_time = total_response_time / len(self.processes) if self.processes else 0
