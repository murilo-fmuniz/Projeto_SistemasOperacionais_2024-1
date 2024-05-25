# models/sjf_preemptivo.py
from models.procedure import Procedure

class SJFPreemptivo(Procedure):
    def executar(self):
        self.processes.sort(key=lambda p: p.execution_time_needed)
        self.calcular_tempos()
