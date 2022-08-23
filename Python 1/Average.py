print(' *** Wind classification ***')

n = input('Enter wind speed (km/h) : ')

n = float(n)

if 0 <= n < 52 :
    print('Wind classification is Breeze.')

elif 52 <= n < 56:
    print('Wind classification is Depression.')

elif 56 <= n < 102:
    print('Wind classification is Tropical Storm.')

elif 102 <= n < 209:
    print('Wind classification is Typhoon.')


elif n >= 209:
    print('Wind classification is Super Typhoon.')



#โจทย์: จงเขียนโปรแกรมรับความเร็วลมเฉลี่ยใน 10 นาที และแสดงผลระดับพายุที่เกิดขึ้น จากการจัดแบ่งความเร็วลมดังนี้
#
#		Speed (km/h)		ระดับพายุ
#			0-51.99			Breeze
#			52.00-55.99		Depression
#			56.00-101.99	        Tropical Storm
#			102.00-208.99	        Typhoon
#			>= 209			Super Typhoon
