from FCFS_function import FCFS_function
from Priority_function import Priority_function
from RR_function import RR_function

while True:
    print('\n\n\n')
    print('Algorithm 1: FCFC Scheduling')
    print('Algorithm 2: Non-preemptive Scheduling')
    print('Algorithm 3: RR Scheduling')
    choice = input('Now please choices your scheduling algorithm or enter exit if you want to quit:')
    choices = ['1', '2', '3', 'exit']
    while choice not in choices:
        choice = input('Please enter 1, 2, or 3 to select Scheduling Algorithm or enter exit to quit the system:')
    if choice == '1':
        FCFS_function()
    if choice == '2':
        Priority_function()
    if choice == '3':
        RR_function()
    if choice == 'exit':
        break

