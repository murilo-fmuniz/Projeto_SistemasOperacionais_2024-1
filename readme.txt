Descrição:
    Neste trabalho, os discentes participantes da disciplina Sistemas Operacionais do curso de Engenharia de Computação possuem como tarefa a implementação de um simulador de gerenciador de processos. Nesse sentido, é pretendido que cada dupla implemente um escalonador de processos de curto prazo, alternando os processos de acordo com diversas políticas de escalonamento. O simulador deverá simular a execução dos processos da seguinte maneira:

    1) O usuário entra com um arquivo ao qual possui diversas programas descritos para execução;

    2) O simulador lê o arquivo e simula a execução do processo;

    3) No final da execução da simulação o simulador deverá retornar a linha do tempo como resultado da simulação;

    4) Além disso, o simulador deverá retornar os Tempos médios e individuais de espera e resposta para cada aplicação;

    Os arquivos que recebem as descrições dos processos seguindo o formato:

    
    Processo	  A	 B	 C	 D	 E	 F	 G	 H	 I	 J
    Tempo	10	11	12	13	14	15	16	17	18	19
    Chegada	0	1	2	3	4	5	6	7	8	9
    Prioridade	 0	0	0	0	0	0	0	0	0	0
    5) O simulador deverá simular a execução de todos os processos e no final exibir um relatório, semelhante ao exemplo a seguir:

    Processos na Fila do First Come First Served:
        A    B    C    D    E    F    G    H    I    J

    Tempo de CPU requerida pelos processos:
    10   11   12   13   14   15   16   17   18   19

    Tempo de Chegada dos processos:
        0    1    2    3    4    5    6    7    8    9





    LINHA DO TEMPO

    |0|−−−−−A−−−−−|10|−−−−−B−−−−−−|21|−−−−−−C−−−−−−|33|−−−−−−D−−−−−−−|46|−−−−−−−E−−−−−−−|60|−−−−−−−F−−−−−−−−|75|−−−−−−−−G−−−−−−−−|91|−−−−−−−−H−−−−−−−−−|108|−−−−−−−−−I−−−−−−−−−|126|−−−−−−−−−J−−−−−−−−−−|145|






    Tempo de Espera de cada processo:
        A    B    C    D    E    F    G    H    I    J
        0    9   19   30   42   55   69   84  100  117




    Tempo de Resposta de cada processo:
        A    B    C    D    E    F    G    H    I    J
    10   20   31   43   56   70   85  101  118  136




    Tempo Médio de Resposta: 67.00




    Tempo Médio de Espera: 52.50

    6) Deverão ser implementadas as seguintes políticas.

    SJF preemptivo

    Round-Robin

    Prioridade estática Preemptiva

aplicação
ler arquivo
salvar os valores lidos no arquivo num objeto processador de objetos processos
        processador:
            process processeses[]
            int average_response_time
        process:
            str name
            int arrival_time
            int execution_time_needed
            int priority
            int waiting_time
            int response_time

aplicar as políticas requisitadas: 
    SJF preemptivo:             #processo com menor tempo de execução é escolhido para a proxima execução

    Round-Robin:                #processos re-escalonados periodicamente dependente do _quantum_ de tempo, com FIFO 

    Prioridade Preemptiva:      #processos novos são alocados numa fila de prioridade com base na chegada 


relatório  
    deve conter:
        linha do tempo de execução
        Tempo de espera de cada processo  
        Tempo de execução de cada processo
        Tempo medio de espera
        Tempo médio de execução
        