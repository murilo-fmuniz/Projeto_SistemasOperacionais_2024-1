from models.procedure import Procedure
from models.processo import Processo

class SJFPreemptivo(Procedure):
    def executar(self):
        
        while self.completed_processes < self.n_processes:
            #print(f'execucao: {self.queue_counter}')
            self.procedure_queue.sort(key=lambda p: p.execution_needed)
            
            if self.procedure_queue[0].execution_needed != 0:
                self.procedure_queue[0].execution_needed -=1
            
            print(f'processo em execucao: {self.procedure_queue[0].name} {self.procedure_queue[0].execution_needed}')
            if self.procedure_queue[0].execution_needed == 0:
                nome = self.procedure_queue[0].name
                indice = self.encontrar_indice_por_id(name = nome)

                self.processes[indice].completed_time = self.queue_counter
                self.processes[indice].response_time = self.queue_counter - self.procedure_queue[0].arrival_time

                print(f'{self.processes[indice].name} wt: {self.processes[indice].waiting_time} rt: {self.processes[indice].response_time}')
                
                self.procedure_queue.pop(0)

                self.procedure_queue.sort(key=lambda p: p.execution_needed)

                self.completed_processes += 1

            for process in self.procedure_queue[1:]:
                nome = process.name
                indice = self.encontrar_indice_por_id(name=nome)
                self.processes[indice].waiting_time += 1
        
            self.queue_counter += 1

    def calcular_tempos(self):
        total_waiting_time = sum(p.waiting_time for p in self.processes)
        total_response_time = sum(p.response_time for p in self.processes)
        
        n = len(self.processes)
        self.average_waiting_time = total_waiting_time / n
        self.average_response_time = total_response_time / n
        
        print(f'Tempo médio de espera: {self.average_waiting_time}')
        print(f'Tempo médio de resposta: {self.average_response_time}')

    def encontrar_indice_por_id(self, name):
        for indice, processo in enumerate(self.processes):
            if processo.name == name:
                return indice