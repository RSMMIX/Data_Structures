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

inp_n, inp_m = input('Enter Input (Normal, Mirror) : ').split()

inp_m = inp_m[::-1]