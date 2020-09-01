
class Actor:
	def __init__(self, name=None):
		if (isinstance(name, str) and len(name) > 0):
			self.name = name
		else:
			self.name = None
		self.colleagues = []
	
	def __repr__(self):
		return f"<Actor {self.name}>"
	
	def __eq__(self, other):
		return (self.__class__ == other.__class__ and self.name == other.name)
	
	def __lt__(self, other):
		return (self.name < other.name)
	
	def __hash__(self):
		return hash(self.name)
	
	@property
	def actor_full_name(self):
		return self.name
	
	@actor_full_name.setter
	def actor_full_name(self, newName):
		self.name = newName
		
	def add_actor_colleague(self, colleague):
		self.colleagues.append(colleague)
		
	def check_if_this_actor_worked_with(self, colleague):
		return (colleague in self.colleagues)