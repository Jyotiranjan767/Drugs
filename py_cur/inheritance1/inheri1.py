class Person:

	def __init__(self, first, last):
		self.first1 = first
		self.last1 = last 

	def Name(self):
		return self.first1 +" "+ self.last1


class Employee(Person):

	def __init__(self, first, last, dept):
		super().__init__( first, last)
		self.dept1 = dept

	def getEmployee(self):

		return self.Name() + " , " +self.dept1

x = Person("jyoti","luckie ")
y = Employee("luckie emp", 'sa','21414')

print(x.Name())
print(y.getEmployee())


