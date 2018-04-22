class Animal:

	def __init__(self, name, stay, food):

		self.name = name
		self.stay = stay
		self.food = food
	
	def __str__(self):
		return self.name + ' stays in ' +self.stay+" eats "+self.food

class Lion(Animal):

	def __init__(self, name, stay, food, sound):
		super().__init__(name, stay, food)
		self.sound = sound

	def __str__(self):
		return super().__str__() + " and "+self.sound + " basically"


x = Animal("animal", "stay", "food")
y = Lion("lion", 'jungle','meats','roars')

print(x)
print(y)

