'''จงสร้างฟังก์ชัน ManageStack() ในการจัดการตัวเลขที่อยู่ใน Stack โดยที่จะมีคำสั่งดังนี้
A (add) : ทำการเพิ่มตัวเลขเข้าไปใน Stack
P (pop) : ทำการนำเลขสุดท้ายใน Stack ออก ( ถ้า Stack ว่างให้แสดงผล -1 )
D (delete) : ทำการลบตัวเลขที่ต้องการใน Stack ( ถ้า Stack ว่างให้แสดงผล -1 )  
LD (lessthan delete) : ทำการลบตัวเลขที่น้อยกว่าตัวเลขที่กำหนดทั้งหมดออกจาก Stack และแสดงผลตัวเลขที่ถูกลบไป ( ถ้า Stack ว่างให้แสดงผล -1 )
MD (Morethan delete) : ทำการลบตัวเลขที่มากกว่าตัวเลขที่ต้องการทั้งหมดออกจาก Stack และแสดงผลตัวเลขที่ถูกลบไป ( ถ้า Stack ว่างให้แสดงผล -1 )
การ Delete ทุกแบบ ถ้าหากไม่มีเลขที่ถูกลบเลย ไม่ต้องแสดงผลอะไรและให้ทำการแสดงผลค่าที่อยู่ใน Stack เมื่อจบโปรแกรม
*** Hint ***
ฟังก์ชัน Delete ต่างๆให้สร้าง Stack ขึ้นมาอีก 1 อันเพื่อใช้เป็น Temp ในการเก็บค่าตัวเลขต่างๆ'''

def ManageStack(stack):
    
    lst = []

    def A(lst,temp):
        lst.append(temp)
        print("Add = "+str(temp))

    def P(lst):
        if len(lst) == 0:
            print(-1)
        else:
            temp = lst[-1]
            lst.pop()
            print("Pop = "+str(temp))

    def D(lst,temp):
        nb = 0
        if len(lst) == 0:
            print(-1)
        else:
            for i in lst:
                if i == temp:
                    nb += 1 #nb = number
            for i in range(nb):
                lst.remove(temp)
                print("Delete = "+str(temp))

    def LD(lst,temp):
        telst = []
        if len(lst) == 0:
            print(-1)
        else:
            for i in range(len(lst)-1,-1,-1):
                if int(lst[i]) >= int(temp):
                    telst.append(lst[i])
                else:
                    print("Delete ="+str(lst[i])+" Because "+str(lst[i])+" is more than "+str(temp))