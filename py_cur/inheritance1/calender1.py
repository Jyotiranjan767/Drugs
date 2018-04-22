class Calendar1:
	"""the class Calendar implements Calendar"""

	months = (31,28,31,30,31,30,31,31,30,31,30,31)
	data_style = "British"

	@staticmethod
	def leap_year(year):
		if not year % 4 == 0:
			return False
		elif not year % 100 == 0:
			return True
		elif not year % 400 == 0:
			return False 
		else : return True 

	def __init__(self, d, m, y):

		self.set_calendar(d, m, y)

	def set_calendar(self, d, m, y):
		"""d,m,y have to be integer and year has to be a four digit number """
		if(type(d) == int and type(m) == int and type(y) == int ):
			self.__days= d
			self.__months= m
			self.__years = y
		else : raise TypeError("d, m , y have to be integers!@")

	def __str__(self):
		if Calendar1.data_style == "British":
			return "{0:02d}:{1:02d}:{2:4d}".format(self.__days,
													self.__months,
													self.__years)

	def advance(self):
		"""this method advances to the next date"""
		max_days = Calendar1.months[self.__months-1]
		if(self.__months == 2 and Calendar1.leap_year(self.__years)):
			max_days += 1

		if(self.__days == max_days):
			self.__days = 1
			if(self.__months == 12):
				self.__months = 1
				self.__years += 1
			else : self.__months += 1
		else : self.__days += 1


if (__name__ == '__main__'):
	x = Calendar1(31, 12, 2014)
	print(x, end = ' ')
	x.advance()
	print("after applying advances ", x)
	x = Calendar1(28, 2, 2013)
	x.advance()
	print(x)


