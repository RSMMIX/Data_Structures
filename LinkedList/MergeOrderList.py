"""
จงเขียนฟังก์ชั่นสำหรับการ Merge LinkList 2 ตัวเข้าด้วยกันโดยห้ามสร้าง Class LinkList จะมีแต่ Class Node ซึ่งเก็บค่า value ของตัวเองและ Node ถัดไป โดยมีฟังก์ชั่นดังนี้

createList() สำหรับการสร้าง LinkList ที่รับ List เข้ามาโดยจะ return Head ของ Linklist

printList() สำหรับการ print LinkList โดยจะรับค่าเป็น head ของ Linklist และจะทำการ print ทุกตัวที่อยู่ใน Linklist ต่อจาก head จนครบทุกตัว

mergeOrderList() สำหรับการ merge linklist 2 ตัวเข้าด้วยกันโดยให้นำมาต่อกันโดยเรียงตามค่า value โดยที่ให้รับ parameter 2 ตัว และจะ return Head ของ Linklist ที่ทำการ merge แล้ว

****ห้ามใช้ sort() หากพบข้อนี้จะไม่ได้คะแนน****

****ห้ามสร้าง Class LinkList****
"""

class node:
    def __init__(self,data = None,next = None ):
        self.data = data
        if next is None :
            self.next = None
        else :
            self.next = next

    def __str__(self):
        return str(self.data)

def createList(l=[]):
    head = node(l[0])
    temp = head
    for i in range(1,len(l)):
        nxt = node(l[i])
        temp.next = nxt
        temp = temp.next
    return head

def printList(H):
    temp = H
    while temp != None:
        print(str(temp),end=" ")
        temp = temp.next
    print()

def mergeOrderesList(p,q):
    dummy = node()
    curr = dummy
    while q != None and p != None :
        if int(p.data) < int(q.data) :
            curr.next = p
            curr = curr.next
            p = p.next
        else:
            curr.next = q
            curr = curr.next
            q = q.next
    if p or q:
        if p != None:
            curr.next = p
        else:
            curr.next = q

    return dummy.next           



#################### FIX comand ####################   
# input only a number save in L1,L2
list1,list2 = input("Enter 2 Lists : ").split()
L1 = list1.split(",")
L2 = list2.split(",")
LL1 = createList(L1)
LL2 = createList(L2)
print('LL1 : ',end='')
printList(LL1)
print('LL2 : ',end='')
printList(LL2)
m = mergeOrderesList(LL1,LL2)
print('Merge Result : ',end='')
printList(m)