'''จงสร้างฟังก์ชัน ManageStack() ในการจัดการตัวเลขที่อยู่ใน Stack โดยที่จะมีคำสั่งดังนี้
A (add) : ทำการเพิ่มตัวเลขเข้าไปใน Stack
P (pop) : ทำการนำเลขสุดท้ายใน Stack ออก ( ถ้า Stack ว่างให้แสดงผล -1 )
D (delete) : ทำการลบตัวเลขที่ต้องการใน Stack ( ถ้า Stack ว่างให้แสดงผล -1 )  
LD (lessthan delete) : ทำการลบตัวเลขที่น้อยกว่าตัวเลขที่กำหนดทั้งหมดออกจาก Stack และแสดงผลตัวเลขที่ถูกลบไป ( ถ้า Stack ว่างให้แสดงผล -1 )
MD (Morethan delete) : ทำการลบตัวเลขที่มากกว่าตัวเลขที่ต้องการทั้งหมดออกจาก Stack และแสดงผลตัวเลขที่ถูกลบไป ( ถ้า Stack ว่างให้แสดงผล -1 )
การ Delete ทุกแบบ ถ้าหากไม่มีเลขที่ถูกลบเลย ไม่ต้องแสดงผลอะไรและให้ทำการแสดงผลค่าที่อยู่ใน Stack เมื่อจบโปรแกรม
*** Hint ***
ฟังก์ชัน Delete ต่างๆให้สร้าง Stack ขึ้นมาอีก 1 อันเพื่อใช้เป็น Temp ในการเก็บค่าตัวเลขต่างๆ'''


class Stack:
    def __init__(self,list = None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self,i):
        self.items.append(i)
           
    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []
        
    def size(self):
        return (len(self.items))

    def peek(self):
        return self.items[-1]
        


def ManageStack(i):
    if i[0] == 'A':
        s.push(int(i[1]))
        print(f'Add = {i[1]}') 

    elif i[0] == 'P':
        if s.isEmpty():
            print(-1)
        else:
            print(f'Pop = {s.pop()}')

    elif i[0] == 'D':
        if s.isEmpty():
            print(-1)
        else:
            value = int(i[1])
            temp = Stack()
        while not s.isEmpty():
            temp.push(s.pop())
            if temp.peek() == value:
                wtd = temp.pop()
                print(f'Delete = {wtd}')
        while not temp.isEmpty():
            s.push(temp.pop())
    
    elif i[0] == 'LD':
        if s.isEmpty():
            print(-1)
        else:
            value = int(i[1])
            temp = Stack()
        while not s.isEmpty():
            temp.push(s.pop())
            if temp.peek() < value:
                wtd = temp.pop()
                print(f'Delete = {wtd} Because {wtd} is less than {value}')
        while not temp.isEmpty():
            s.push(temp.pop())

    elif i[0] == 'MD':
        if s.isEmpty():
            print(-1)
        else:
            value = int(i[1])
            temp = Stack()
        while not s.isEmpty():
            temp.push(s.pop())
            if temp.peek() > value:
                wtd = temp.pop()
                print(f'Delete = {wtd} Because {wtd} is more than {value}')
        while not temp.isEmpty():
            s.push(temp.pop())


s = Stack()
n = input('Enter Input : ').split(',')
for i in n:
    i = i.split()
    ManageStack(i)


