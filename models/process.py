class Process:
    def __init__(self, name, arrival_time, execution_time_needed, priority):
        self.name = name
        self.arrival_time = arrival_time
        self.execution_time_needed = execution_time_needed
        self.priority = priority
        self.remaining_time = execution_time_needed  # Usado para políticas preemptivas
        self.completion_time = None
        self.waiting_time = None
        self.turnaround_time = None
        self.start_time = None  # Para cálculo do tempo de resposta

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        return f"{self.name}(arrival: {self.arrival_time}, remaining: {self.remaining_time}, priority: {self.priority})"