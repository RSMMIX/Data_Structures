"""
คอยนาน
จำลองการเลื่อนแถวคอยภายในเวลาที่กำหนดโดยใช้ class queue

โดยที่มีแถวหลัก 1 แถวยาวกี่คนก็ได้

แถวหน้า cashier 1 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 3 นาทีในการคิดค่าบริการ

แถวหน้า cashier 2 ยาว 5 คน โดยที่คนนี้จะใช้เวลา 2 นาทีในการคิดค่าบริการ

ลูกค้าจะ move แถวทุกๆ 1 นาที โดยหากแถว 1 ว่างจะไปก่อนหากเต็มจึงไปแถว 2

จงแสดง นาที [แถวหลัก] [แถว cashier 1] [แถว cashier 2] จนกว่าแถวหลักจะหมด
"""
class Queue:
    def __init__(self):
        self.items = []

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop(0)

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def front(self) :
            return self.items[0]  

Q = Queue()
q1  = Queue()
q2  = Queue()
n = input("Enter people : ")
for i in n : 
    Q.push(i)
    
p = 0
p1 = 0
p2 = 0
while(1):
    p += 1
    if q1.size() < 5:
        q1.push(Q.front())
        Q.pop()

    else :
        q2.push(Q.front())
        Q.pop()
    print(f'{str(p)} {Q.items} {q1.items} {q2.items}')

    if not q1.isEmpty():
        p1 += 1
    if not q2.isEmpty():

        p2 += 1  
    if p1 == 3 :
        q1.pop()
        p1 = 0

    if p2 == 2 :
        q2.pop()
        p2 = 0
    if Q.isEmpty() :
        break