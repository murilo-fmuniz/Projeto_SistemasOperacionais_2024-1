from models.procedure import Procedure

class PrioridadePreemptiva(Procedure):
    def executar(self):
        self.processes.sort(key=lambda p: p.priority)
        self.calcular_tempos()
