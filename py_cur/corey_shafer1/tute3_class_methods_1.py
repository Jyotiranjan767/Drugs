class Employee():

	raise_amount = 1.04

	def  __init__(self, first, last, pay):
		self.first = first
		self.last  = last
		self.email = self.first,'.',self.last,'@gmail.com'
		self.pay = pay

	def full_name(self):
		return "{} {}".format(self.first,self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

	@classmethod
	def set_raise_amount(cls,amount):
		cls.raise_amount =  amount
	
	@classmethod
	def set_custom_init(cls, emp_str):
		first,last,pay = emp_str.split('-')
		return cls(first,last,pay)
	
	@staticmethod
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True

emp_1 = Employee('samantha ', 'saint ',248)
emp_2  = Employee('Abigail', "Mac", 242)

emp_str_1 = 'nicole-aniston-4248'
emp_str_2 = 'Nikki-Benz-2841'
emp_str_3 = "Blaire-Williams-2824"


new_emp_1 = Employee.set_custom_init(emp_str_3)
print(new_emp_1.email)
print(emp_1.email)
print(Employee.full_name(emp_2))
emp_1.set_raise_amount(10)
print(Employee.raise_amount)

import datetime
todays_date =datetime.date(2016, 7, 11)
print(Employee.is_workday(todays_date))