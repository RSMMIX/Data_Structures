def Rshift(num,shift):
    return num // 2**shift

n,s = input("Enter number and shiftcount : ").split()

print(Rshift(int(n),int(s)))




