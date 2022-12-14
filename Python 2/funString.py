#จงสร้าง Class funString ที่จะรับพารามิเตอร์เป็น String และเลขคำสั่งโดยมีฟังก์ชันดังต่อไปนี้
#1. หาความยาวของ String
#2. สลับพิมพ์เล็กพิมพ์ใหญ่ใน String (ห้ามใช้คำสั่ง upper และ lower)
#3. Reverse String (ห้ามใช้คำสั่ง reversed)
#4. ลบตัวอักษรที่ปรากฏมาก่อนใน String
class funString():

    def __init__(self,string = ""):
    
        self.s = string

    def size(self) :

        return len(self.s)

    def changeSize(self):
        
        temp = ''
        for ch in self.s:
            if ch.isupper():
                temp += chr(ord(ch) - 65 + 97)  #ord = ch > Ascii  , chr = Ascii > ch
            else:
                temp += chr(ord(ch) + 65 - 97)
        return temp

    def reverse(self):

       return self.s[::-1]

    def deleteSame(self):
        temp = ''
        for ch in self.s:
            if ch not in temp:
                temp += ch          
        
        return temp


str1,str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :    print(res.size())

elif str2 == "2":  print(res.changeSize())

elif str2 == "3" : print(res.reverse())

elif str2 == "4" : print(res.deleteSame())