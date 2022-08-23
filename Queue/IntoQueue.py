'''
ให้น้องๆเขียนโปรแกรมโดยรับ input 2 แบบ โดยใช้ Queue ในการแก้ปัญหา
E  <value>  ให้นำ value ไปใส่ใน Queue และทำการแสดงผล ข้อมูลปัจจุบันของ Queue

D ให้ทำการ Dequeue ตัวที่อยู่หน้าสุดของ Queue ออก หลังจากนั้นแสดงตัวเลขที่เอาออกมา และ แสดงผลข้อมูลปัจจุบันของ Queue

***และเมื่อจบการทำงานให้แสดงผลข้อมูลปัจจุบันของ Queue พร้อมกับข้อมูลที่ถูก Dequeue ทั้งหมดตามลำดับ
***ถ้าหากไม่มีข้อมูลใน Queue แล้วให้แสดงคำว่า  Empty
'''

class Queue:
    def __init__(self):
        self.items = []

    def enQueue(self, i):
        self.items.append(i)

    def deQueue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def front(self) :
        return self.items[0]  

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        return ", ".join(self.items)

q1 = Queue()
q2 = Queue()
n = input('Enter Input : ').split(',')
for i in n:
    i = i.split()
    if i[0] == 'E':
        q1.enQueue(i[1])
        print(q1)
    elif i[0] == 'D':
        if q1.isEmpty():
            print(q1)
        else:
            d = q1.deQueue()
            q2.enQueue(d)
            print(f'{d} <- {q1}')
print(f'{q2} : {q1}')
