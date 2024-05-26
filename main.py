from models.sjf_preemptivo import SJFPreemptivo
from models.round_robin import RoundRobin
from models.prioridade_preemptiva import PrioridadePreemptiva
from models.processo import Processo
from utils.ler_arquivo import ler_arquivo_e_criar_processos

def main(caminho_do_arquivo):

    file_result = ler_arquivo_e_criar_processos(caminho_do_arquivo)
    processos = file_result[0]
    n_processos = file_result[1]

    sjf = SJFPreemptivo(n_processos)
    #rr = RoundRobin(4)  # Quantum = 4
    #prioridade = PrioridadePreemptiva()


    for processo in processos:
        sjf.adicionar_processo(processo)
        #rr.adicionar_processo(processo)
        #prioridade.adicionar_processo(processo)

    sjf.imprimirProcessos()
    #rr.imprimirProcessos()
    #prioridade.imprimirProcessos()

    sjf.executar()

    print(f'SJF: {sjf.completed_processes}\n')
    #for process in sjf.processes:
    #    print(f'{process.name} wt: {process.waiting_time} rp: {process.response_time}')
    #sjf.calcular_tempos()


if __name__ == "__main__":
    caminho_do_arquivo = 'processos.txt'  # Coloque aqui o caminho do seu arquivo
    main(caminho_do_arquivo)
