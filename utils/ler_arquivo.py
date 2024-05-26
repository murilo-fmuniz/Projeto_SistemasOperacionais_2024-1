import os

def ler_arquivo_e_criar_processos(caminho_do_arquivo):
    from models.processo import Processo

    n_process = 0
    

    caminho_completo = os.path.join(os.path.dirname(__file__), '..', caminho_do_arquivo)

    with open(caminho_completo, 'r') as file:
        linhas = file.readlines()

    nomes = linhas[0].strip().split(',')
    execution_times = list(map(int, linhas[1].strip().split(',')))
    arrival_times = list(map(int, linhas[2].strip().split(',')))
    priorities = list(map(int, linhas[3].strip().split(',')))

    processos = []
    for i in range(len(nomes)):
        processo = Processo(
            name=nomes[i],
            arrival_time=arrival_times[i],
            execution_time_needed=execution_times[i],
            priority=priorities[i]
        )
        processos.append(processo)
        n_process +=1

    return processos, n_process
