class Emplo1():

	def __init__(self, first, last):
		self.first = first
		self.last = last
		# self.email = self.first+ '.' + self.last+'@gmail.com'

	@property
	def email(self):
		return '{}.{}@gmail.com'.format(self.first,self.last)
	@property
	def full_name(self):
		return '{1} {0}'.format(self.first,self.last)
	@full_name.setter
	def full_name(self,name):
		first, last = name.split(' ')
		self.first = first
		self.last = last
	@full_name.deleter
	def full_name(self):
		print('deleting name , wait and deleted')
		self.first = None
		self.last = None

x = Emplo1('luckie','jyoti')
x.first = 'fukcie'
x.full_name = "jyoti sla"
print(x.first)
del x.full_name
print(x.email)
print(x.full_name)
