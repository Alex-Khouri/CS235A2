
class Director:
	def __init__(self, name=None):
		if (isinstance(name, str) and len(name) > 0):
			self.name = name
		else:
			self.name = None
	
	def __repr__(self):
		return f"<Director {self.name}>"
	
	def __eq__(self, other):
		return (self.__class__ == other.__class__ and self.name == other.name)
	
	def __lt__(self, other):
		return (self.name < other.name)
	
	def __hash__(self):
		return hash(self.name)
	
	@property
	def director_full_name(self):
		return self.name
	
	@director_full_name.setter
	def director_full_name(self, newName):
		self.name = newName


class TestDirectorMethods:

	def test_init(self):
		director1 = Director("Taika Waititi")
		assert repr(director1) == "<Director Taika Waititi>"
		director2 = Director("")
		assert director2.director_full_name is None
		director3 = Director(42)
		assert director3.director_full_name is None