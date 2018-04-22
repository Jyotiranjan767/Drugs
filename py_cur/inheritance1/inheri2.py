class Start:
	
	def __init__(self, start, end):

		self.x = start
		self.y = end

	def __str__(self):
		return self.x + " " + self.y

class End(Start):

	def __init__(self, start, end, inB):

		super().__init__(start,end)
		self.inBetween = inB


x = Start('jyoti', 'luckie')
y = End('jyotiEnd ', 'luckie end', '35')

print(x)
print(y)