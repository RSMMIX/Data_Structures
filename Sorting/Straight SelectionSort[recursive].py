"""
เขียน function Straight Selection Sort เพื่อเรียงข้อมูลใน list จากน้อยไปมาก โดยใช้ recursive

และแสดงขั้นตอนของ Straight Selection Sort ตามตัวอย่าง

***ห้ามใช้ คำสั่งloopต่างๆ เช่น for ,while หรือ Built-in Function ที่เกี่ยวกับ Sort เช่น .sort***

*** ยกเว้นให้ใช้  for ได้แค่ขั้นตอนรับ input เท่านั้น ***
"""

def str_selection(n, k, m, i):
    if n == len(inp) - 1:
        return
    if k == len(inp) - n:
        inp[i], inp[len(inp) - n - 1] = inp[len(inp) - n - 1], inp[i]
        if len(inp) - n - 1 != i:
            print(f'swap {inp[i]} <-> {inp[len(inp) - n - 1]} : {inp}')
        str_selection(n+1, 0, -1, -1)
        return
    if inp[k] > m:
        str_selection(n, k+1, inp[k], k)
    else:
        str_selection(n, k+1, m, i)

inp = list(map(int, input('Enter Input : ').split()))
str_selection(0, 0, -1, 0)
print(inp)