class A:
	def m(self):
		print("class A is called")

class B:
	def m(self):
		print("class B is called")
	# pass

class C:
	def m(self):
		print("class C is called")

class D(B, C):
	def m(self):
		print("class D is called")
		B.m(self)
		C.m(self)
		A.m(self)


x = D()
B.m(x)
C.m(x)
A.m(x)
# D.m(x)
x.m()
 
