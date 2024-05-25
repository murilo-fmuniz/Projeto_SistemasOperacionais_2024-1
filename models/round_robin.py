from models.procedure import Procedure

class RoundRobin(Procedure):
    def __init__(self, quantum):
        super().__init__()
        self.quantum = quantum

    def executar(self):
        pass
