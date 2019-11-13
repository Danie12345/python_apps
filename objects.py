class Buildings:
	def __init__(self, base=1, production=1):
		self.produce = base
		self.production = production
	
	def Produce(self):
		return self.produce*self.production