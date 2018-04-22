from clock1 import Clock
from calender1 import Calendar1

class Calender_clock(Clock, Calendar1):

	def __init__(self,  d, mo, y, h,m,s):
		Clock.__init__(self,h,m,s)
		Calendar1.__init__(self, d, mo, y)

	def tick(self):
		"""advance the clcok by one seconds"""
		previous_hour = self._hours
		Clock.tick(self)
		if(self._hours < previous_hour):
			self.advance()

	def __str__(self):

		return Calendar1.__str__(self)+' , '+Clock.__str__(self)

x = Calender_clock(31,12,2013,23,59,59)
print('one tick from ',x, end = ' ')
x.tick()
print('to ',x)
