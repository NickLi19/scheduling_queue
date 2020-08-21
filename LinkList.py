class Node:

    def __init__(self, data, pnext=None):
        self.data = data
        self._next = pnext

    def __repr__(self):
        return str(self.data)  # Need reconsider

class Linklist(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def isEmpty(self):
        return (self.length == 0)

    def append(self, pcb):
        item = Node(pcb)
        if self.tail == None:
            self.head = item
            self.tail = item
            self.length += 1

        else:
            item._next = None
            self.tail._next = item
            self.tail = item
            self.length += 1

    def insert(self, index, pcb):
        if self.isEmpty():
            print('This queue is empty.')
            return

        if index < 0 or index > self.length:
            print('Error: Out of Index! Index={} and Length={}'.format(str(index), str(self.length)))
            return

        item = Node(pcb)

        if index == 0:
            item._next = self.head
            self.head = item
            self.length += 1
            return

        flag = 0
        current = self.head
        previous = self.head
        while current._next and flag < index:
            previous = current
            current = current._next
            flag += 1

        if flag == index:
            item._next = current
            previous._next = item
            self.length += 1

    def update(self, index, pcb):
        if self.isEmpty():
            print('This queue is empty.')
            return

        if index < 0 or index >= self.length:
            print('Error: Out of Index!')
            return

        flag = 0
        current = self.head
        while current._next and flag < index:
            current = current._next
            flag += 1

        if flag == index:
            current.data = pcb

    def pop(self):
        if self.isEmpty():
            print('This queue is empty.')

        else:
            pop_item = self.head
            self.head = self.head._next
            self.length -= 1
            del pop_item

    def delete(self, pid):
        index = self.getIndex(pid)
        if index < 0 or index >= self.length:
            return

        if index == 0:
            self.head = self.head._next
            self.length -= 1
            return

        flag = 0
        current = self.head
        previous = self.head
        while current._next and flag < index:
            previous = current
            current = current._next
            flag += 1

        if flag == index:
            previous._next = current._next
            self.length -= 1
            del current

    def sort_by_arrival_time(self):
        current = self.head
        end = None
        while current != end:
            while current._next != end:
                if int(current.data.arrival_time) > int(current._next.data.arrival_time):
                    temp = current.data
                    current.data = current._next.data
                    current._next.data = temp
                current = current._next
            end = current
            current = self.head

    def sort_by_priority_curtime(self, current_time):
        current = self.head
        current1 = self.head
        end = None
        while current1 and int(current1.data.arrival_time) <= current_time:
            current1 = current1._next
            end = current1

        while current != end:
            while current._next != end:
                if int(current.data.priority) >= int(current._next.data.priority):
                    temp = current.data
                    current.data = current._next.data
                    current._next.data = temp
                current = current._next
            end = current
            current = self.head

    def sort_by_rr_curtime(self, current_time):
        current = self.head
        index = 0
        while current and int(current.data.arrival_time) <= current_time:
            current = current._next
            index += 1

        if index == self.length:
            self.append(self.head.data)
        else:
            self.insert(index, self.head.data)
        self.pop()

    def getItem(self, index):
        if self.isEmpty():
            print('This queue is empty.')
            return

        if index < 0 or index >= self.length:
            print('Error: Out of Index!')
            return

        flag = 0
        current = self.head
        while current._next and flag < index:
            current = current._next
            flag += 1

        return current.data


    def getIndex(self, pid):
        flag = 0
        if self.isEmpty():
            print('This queue is empty.')
            return
        item = self.head
        while item:
            item_pid = int(item.data.pid)  # convert pid to int
            if item_pid == pid:
                return flag
            item = item._next
            flag += 1

        if flag == self.length:
            print('PCB is not found!')
            return -1

    def display(self):
        if self.isEmpty():
            print('This queue is empty.')
            return

        flag = 0
        current = self.head
        while current and flag < self.length:
            # print(current.data)
            current.data.display_pcb()
            current = current._next
            flag += 1

    def clear(self):
        flag = 0
        current = self.head
        while current._next and flag < self.length:
            previous = current
            current = current._next
            flag += 1
            del previous
        self.head = None
        self.tail = None
        self.length = 0
