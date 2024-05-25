from models.sjf_preemptivo import SJFPreemptivo
from models.round_robin import RoundRobin
from models.prioridade_preemptiva import PrioridadePreemptiva
from utils.ler_arquivo import ler_arquivo_e_criar_processos

def main(caminho_do_arquivo):
    # Ler o arquivo e criar os processos
    processos = ler_arquivo_e_criar_processos(caminho_do_arquivo)

    # Criar instâncias das classes de procedimento
    sjf = SJFPreemptivo()
    rr = RoundRobin(4)  # Quantum = 4
    prioridade = PrioridadePreemptiva()

    # Adicionar os processos aos respectivos procedimentos
    for processo in processos:
        sjf.adicionar_processo(processo)
        rr.adicionar_processo(processo)
        prioridade.adicionar_processo(processo)

    # Executar os procedimentos
    sjf.executar()
    rr.executar()
    prioridade.executar()

    # Relatórios
    print("\nPolítica: SJF Preemptivo")
    sjf.relatorio()

    print("\nPolítica: Round-Robin")
    rr.relatorio()

    print("\nPolítica: Prioridade Preemptiva")
    prioridade.relatorio()


# Executar a aplicação com o arquivo fornecido
if __name__ == "__main__":
    caminho_do_arquivo = 'processos.txt'  # Coloque aqui o caminho do seu arquivo
    main(caminho_do_arquivo)
