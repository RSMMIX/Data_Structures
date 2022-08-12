n = input('Enter All Bid : ').split()
if len(n) < 2:
    print('not enough bidder')
    exit(0)

bid = []
for i in n:
    bid.append(int(i))

bid.sort(reverse=True)
if bid[0] == bid[1]:
    print('error : have more than one highest bid')
else:
    print(f'winner bid is {bid[0]} need to pay {bid[1]}')
