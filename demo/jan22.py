# ---
# Get all students from the database
def getStudents():
	return []
	# return ['s1', 's2', 's3', 's4', 's5']

students = getStudents() # []

if students:
	print("Students are present")

if not students:
	print("No students are present")


# ---
a = 10
print(type(a))
print(isinstance(a, int))
print(isinstance(a, float))


def add(a: int, b: int) -> int:
	isAInt = isinstance(a, int) # True
	isBInt = isinstance(b, int) # True

	hasInValidValues = not isAInt or not isBInt
	if hasInValidValues:
		print('Invalid Values Provided')
		return -1
	return a + b

print(add(10, 20))
# print(add(10, 20.5))
# print(add(10, '20'))


# --
a = 10
b = 11

a += 1 # a = a + 1

a = 2
a **= 2 # a = a ** 2 = 2**2 = 4

# ---
numbers = [1,2,3,4]

for x in numbers:
	print(x)

# --

numbers = [1,2,3,4]
more_numbers = [5,6,7,8]

numbers.extend(more_numbers)

print(numbers)

# ---
students = ['s1', 's2', 's3', 's3', 's4', 's5']
students = ['s1', 's2', 's3', 's3',  's3', 's3', 's4', 's5']
students = ['s1', 's2', 's3', 's3',  's3', 's3', 's3', 's3', 's4', 's5']
students = ['s1', 's2', 's4', 's5']

def removeStudentFromList(students: list[str], name: str) -> list[str]:
	# one of many ways
	num = students.count(name)
	for x in range(0, num):
		students.remove(name)

	# two of many ways
	new_students = []
	for s in students:
		if s != name:
			new_students.append(s)

	# three of many ways
	while name in students:
		students.remove(name)

	return students

x = removeStudentFromList(students, 's3') # ['s1', 's2', 's4', 's5']
print(x)