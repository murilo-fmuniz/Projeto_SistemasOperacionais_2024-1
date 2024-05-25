# Importando módulos para facilitar o uso externo
from .processo import Processo
from .procedure import Procedure
from .sjf_preemptivo import SJFPreemptivo
from .round_robin import RoundRobin
from .prioridade_preemptiva import PrioridadePreemptiva

# Definindo o __all__ para controlar o que é exportado quando alguém importa o pacote
__all__ = [
    'Processo',
    'Procedure',
    'SJFPreemptivo',
    'RoundRobin',
    'PrioridadePreemptiva'
]
