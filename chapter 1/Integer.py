print(' *** Summation of each digit ***')
sum = 0
n = (input('Enter a positive number : '))
for i in n:
    i = int(i)
    sum += i
print('Summation of each digit = ',sum)