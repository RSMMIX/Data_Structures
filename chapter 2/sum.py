from itertools import combinations

n = [int(i) for i in input('Enter Your List : ').split()]

    
if len(n) < 3:
    print(f'Array Input Length Must More Than 2')
    exit(0)

temp = []

for comb in combinations(n,3):
    comb = sorted(comb)
    if sum(comb) == 0 and comb not in temp:
        temp.append(comb)

print(temp)

