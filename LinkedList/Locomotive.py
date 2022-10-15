"""
มีรถไฟอยู่ขบวนหนึ่ง โดยรถไฟนั้นจะมีหมายเลขกำกับตู้แต่ละตู้อยู่และรถไฟก็มีหัวรถจักรอยู่

แต่หัวรถจักรดันไปต่อกับตู้รถไฟอยู่ พี่ต้องการให้น้อง ๆ ทำการแบ่งขบวนรถไฟออก

โดยให้หัวรถจักรอยู่ข้างหน้าสุด และส่วนตู้ที่เหลือให้ทำการต่อกับตู้สุดท้ายโดยไม่มีการเปลี่ยนลำดับของตู้

ซึ่งพี่จะให้หมายเลข 0 แทนเป็นหัวรถจักร ส่วน หมายเลขอื่นจะเป็นตู้รถไฟ

เช่น 2 <- 3 <- 1 <- 0 <- 4 <- 5 <- 6

เป็น 0 <- 4 <- 5 <- 6 <- 2 <- 3 <- 1 ( ให้ใช้ singly linked list)
"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return f'{self.data}'

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self) -> str:
        if self.head == None:
            return ''
        current = self.head.next
        out = str(self.head)
        while current is not None:
            out += ' <- ' + (str(current))
            current = current.next
        return out

    def append(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def moveHead(self):
        if self.head.data == 0:
            return

        current =  self.head
        while current.next.data != 0:
            current = current.next
        
        self.tail.next = self.head
        self.tail = self.head
        self.head = current.next
        self.tail = current
        current.next = None

print(' *** Locomotive ***')
n = input('Enter Input : ').split()
ll = LinkedList()
for i in n:
    ll.append(int(i))

print(f'Before : {ll}')
ll.moveHead()
print(f'After : {ll}')           