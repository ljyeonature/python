# a = '20'
# b = '4'
# print(type(float(a / b)))

# a = '3'
# b = float(a)
# print(b ** int(a))
#
# a = "3.5"
# b = "1.5"
# print(a + b)
#
# a = "3.5"
# b = 4
# print(a * b)
# print('======================')
# a = 10.6
# b = 10.5
# print(a * b)
#
# print(type(a + b))


a = 3.5
b = int(3.5)

print(a**((a // b) * 2))
print(((a - b) * a) // b)
b = (((a - b) * a) % b)
print(b)
print((a * 4) % (b * 4))


fact = "Python is funny"
print(str(fact.count('n') + fact.find('n') + fact.rfind('n')))

result = "CODE2018"
print("{0},{1}".format(result[-1], result[-2]))

a = "abcd e f g"
b = a.split()
c = (a[:3][0])
d = (b[:3][0][0])
print(c + d)

a = '10'
b = '5-2'.split('-')[1]
print(a * 3 + b)

print("="*50)
a = [0, 1, 2, 3, 4]
print(a[:3], a[:-3])

a = [0, 1, 2, 3, 4]
print(a[::-1])

first = ["egg", "salad", "bread", "soup", "canafe"]
second = ["fish", "lamb", "pork", "beef", "chicken"]
third = ["apple", "banana", "orange", "grape", "mango"]
order = [first, second, third]
john = [order[0][:-2], second[1::3], third[0]]
del john[2]
john.extend([order[2][0:1]])
print(john)

list_a = [3, 2, 1, 4]
list_b = list_a.sort()
print(list_a, list_b)

fruits = ['apple', 'banana', 'cherry', 'grape', 'orange', 'strawberry', 'melon']
print(fruits[-3:], fruits[1::3])

num = [1, 2, 3, 4]
print(num * 2)

list_a = ['Hankook', 'University', 'is', 'an', 'academic', 'institute', 'located', 'in', 'South Korea']
list_b=[ ]
for i in range(len(list_a)):
    if i % 2 != 1:
        list_b.append(list_a[i])

print(list_b)

# admission_year = input("입학 연도를 입력하세요: ")
# print(type(admission_year))

country = ["Korea", "Japan", "China"]
capital = ["Seoul", "Tokyo", "Beijing"]
index = [1, 2, 3]
country.append(capital)
print(country[3][1])
country[3][1] = index[1:]
print(country)


a = [1, 2, 3, 5]
b = ['a', 'b', 'c','d','e']
a.append('g')
b.append(6)
print('g' in b, len(b))

num = [1, 2, 3, 4]
print(num * 2)

fruits = ['apple', 'banana', 'cherry', 'grape', 'orange', 'strawberry', 'melon']
print(fruits[-3:], fruits[1::3])
print(fruits[1::3])

list_a = [3, 2, 1, 4]
list_a.sort()
list_b = list_a.sort()
print(list_b)
print(list_a, list_b)