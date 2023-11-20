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

num = ""
for i in range(10):
    if i <= 5 and (i % 2)==0:
        continue
    elif i is 7 or i is 10:
        continue
    else:
        num = str(i) + num
print(num)