"""

นักศึกษาจะได้รับ Input เป็น list<int> ของดาวเคราะห์น้อย
สำหรับดาวเคราะห์น้อยแต่ละดวงนั้น ค่าสัมบูรณ์ จะแสดงขนาดของมัน และเครื่องหมายแสดงถึงทิศทางของมัน (ถ้าเลขเป็นบวกแสดงว่าวิ่งไปทางขวา ,ลบทางซ้าย) โดยที่ดาวเคราะห์น้อยแต่ละดวงเคลื่อนที่ด้วยความเร็วเท่ากัน

ค้นหาสถานะของดาวเคราะห์น้อยหลังจากการชนกันทั้งหมด

1.หากดาวเคราะห์น้อยสองดวงมาพบกันดวงที่เล็กกว่าจะระเบิด

2.ถ้าทั้งสองมีขนาดเท่ากันทั้งคู่จะระเบิด

3.ดาวเคราะห์น้อยสองดวงที่เคลื่อนที่ไปในทิศทางเดียวกันจะไม่มีวันพบกัน

****ห้ามใช้คำสั่ง for, while, do while*****

หมายเหตุ ฟังก์ชันมี parameter ได้ไม่เกิน 2 ตัว 

"""
def asteroid_collision(asts,index):
    if len(asts) == 0:
        return asts
    if index == 0:
        return asts
    if index-1 >= 0:
        #print("DATA: ",asts[index])
        #print("PREV DATA: ",asts[index-1])
        if asts[index] < 0 and asts[index - 1] > 0:
            if -asts[index] > asts[index - 1]:
                asts.pop(index - 1)
            elif -asts[index] == asts[index - 1]:
                asts.pop(index)
                asts.pop(index - 1)
            elif -asts[index] < asts[index - 1]:
                asts.pop(index)
            asteroid_collision(asts, len(asts)-1)
        else:
            asteroid_collision(asts, index - 1)
    #print("INDEX-1",index-1)
 
 
    return asts
 
 
x = input("Enter Input : ").split(",")
x = list(map(int,x))
print((asteroid_collision(x,len(x)-1)))