class Circle:
	def __init__(self, radius=10, x=0, y=0):
		self.radius=radius
		self.x=x
		self.y=y
	
	def values(self):
		print("Radius=",self.radius, " x=", self.x, " y=", self.y)

	def changevalues(self,radius,x,y):
		self.x=x
		self.y=y
		self.radius=radius
