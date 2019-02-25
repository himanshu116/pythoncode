class pp:
	def __init__(self,pages):
		self.pages=pages
	def __add__(self,other):
		print(id(self))
		return self.pages+other.pages
a1=pp(200)
a2=pp(300)
a3=9+10
print(a3)
print(id(a1))
print("total no. of pages :",a1+a2)