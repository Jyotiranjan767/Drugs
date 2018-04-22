class Employees():

	def __init__(self,  first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = self.first+'.'+self.last+"@gmail.com"

	def full_name(self):
		return "{} {}".format(self.first,self.last)

class Developers(Employees):
	def __init__(self, first, last, pay, prog_name):
		super().__init__(first, last, pay)
		self.prog_name = prog_name

class Manager(Employees):
	def __init__(self, first, last, pay, employees = None):
		super().__init__(first, last, pay)
		if employees is None:
			self.employees = []
		self.employees = employees

	def add_emp(self, emp):
		if  emp not in self.employees:
			self.employees.append(emp)
	
	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print  ('-->', emp.full_name())

dev1 = Developers("corey", 'schafer', 50000,'python')
dev2 = Developers('Kelsi ' ,'Monore', 24240, "'poek")
mgr1  = Manager('luckie', 'jyoti', 241, [dev1])
print(mgr1.email)
mgr1.remove_emp(dev2)
mgr1.add_emp(dev1)
mgr1.add_emp(dev2)
mgr1.print_emps()


