class PCB:

    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority

    def __repr__(self):
        return str(self.pid)  # Need reconsider

    def get_pid(self):
        return self.pid

    def display_pcb(self):
        print('PID: '+self.pid)
        print('Arrvial Time: '+self.arrival_time)
        print('Burst Time: '+self.burst_time)
        print('Priority: '+self.priority)
        print('\n')
