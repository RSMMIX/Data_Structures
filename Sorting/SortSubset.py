"""
ให้น้องรับ input มา 2 อย่างโดยคั่นด้วย /

1. ด้านซ้าย เป็นผลลัพธ์
2. ด้านขวา เป็น list ของจำนวนเต็ม

โดยผลลัพธ์ให้แสดงเป็น subset ของ input ด้านขวาที่มีผลรวมได้เท่ากับ input ด้านซ้าย และมี Pattern การแสดงผลลัพธ์ดังนี้

1. ให้เรียงลำดับจากขนาดของ subset จากน้อยไปมาก
2. ถ้าหาก subset มีขนาดเท่ากันให้เรียงลำดับจำนวนเต็มใน subset จากน้อยไปมาก

ถ้าหากไม่มี subset ไหนที่ผลรวมเท่ากับ input ด้านซ้าย ให้แสดงว่า No Subset



****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง และห้าม Import

อธิบาย Test Case 1:
[2]
[-1, 3]
[0, 2]  # [-1, 3] กับ [0, 2] มีขนาดเท่ากัน แต่ -1 < 0 ดังนั้น [-1, 3] จึงแสดงผลก่อน [0, 2]
[-3, 2, 3]
[-2, 1, 3]
[-1, 0, 3]
[-1, 1, 2]
[-3, 0, 2, 3]
[-2, -1, 2, 3]
[-2, 0, 1, 3]   # [-2, -1, 2, 3] กับ [-2, 0, 1, 3] มีขนาดและตัวแรกสุดเท่ากัน แต่ตัวที่สอง -1 < 0 ดังนั้น [-2, -1, 2, 3] จึงแสดงผลก่อน [-2, 0, 1, 3]
[-1, 0, 1, 2]
[-3, -1, 1, 2, 3]
[-2, -1, 0, 2, 3]
[-3, -1, 0, 1, 2, 3]

"""
def printRecur(num, left, res, x=0, list=[]):
    sum = 0
    patten = 0
    for i in list:
        sum += i
    if left == 0:
        if res == sum:
            print(list)
            return 1
        return 0
    elif x >= len(num):
        return 0
    else:
        patten += printRecur(num, left-1, res, x + 1, list + [num[x]])
        patten += printRecur(num, left, res, x + 1, list)
    return patten


inp = input('Enter Input : ').split("/")
res = int(inp[0])
num = [int(x) for x in inp[1].split()]
for i in range(len(num)):
    for j in range(len(num)-1-i):
        if num[j] > num[j+1]:
            num[j], num[j+1] = num[j+1], num[j]
patten = 0
for j in range(len(num)):
    patten += printRecur(num, j+1, res)
if patten == 0:
    print('No Subset')