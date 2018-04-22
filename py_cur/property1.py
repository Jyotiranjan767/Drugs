
class P:

	def __init__(self, x):
		# self.__x = x
		self.set_x(x)


	def get_x(self):
		return self.__x

	def set_x(self, x):
		self.__x = x

p1 = P(12)
p2 = P(23) 
print(p1.get_x() + p2.get_x())
