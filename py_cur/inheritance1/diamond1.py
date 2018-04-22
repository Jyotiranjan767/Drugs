class A(object):
	def m(self):
		print("class A is called")

class B(A):
	def m(self):
		print("class B is called")
	# pass

class C(A):
	def m(self):
		print("class C is called")

class D(A, B, C):
	pass

x = D()
x.m()

 
