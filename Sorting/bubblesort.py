"""
รับ input เป็น list แล้วแสดงขั้นตอนของ bubble sort ตามตัวอย่าง

***ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort เช่น .sort ให้น้องเขียนฟังก์ชัน Sort เอง และห้าม Import***

"""

inp = list(map(int,input("Enter Input : ").split(" ")))
for i in range(len(inp)-1):
    swapped = False
    temp = [None]
    for j in range(0,len(inp)-i-1):
        if inp[j] > inp[j+1]:
            if not inp[j] in temp:
                temp.pop()
                temp.append(inp[j])
            inp[j], inp[j+1] = inp[j+1], inp[j]
            swapped = True
    if swapped == False or i == len(inp)-2:
        print("last step : " +str(inp)+" move"+str(temp))
        break
    else:
        print(str(i+1)+" step : "+str(inp)+" move"+str(temp))
    