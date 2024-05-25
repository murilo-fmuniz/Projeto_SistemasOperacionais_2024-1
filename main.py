from models.sjf_preemptivo import SJFPreemptivo
from models.round_robin import RoundRobin
from models.prioridade_preemptiva import PrioridadePreemptiva
from utils.ler_arquivo import ler_arquivo_e_criar_processos

def main(caminho_do_arquivo):

    processos = ler_arquivo_e_criar_processos(caminho_do_arquivo)


    sjf = SJFPreemptivo()
    rr = RoundRobin(4)  # Quantum = 4
    prioridade = PrioridadePreemptiva()


    for processo in processos:
        sjf.adicionar_processo(processo)
        rr.adicionar_processo(processo)
        prioridade.adicionar_processo(processo)


    



if __name__ == "__main__":
    caminho_do_arquivo = 'processos.txt'  # Coloque aqui o caminho do seu arquivo
    main(caminho_do_arquivo)
