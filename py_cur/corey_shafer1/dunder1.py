class Empla:

	def __init__(self, first ,last,pay):
		self.first = first
		self.last = last
		self.pay = pay

	def full_name(self):
		return "{} {}".format(self.first,self.last)

	def __repr__(self):
		return "{}.{}@gmail.com".format(self.first,self.last)

	# def __str__(self):
	# 	# return "{} {}".format(self.first, self.last)
	# 	pass

	def __add__(self, other):
		return self.pay +other.pay
	
	def __len__(self):
		return len(self.full_name())

x  = Empla("luckie", 'jyoti',240)
y  = Empla("luckie1", 'jyoti1',242)
print(x)
print(len('luckie'))
print('luckie'.__len__())
print("luckie longetivity",len(x))
print(x+y)

