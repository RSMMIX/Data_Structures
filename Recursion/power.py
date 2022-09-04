'''
****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )

เขียน Recursive รับค่า a,b โดยที่ a,b เป็นจำนวนเต็มบวกหรือศูนย์ และค่าหา ab  
'''
def power(a, b):
    if b == 0:
        return 1

    return a*power(a,b-1)

n = input('Enter Input a b : ').split()
x = int(n[0])
y = int(n[1])
print(power(x,y))