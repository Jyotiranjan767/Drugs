class Pr2:

	def __init__(self, arg):
		self.set_arg(arg)

	def get_arg(self):
		return self.__arg

	def set_arg(self, arg):

		if(arg > 1000):
			self.__arg = 1000
		
		elif(arg < 0):
			self.__arg = 0

		else :self.__arg = arg

p = Pr2(1400)
p.set_arg(-243)

print(p.get_arg())

		
			

