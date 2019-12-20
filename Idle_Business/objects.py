class Building:
	def __init__(self, base=1, production=1):
		self.produce = base
		self.production = production
	
	def Produce(self):
		return self.produce*self.production

class Worker(Building):
	def __init__(self):
		super().__init__()
		pass

if __name__ == "__main__":
	manny = Worker()