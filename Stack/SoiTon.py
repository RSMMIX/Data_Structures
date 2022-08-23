'''ที่จอดรถของนาย ก เป็นส่วนที่แรเงาสีฟ้า ส่วนสีแดงเป็นที่ของนาย ข ซี่งเป็นญาติกัน ที่จอดรถของนาย ก และ นาย ข แคบมาก จอดรถได้เรียงเดี่ยว นาย ข ไม่ได้ใช้ที่จอดรถ แต่ อนุญาติให้นาย ก ใช้ที่จอดรถของเขาได้โดยไม่จอดรถแช่ไว้ เนื่องจากซอยแคบ ดังนั้นการมาจอด (arrive) และการรับรถ (depart)จะเป็นลักษณะของ stack เงื่อนไขคือ ในการรับรถ x ใดๆอยากให้ลำดับรถเป็นเหมือนเดิม ดังรูป simulate การจอดรถในที่จอดรถของนาย ก โดยใช้ operation ของ stack ข้างล่างเป็นตัวอย่าง output

การรับ input : รับ input 4 ค่าใน 1 บรรทัดโดยให้แยกโดย " " (space bar) โดยตำแหน่งแรกคือ จำนวนสูงสุดที่รถสามารถจอดได้ในซอยของ นาย ก ตำแหน่งที่สองคือ รถที่จอดอยู่ในซอยของ นาย ก ตำแหน่งที่สามคือ การกระทำเช่น ถ้าเป็น arrive จะทำการเพิ่มรถในซอย ส่วน depart จะทำการเอารถออกจากซอย โดยรถที่จะทำการเพิ่มหรือนำออกนั้นจะเป็น เลขในตำแหน่งที่ 4

***หมายเหตุ ถ้าในซอยไม่มีรถอยู่เลยให้ input = 0 ในตำแหน่งที่ 2***

*** สามารถสร้างได้มากกว่า 1 stack ***

'''


class Stack:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list

    def push(self, i):
        self.items.append(i)

    def pop(self):
        return self.items.pop(len(self.items)-1)

    def isEmpty(self):
        return self.items == []

    def size(self):
        return (len(self.items))


print('******** Parking Lot ********')

m, s, o, n = input("Enter max of car,car in soi,operation : ").split()
s = list(s.split(','))
m, n = int(m), int(n)

if o == 'arrive':
    if len(s) < m:
        if str(n) in s:
            print("car "+str(n)+" already in soi")
        else:
            print("car "+str(n)+" arrive! : Add Car "+str(n))
            s.append(n)
    else:
        print("car "+str(n)+" cannot arrive : Soi Full ")
else:
    if '0' in s:
        print("car "+str(n)+" cannot depart : Soi Empty")
    elif str(n) not in s:
        print("car "+str(n)+" cannot depart : Dont Have Car "+str(n))
    else:
        print("car "+str(n)+" depart ! : Car "+str(n)+" was remove")
        s.remove(str(n))


temp = []
for i in s:
    temp.append(int(i))
    if int(i) == 0:
        temp.remove(0)
print(temp)
