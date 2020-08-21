import LinkList
import PCB
import io

pcb_linklist = LinkList.Linklist()
file = io.open('pcb.txt', 'r', encoding='utf-8')
for line in file:
    info = line.replace('\r', '').replace('\n', '').strip()
    info_list = info.split(',')
    if len(info_list) != 4:
        pass
    else:
        pcb = PCB.PCB(info_list[0], info_list[1], info_list[2], info_list[3])
        pcb_linklist.append(pcb)
file.close()

pcb_linklist.display()
print('---------------')
# pcb_linklist.delete(2710)
# pcb_linklist.display()
# pcb_linklist.getItem(1).display_pcb()
