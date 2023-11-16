coupon = 0
money = 20000
coffee = 3500

while money > coffee:
	if coupon < 4:
		money = money - coffee
		print(money)
		coupon += 1
	else:
		money +=2800
		coupon = 0
print(money)