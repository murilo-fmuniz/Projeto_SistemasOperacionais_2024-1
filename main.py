from models.scheduler import Scheduler
from models.process import Process
from utils.ler_arquivo import ler_arquivo_e_criar_processos

import copy, os

def main(caminho_do_arquivo):

    processes = ler_arquivo_e_criar_processos(caminho_do_arquivo=caminho_do_arquivo)

    print(processes)

    schedulerSJF = Scheduler(copy.deepcopy(processes))
    schedulerRR = Scheduler(copy.deepcopy(processes))
    schedulerPP = Scheduler(copy.deepcopy(processes))
    print("\n\n\tSJF")
    schedulerSJF.sjf_preemptive()
    print("\n\n\tRR")
    schedulerRR.round_robin(quantum=3)
    print("\n\n\tPP")
    schedulerPP.priority_preemptive()


if __name__ == "__main__":
    caminho_do_arquivo = 'processos.txt'  # Coloque aqui o caminho do arquivo desejado
    main(caminho_do_arquivo)
