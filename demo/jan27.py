class Car:
	def __init__(self, color: str, num_wheels: int):
		if not color or not num_wheels:
			raise ValueError("Invalid values provided during instantiation")
		if num_wheels <= 0:
			raise ValueError("Invalid number of wheels")
		
		self.color = color
		self.plate = 'VAN123'
		self.number_of_wheels = num_wheels

	def __str__(self):
		return f'{self.color} Car with {self.number_of_wheels} wheels'

	def increase_wheels(self):
		print(self.color) # "this" in js
		self.number_of_wheels =+ 1

c1 = Car("red", 3)
print(c1.color, c1.number_of_wheels)

c2 = Car("blue", 4)
print(c2.color, c2.number_of_wheels)

c3 = Car("yellow", 1)
print(c3.color, c3.number_of_wheels)

print(c1)
print(c2)
print(c3)

c1.increase_wheels()
c2.increase_wheels()
c3.increase_wheels()

del c1.plate # deleted the attribute
if not hasattr(c1, "plate"):
	print("C1 does not have a plate")

setattr(c1, "plate", "NEWVAN123") # c1.plate = "NEWVAN123"
print(c1.plate)

x = getattr(c1, "plate") # c1.plate
print(x)

# ---
y = "color"
x = "orange"

c2.y = x # this will not work
print(c2)

setattr(c2, y, x)
print(c2)
print(getattr(c2, y))


# ----
print('-----------------')
# PERSON: PARENT / BASE CLASS
# STUDENT, TEACHER: CHILD / DERIVED CLASS
class Person:
	def __init__(self, fname: str, lname: str, age: int):
		self.fname = fname
		self.lname = lname
		self.age = age

	def __str__(self):
		return f'Hi, I am {self.fname}{self.lname} and I am {self.age} years old.'
	
class Student(Person):
	pass

class Teacher(Person):
	def __init__(self, fname, lname, age, id: str):
		super().__init__(fname, lname, age)
		self.id = id

	def __str__(self):
		return super().__str__() + f' My ID is {self.id}'

p1 = Person('p1', '.0', 25)
print(p1)

s1 = Student('s1', '.0', 25)
print(s1)

t1 = Teacher('t1', '.0', 27, 'ABC123')
print(t1)

# ------
print('-----------------')
class A:
	def __str__(self):
		return f'In class A'
	
class B(A):
	def __str__(self):
		return f'In class B'
	
class C(A):
	pass

class D:
	def __str__(self):
		return f'In class D'
	
class E(A, D):
	pass

class F(D, A):
	pass

class G(C, D):
	pass

o1 = A()
o2 = B()
o3 = C()
o4 = D()
o5 = E()
o6 = F()
o7 = G()

print(o1) # In class A
print(o2) # In class B
print(o3) # In class A
print(o4) # In class D
print(o5) # In class A
print(o6) # In class D
print(o7) # In class A
	
# ------
print('-----------------')

def test_function():
	try:
		print(test)		
		# 1: update username: DONE

		# 2: update email: FAILS
	except:
		# UNDO EVERYTHING: 1 & 2
		print("Error happened")

test_function()
print("hi")




