print('*** Fun with Drawing ***')

n = int(input('Enter input : '))

for y in range((3*n)-2):
    
    for x in range((4*n)-3): 
        line1 = y == n-x-1
    
        line2 = x == y+n-1 and y < n

        line3 = y == 3*n-3-x and y < n

        line4 = x == y+(n-1)*3

        line5 = y == (n-1)*5-x

        line6 = x == y-(n-1) 

        area1 = y > n-x-1 and x < y+n-1 and y < n

        area2 = y > 3*n-3-x and x < y+(n-1)*3 and y < n 

        area3 = y < (n-1)*5-x and x > y-(n-1) and y >= n

        if  line1 or line2 or line3 or line4 or line5 or line6:
            print('*',end='')

        elif area1 or area2 or area3:
            print('+',end='')

        else:
            print('.',end='')

    print()
