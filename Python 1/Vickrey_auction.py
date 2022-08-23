#จงสร้าง vickrey auction แบบจำลอง
#Vickrey auction คือการประมวลที่ผู้ที่จะชนะการประมูล คือ ผู้ที่ยื่นซองเสนอราคาสูงที่สุด แต่จะจ่ายจริงในราคาที่สูงเป็นอันดับสองรองลงมา
#
#word
#"Enter All Bid : "
#"not enough bidder"
#"error : have more than one highest bid"
#"winner bid is $ need to pay $"

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
