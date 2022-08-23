class Stack:
    def __init__(self,lst = None):
        if lst == None:
            self.items = []
        else:
            self.items = lst

    def push(self,i):
        self.items.append(i)
           
    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []
        
    def size(self):
        return (len(self.items))

s = Stack()
n = input('Enter Input : ').split(',')
for i in n:
    cmd = i.split()
    if cmd[0] == 'A':
        s.push(int(cmd[1]))
        print(f'Add = {cmd[1]} and Size = {s.size()}') 

    else:
        if s.isEmpty():
            print(-1)

        else:
            print(f'Pop = {s.pop()} and Index = {s.size()}')

if not s.isEmpty():
    print('Value in Stack =',*s.items)
else :
    print('Value in Stack = Empty')
