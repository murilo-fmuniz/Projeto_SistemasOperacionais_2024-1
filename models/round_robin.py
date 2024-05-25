from models.procedure import Procedure

class RoundRobin(Procedure):
    def __init__(self, quantum):
        super().__init__()
        self.quantum = quantum

    def executar(self):
        current_time = 0
        queue = self.processes.copy()
        remaining_times = {p: p.execution_time_needed for p in queue}

        while queue:
            processo = queue.pop(0)
            if remaining_times[processo] > self.quantum:
                remaining_times[processo] -= self.quantum
                current_time += self.quantum
                queue.append(processo)
            else:
                current_time += remaining_times[processo]
                processo.execution_time_needed = remaining_times[processo]
                processo.response_time = current_time - processo.arrival_time
                processo.waiting_time = processo.response_time - processo.execution_time_needed

        self.average_response_time = sum(p.response_time for p in self.processes) / len(self.processes)
