
#ให้นักศึกษาเขียนโปรแกรมภาษา Python ในการสร้าง range() ใหม่ขึ้นมาโดยใช้ function แค่ 1 function
#ถ้าหากเป็น 1 argument -> range(a)            | start = 0 , end = a , step = 1
#ถ้าหากเป็น 2 argument -> range(a, b)        | start = a , end = b , step = 1
#ถ้าหากเป็น 3 argument -> range(a, b, c)    | start = a , end = b , step = cdef range2(*args):
def range2(*args):
    if len(args) == 1:
        start = 0
        end = args[0]
        step = 1
    elif len(args) == 2:
        start = args[0]
        end = args[1]
        step = 1
    elif len(args) == 3:
        start = args[0]
        end = args[1]
        step = args[2]
    else:
        return 
    start = float(start)
    temp = []
    while start < end:
        temp.append(round(start,6))
        start += step
    return tuple(temp)

print('*** New Range ***')
n = (input("Enter Input : ")).split()
temp = []
for i in n:
    temp.append(float(i))
print(range2(*temp))

