import time
class Clock(object):
	"""The class is used to simulate a clock"""

	def __init__(self, hours, minutes, seconds):

		self.set_Clock(hours, minutes, seconds)

	def set_Clock(self, hours, minutes, seconds):

		if(type(hours) == int and 0 <= hours and 24 > hours):
			self._hours = hours

		else : raise TypeError("invalid entry for hours!")

		if (type(minutes) == int and 0 <= minutes and 60 > minutes):
			self.__minutes = minutes
		else : raise TypeError("invalid entry for minutes")

		if (type(seconds) == int and 0 <= seconds and 60 > seconds):
			self.__seconds = seconds
		else: raise TypeError("invalid entry for seconds")

	def __str__(self):
		return "{0:02d}:{1:02d}:{2:02d}".format(self._hours,
												self.__minutes,
												self.__seconds)

	def tick(self):
		"""this method lets the clock "tick", this means that the 
		internal time will be advanced by one second"""

		if(self.__seconds==59):
			self.__seconds=0
			if(self.__minutes==59):
				self.__minutes=0
				if(self._hours==23):
					self._hours=0
				else: self._hours+=1
			else: self.__minutes+=1
		else: self.__seconds+=1

if(__name__=="__main__"):
	x = Clock(23,59,59)
	print(x)
	for i in range(x._hours):
		print(i)
		for ii in range(60):
			for iii in range(60):
				x.tick()
				time.sleep(1)
				print(x)
	# print(type(y))
