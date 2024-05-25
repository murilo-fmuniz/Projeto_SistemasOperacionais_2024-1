class Processo:
    def __init__(self, name, arrival_time, execution_time_needed, priority):
        self.name = name
        self.arrival_time = arrival_time
        self.execution_time_needed = execution_time_needed
        self.priority = priority
        self.waiting_time = 0
        self.response_time = 0
