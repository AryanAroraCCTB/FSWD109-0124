# • An Employee has attributes name, age, and salary.
class Employee():
	def __init__(self, name, age, salary):
		self.name = name
		self.age = age
		self.salary = salary

	def __str__(self):
		return f'Employee {self.name} of {self.age} years old with {self.salary} salary / month'
	
	def calcTotalEarnings(self):
		return self.salary
	
	def setSalary(self, salary):
		self.salary = salary

# • A Manager is an Employee with an additional attribute department.
class Manager(Employee):
	def __init__(self, name, age, salary, department):
		super().__init__(name, age, salary)
		self.department = department

	def __str__(self):
		return (super().__str__()).replace('Employee', 'Manager') + f' in department {self.department}'
	
	def calcTotalEarnings(self):
		pass

# • An Executive is a Manager with an additional attribute bonus.
class Executive(Manager):
	def __init__(self, name, age, salary, department, bonus):
		super().__init__(name, age, salary, department)
		self.bonus = bonus

	def __str__(self):
		return (super().__str__()).replace('Manager', 'Executive') + f' with bonus of {self.bonus} / year'
	
	def calcTotalEarnings(self):
		return super().calcTotalEarnings() + self.bonus


e1 = Employee('e1', 20, 1000)
m1 = Manager('m1', 21, 1100, 'HR')
ex1 = Executive('ex1', 22, 1200, 'HR', 100)

print(e1)
print(m1)
print(ex1)

print(isinstance(e1, Employee)) # True
print(isinstance(m1, Manager)) # True
print(isinstance(ex1, Executive)) # True

print(isinstance(m1, Employee))
print(isinstance(ex1, Manager))

print(isinstance(m1, Executive))