"""
โรงอาหารของบริษัทแห่งหนึ่ง จะมีเจ้าหน้าที่คอยจัดแถวสำหรับการซื้ออาหาร โดยจะมีหลักการคือจะดูจากแผนกของพนักงานแต่ละคนว่าอยู่แผนกไหน ถ้าหากในแถวที่ต่ออยู่มีแผนกนั้น จะนำพนักงานคนนั้นแทรกไปด้านหลังของแผนกเดียวกัน ตัวอย่างเช่น
Front | 1 2 2 2 2 3 3 3 | Rear  จาก Queue ถ้าหากมีพนักงานแผนก1เข้ามา Queue จะกลายเป็น Front | 1 1 2 2 2 2 3 3 3 | Rear

Input :
จะแบ่งเป็น 2 ฝั่งแบ่งด้วย /   คือ ซ้าย : เป็นแผนกของพนักงานและIDของพนักงานแต่ละคน  ขวา : จะแบ่งเป็น 2 ส่วน คือ D กับ E
E < id >  ->   เป็นการนำพนักงานเข้า Queue
D  ->  เป็นการนำพนักงานคนหน้าสุดออกจากแถว โดยจะแสดงผลเป็น id ของพนักงานคนนั้น ถ้าหากไม่มีพนักงานในแถวจะทำการแสดงผลเป็น Empty

อธิบาย TestCase_1 :  จะมีพนักงาน 4 คน คือแผนก 1 id=101,102 และแผนก 2 id=201,202  ต่อมาจะแสดงผล Empty เพราะยังไม่มีพนักงานในแถว  และนำพนักงาน id=101และ201 เข้าแถวตามลำดับ ต่อมาจะแสดงผลเป็น 101 เพราะพนักงาน 101 อยู่คนแรกและแสดงผล 201 เพราะอยู่คนแรก
"""



class Queue:
    def __init__(self,ls = None):
        if ls == None:
            self.items = []
        else:
            self.items = ls

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


info, action = input("Enter Input : ").split("/")

info = dict([i.split()[::-1] for i in info.split(',')])
lq = []

def search(id):
    for i in range(len(lq)):
        if info[lq[i].front()] == info[id]:
            return i
    return -1

for i in action.split(','):
    i = i.split()
    if i[0] == 'E':
        id = i[1]
        index = search(id)
        if index != -1 :
            lq[index].enQueue(id)
        else:
            lq.append(Queue([id]))


    elif i[0] == 'D':
        if not lq:
            print('Empty')
        else:
            print(lq[0].deQueue())
            if lq[0].isEmpty():
                lq.pop(0)