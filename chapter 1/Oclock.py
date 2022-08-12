#รับจำนวนเต็ม 3 จำนวนจากแป้นพิมพ์เก็บในตัวแปร h, m และ s ซึ่งแทนจำนวน ชั่วโมง นาที และ วินาที
print('*** Converting hh.mm.ss to seconds ***')

n = input('Enter hh mm ss : ').split()

s = (int(n[0])*3600)+(int(n[1])*60)+(int(n[2]))

if int(n[0]) < 0:
    print(f'hh({n[0]}) is invalid!')

elif not (0 <= int(n[1]) < 60):
    print(f'mm({n[1]}) is invalid!')

elif int(n[2]) < 0:
    print(f'ss({n[2]}) is invalid!')

else :
    print(f'{int(n[0]):02}:{int(n[1]):02}:{int(n[2]):02} = {s:,} seconds')
 