import random

print('Hello World!')

a = 10
b = 11
print(a + b)

a = '10'
b = '11'
print(a + b) # 1011

# TODO: 
# FIXME:

testGlobal = 11

def total_sales(sales: list[int]) -> int:
	global testGlobal
	testGlobal = testGlobal + 1
	print(testGlobal) # 10
	return sum(sales)


total_sales([10])
print(testGlobal) # 10


fruits = ['apple', 'banana', 'cherry']
x = fruits[0]
y = fruits[1]
z = fruits[2]


print(type('test'))

z = range(6)
print(z)
for x in z:
	print(x)


x = {
	"name": "John",
	"age": 36,
	"country": "Norway"
}
print(type(x))
print(x["name"])

x = "test"



name = "John" # name[0]
# name = ['j', 'o', 'h', 'n'] # name[0]

print(len(name))

letter = 'x'
hasLetter = letter in name
print(hasLetter)

if hasLetter:
	print('yes')
else:
	print('no')


name = "John" # J: 0, o: 1, h: 2, n: 3
x = name[0:2] # Jo
print(x)

y = name[2:]

z = name[::2]
print(z)

a = "  te  st  "
a = a.strip().lower().replace(" ", "")
print(a)

hobbies = "basketball,soccer,tennis"
hobbies = hobbies.split(",")
print(hobbies)