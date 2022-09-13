class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.previous = None


class DoublyLinkedList :
        
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    def __str__(self):
        str = ""
        prv = self.head
        while prv != None: #printval
            str += (prv.data + ("->" if(prv.next != None) else ""))
            prv = prv.next
        return f"linked list : {str}"


    def str_reverse(self):
        str = ""
        prv = self.tail
        while prv != None:
            str += (prv.data + ("->" if(prv.previous != None) else ""))
            prv = prv.previous
        return f"reverse : {str}"

        
    def isEmpty(self):
        return True if(self.head == None) else False


    def append(self, data):
        new_Node = Node(data)
        if(self.isEmpty()):
            self.head = new_Node
            self.tail = new_Node
        else:
            new_Node.previous = self.tail
            self.tail.next = new_Node
            self.tail = new_Node
        self.size += 1


    def insert(self, index, data):
        new_Node = Node(data)
        if(int(index) >= 0 and int(index) <= self.size):
            if(int(index) == self.size):
                self.append(data)
            elif(int(index) == 0):
                if(self.head != None):
                    self.head.previous = new_Node
                new_Node.next = self.head
                self.head = new_Node
            else:
                now = self.head
                for i in range(int(index)-1):
                    if(now.next == None):
                        break
                    now = now.next
                new_Node.previous = now
                new_Node.next = now.next
                if(now.next != None):
                    now.next.previous = new_Node
                else:
                    self.tail = new_Node
                now.next = new_Node
            self.size += 1
        else:
            return "Data cannot be added"
        return f"index = {int(index)} and data = {data}"


    def remove(self, data):
        index = 0
        now = self.head
        if(now != None):
            if(int(now.data) == int(data)):
                self.head = now.next
                if(now.next != None):
                    now.next.previous = None
                if(self.head == None):
                    self.tail = None
                    self.size = 0
                now = None
                return f"removed : {int(data)} from index : 0"
        while(now != None):
            if(int(now.data) == int(data)):
                if(now.next == None):
                    self.tail = now.previous
                break
            index += 1
            prev = now
            now = now.next
        if(now == None):
            return "Not Found!"
        prev.next = now.next
        now.next.previous = prev
        now = None
        self.size -= 1
        return f"removed : {int(data)} from index : {int(index)}"


listed = DoublyLinkedList()
inp = input("Enter Input : ").split(',')
l1 = []
l2 = []
for e in inp:
    l1.append([i for i in e.split()])
for e in l1:
    l2.append([e[0], [i for i in e[1].split(":")]])

for e in l2:
    if(e[0] == "A"):
        listed.append(e[1][0])
    elif(e[0] == "Ab"):
        listed.insert(0, e[1][0])
    elif(e[0] == "I"):
        print(listed.insert(e[1][0], e[1][1]))
    elif(e[0] == "R"):
        print(listed.remove(e[1][0]))
    print(listed.__str__())
    print(listed.str_reverse())