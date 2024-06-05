import heapq
from collections import deque
import copy, os

class Scheduler:
    def __init__(self, processes):
        self.processes = processes
        self.current_time = 0
        self.timeline = []

    def sjf_preemptive(self):
        process_queue = []
        completed_processes = 0
        n = len(self.processes)

        while completed_processes < n:
            for process in self.processes:
                if process.arrival_time == self.current_time:
                    heapq.heappush(process_queue, (process.remaining_time, process))

            if process_queue:
                current_process = heapq.heappop(process_queue)[1]
                if current_process.start_time is None:
                    current_process.start_time = self.current_time
                self.timeline.append((self.current_time, current_process.name))
                current_process.remaining_time -= 1

                if current_process.remaining_time == 0:
                    current_process.completion_time = self.current_time + 1
                    completed_processes += 1
                else:
                    heapq.heappush(process_queue, (current_process.remaining_time, current_process))

            self.current_time += 1

        for process in self.processes:
            process.turnaround_time = process.completion_time - process.arrival_time
            process.waiting_time = process.turnaround_time - process.execution_time_needed

        self.generate_report()

    def round_robin(self, quantum):
        process_queue = deque()
        for process in self.processes:
            if process.arrival_time == self.current_time:
                process_queue.append(process)

        while process_queue:
            current_process = process_queue.popleft()
            if current_process.start_time is None:
                current_process.start_time = self.current_time
            execution_time = min(current_process.remaining_time, quantum)
            current_process.remaining_time -= execution_time
            for _ in range(execution_time):
                self.timeline.append((self.current_time, current_process.name))
                self.current_time += 1

            if current_process.remaining_time > 0:
                for process in self.processes:
                    if process.arrival_time <= self.current_time and process not in process_queue:
                        process_queue.append(process)
                process_queue.append(current_process)
            else:
                current_process.completion_time = self.current_time

        for process in self.processes:
            process.turnaround_time = process.completion_time - process.arrival_time
            process.waiting_time = process.turnaround_time - process.execution_time_needed

        self.generate_report()

    def priority_preemptive(self):
        process_queue = []
        completed_processes = 0
        n = len(self.processes)

        while completed_processes < n:
            for process in self.processes:
                if process.arrival_time == self.current_time:
                    heapq.heappush(process_queue, (process.priority, process))

            if process_queue:
                current_process = heapq.heappop(process_queue)[1]
                if current_process.start_time is None:
                    current_process.start_time = self.current_time
                self.timeline.append((self.current_time, current_process.name))
                current_process.remaining_time -= 1

                if current_process.remaining_time == 0:
                    current_process.completion_time = self.current_time + 1
                    completed_processes += 1
                else:
                    heapq.heappush(process_queue, (current_process.priority, current_process))

            self.current_time += 1

        for process in self.processes:
            process.turnaround_time = process.completion_time - process.arrival_time
            process.waiting_time = process.turnaround_time - process.execution_time_needed

        self.generate_report()

    def generate_report(self):
        timeline_str = "LINHA DO TEMPO\n\n|0|"
        last_time = 0

        for i, (time, name) in enumerate(self.timeline):
            if i == 0 or self.timeline[i-1][1] != name:
                timeline_str += f"{time}|−−−−−{name}−−−−−|"
            last_time = time + 1

        max_time = self.timeline[-1][0] + 1 if self.timeline else 0
        timeline_str += f"|{max_time}|\n\n"

        wait_times = "Tempo de Espera de cada processo:\n"
        response_times = "Tempo de Resposta de cada processo:\n"
        process_names = "    " + "    ".join(p.name for p in self.processes) + "\n"
        wait_values = "    " + "    ".join(str(p.waiting_time) for p in self.processes) + "\n"
        response_values = "    " + "    ".join(str(p.start_time - p.arrival_time) for p in self.processes) + "\n"

        avg_response_time = sum(p.start_time - p.arrival_time for p in self.processes) / len(self.processes)
        avg_wait_time = sum(p.waiting_time for p in self.processes) / len(self.processes)

        report = (
            f"{timeline_str}\n"
            f"{wait_times}{process_names}{wait_values}\n"
            f"{response_times}{process_names}{response_values}\n"
            f"\nTempo Médio de Resposta: {avg_response_time:.2f}\n"
            f"Tempo Médio de Espera: {avg_wait_time:.2f}\n"
        )

        print(report)