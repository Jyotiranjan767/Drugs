class Robot:

	counter = 0
	def __init__(self, name ):
		self.namee = name
	def say_hello(self):
		return "hi I'm "+self.namee

def rob_init(self, name):
		self.name = name 

Robot2 = type("Robot2",(),
				{
					'counter' : 0,
					'__init__': rob_init,
					'say_hello' : lambda self : "Hi I'am "+self.name
				})

x = Robot2("jyoti")
print(x.say_hello())
y = Robot("luckie")
print(y.say_hello())

print('x ,',x.__dict__)
print('y ,',y.__dict__)