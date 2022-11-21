"""
ให้น้องๆเขียนการทำ Rehashing ด้วยเงื่อนไขดังนี้
1. Table เต็มถึงระดับที่กำหนด ( Threshold (%) )
2. เมื่อเกิดการ Collision ถึงจำนวนที่กำหนด

หากเกิดการ Rehashing ให้ทำการขยาย Table เป็นค่า prime ถัดไปที่มากกว่าเดิม 2 เท่า เช่น หาก Table ตอนแรกมีขนาด 4 และเกิดการ Rehashing  ตัว Table ใหม่จะมีขนาดเป็น 11 เนื่องจาก 2 เท่าของ 4 คือ 8  และค่า prime ที่มากกว่า 8 และใกล้ 8 มากที่สุดคือ 11

การ Hash หากเกิดการ Collision ให้ใช้ Quadratic Probing ในการแก้ปัญหา Collision

อธิบาย Input
แบ่ง Data เป็น 2 ชุดด้วย /
    -   ด้านซ้ายหมายถึง ขนาดของ Table , MaxCollision และ Threshold (สูงสุด 100 %) ตามลำดับ
    -   ด้านขวาหมายถึง Data n ชุด โดย Data แต่ละชุดแบ่งด้วย spacebar และ Data แต่ละตัวเป็นจำนวนเต็มศูนย์หรือบวกเท่านั้น และไม่มี Data ซ้ำกันเด็ดขาด


"""



class hash:
     def __init__(self,size,maxCol,threshold):
          self.table = [None]*size
          self.size = size
          self.maxCol = maxCol
          self.threshold = threshold

     def insert(self,data):
          if self.isfull() :
               print("****** Data over threshold - Rehash !!! ******")
               return False
          else:
               index = data % self.size

               if self.table[index] == None:
                    self.table[index] = data
               else:
                    col = 0
                    print(f'collision number {col+1} at {index}')
                    while True:
                         col += 1
                         newIndex = ( index + col * col ) % self.size
                         if self.maxCol <= col:
                              print("****** Max collision - Rehash !!! ******")
                              return False
                         if self.table[newIndex] == None:
                              self.table[newIndex] = data
                              break
                         print(f'collision number {col+1} at {newIndex}')
               return True

     def isfull(self):
          full = int(self.size * self.threshold / 100)
          count = 0
          for data in self.table:
               if data is not None:
                    count += 1
          if count >= full:
               return True
          return False

     def nextPrime(self,value):
          while value:
               value += 1
               for i in range(2,value):
                    if value % i == 0:
                         break
                    if i == value-1:
                         return value

     def printHashTable(self):
          for i in range(self.size):
               print(f'#{i+1}'+ " " * (7-len(str(i+1))) + f'{self.table[i]}')
          print("----------------------------------------")

print(" ***** Rehashing *****")
inp = input("Enter Input : ").split("/")

size, maxcol, threshold = map(int, inp[0].split())
data = list(map(int, inp[1].split()))
H = hash(size,maxcol,threshold)

print("Initial Table :")
H.printHashTable()

lastadd = -1
notall = True

while notall:
     for i in range(len(data)):
          if i >= lastadd + 1:
               print(f'Add : {data[i]}')
          if not H.insert(data[i]):
               H = hash(H.nextPrime(H.size * 2),maxcol,threshold)
               lastadd = i
               break
          else:
               if i >= lastadd:
                    H.printHashTable()
          if i == len(data)-1:
               notall = False