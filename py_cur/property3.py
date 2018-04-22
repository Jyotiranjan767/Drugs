class Making_private_method :

	def __init__(self, arg):
		self.__set_arg(arg)

	def __get_arg(self):
		return self.__arg

	def __set_arg(self, arg):

		if(arg < 0):
			self.__arg = 0

		elif(arg > 1000):
			self.__arg = 1000

		else : self.__arg = arg

x = property(__get_arg __set_arg)

p = Making_private_method(-1200)
p.__set_arg(1252)
print(p.__get_arg())
print()

