"""
ให้เรียงลำดับ input ที่รับเข้ามาจากน้อยไปมาก โดยเรียงลำดับจากตัวอักษรที่มีอยู่ในแต่ละ string โดยตัวอักษรจะมีแค่ a - z เท่านั้น และในแต่ละ string จะมี alphabet เพียงแค่ 1 ตัวเท่านั้น

****** ห้ามใช้ Built-in Function ที่เกี่ยวกับ Sort ให้น้องเขียนฟังก์ชัน Sort เอง

"""

lists = input("Enter Input : ").split()
sortByAlphabetList  = []
for i in lists:
    for j in i:
        if j.isalpha():
            sortByAlphabetList.append([j,i])
            break
for i in range(len(sortByAlphabetList)):
    swapped = False
    for j in range(0,len(sortByAlphabetList)-i-1):
        if ord(sortByAlphabetList[j][0]) > ord(sortByAlphabetList[j+1][0]):
            sortByAlphabetList[j],sortByAlphabetList[j+1] = sortByAlphabetList[j+1],sortByAlphabetList[j]
            swapped = True
    if swapped == False:
        break
for i in sortByAlphabetList:
    print(i[1],end=" ")