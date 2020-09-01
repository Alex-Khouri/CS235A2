
class Genre:
	def __init__(self, name=None):
		if (isinstance(name, str) and len(name) > 0):
			self.name = name
		else:
			self.name = None
	
	def __repr__(self):
		return f"<Genre {self.name}>"
	
	def __eq__(self, other):
		return (self.__class__ == other.__class__ and self.name == other.name)
	
	def __lt__(self, other):
		return (self.name < other.name)
	
	def __hash__(self):
		return hash(self.name)
	
	@property
	def genre_name(self):
		return self.name
	
	@genre_name.setter
	def genre_name(self, newName):
		self.name = newName