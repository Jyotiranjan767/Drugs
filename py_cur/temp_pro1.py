class Celcius :

	def __init__(self, temperature = 0):
		# self.set_temp(temperature)
		self.temp = temperature

	def get_temp(self):
		print("getting values")
		print( self.temperature )



	def to_farenheit(self):
		return (self.temperature * 1.8)+32



	def set_temp(self, value ):

		if(value < -273):
			# self.temp = 0
			raise ValueError ("temperature below -273 is not possible !")
		print("setting values ")
		self.temp = value

		# elif(temp > 1000):
		# 	self.temp = 1000

		# else: self.temperature = temp
	temp_property = (get_temp, set_temp)

man = Celcius(-13311)
man.temperature = -1238
man.get_temp()
#print(man.temperature)


