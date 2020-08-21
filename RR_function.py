import LinkList
import PCB
import io

def RR_function():
    pcb_linklist = LinkList.Linklist()
    file = io.open('pcb1.txt', 'r', encoding='utf-8')
    for line in file:
        info = line.replace('\r', '').replace('\n', '').strip()
        info_list = info.split(',')
        if len(info_list) != 4:
            pass
        else:
            pcb = PCB.PCB(info_list[0], info_list[1], info_list[2], info_list[3])
            pcb_linklist.append(pcb)
    file.close()

    time_slice = 2
    pcb_linklist.sort_by_arrival_time()
    number_of_process = pcb_linklist.length
    waiting_time = 0
    current_time = 0
    while pcb_linklist.length > 0:
        current = pcb_linklist.head
        pid = current.data.pid
        arrival_time = current.data.arrival_time
        burst_time_left = current.data.burst_time

        if int(burst_time_left) > time_slice:
            burst_time = str(time_slice)
        else:
            burst_time = burst_time_left

        if int(arrival_time) > current_time:
            current_time = int(arrival_time)

        waiting_time = waiting_time + (current_time - int(arrival_time))

        print('Current time is {}'.format(str(current_time)))
        print(' -Process {} arrives at {} miliseconds and starts running: '.format(pid, arrival_time))
        print(' -Running for {} miliseconds'.format(burst_time))

        if int(burst_time_left) >= time_slice:
            current.data.burst_time = str(int(burst_time_left) - time_slice)
            current_time = current_time + time_slice
            current.data.arrival_time = str(current_time)
        else:
            current.data.burst_time = str(0)
            current_time = current_time + int(burst_time_left)
            current.data.arrival_time = str(current_time)

        if int(current.data.burst_time) != 0:
            pcb_linklist.sort_by_rr_curtime(current_time)
        else:
            pcb_linklist.pop()

    avg_waiting_time = waiting_time / number_of_process
    print("-----------------------------------------------------------")
    print('Average Waiting Time is: {}'.format(str(avg_waiting_time)))
    print("-----------------------------------------------------------")
