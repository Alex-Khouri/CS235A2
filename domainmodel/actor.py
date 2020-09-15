
class Actor:
	def __init__(self, name=None):
		if (isinstance(name, str) and len(name) > 0):
			self.name = name
		else:
			self.name = None
		self.actor_movies = list()
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

	@property
	def movies(self):
		return self.actor_movies
	
	@actor_full_name.setter
	def actor_full_name(self, newName):
		self.name = newName

	@movies.setter
	def movies(self, newMovies):
		if isinstance(newMovies, list):
			self.actor_movies = newMovies
		
	def add_actor_colleague(self, colleague):
		self.colleagues.append(colleague)

	def add_movie(self, newMovie):
		if not newMovie in self.actor_movies:
			self.actor_movies.append(newMovie)
			return True
		else:
			return False
		
	def check_if_this_actor_worked_with(self, colleague):
		return colleague in self.colleagues

	def remove_movie(self, remMovie):
		if remMovie in self.actor_movies:
			self.actor_movies.remove(remMovie)
			return True
		else:
			return False


if __name__ == "__main__":
	from domainmodel.movie import Movie