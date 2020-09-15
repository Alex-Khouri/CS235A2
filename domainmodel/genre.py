
class Genre:
	def __init__(self, name=None):
		if (isinstance(name, str) and len(name) > 0):
			self.name = name
		else:
			self.name = None
		self.genre_movies = list()
	
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

	@property
	def movies(self):
		return self.genre_movies
	
	@genre_name.setter
	def genre_name(self, newName):
		self.name = newName

	@movies.setter
	def movies(self, newMovies):
		if isinstance(newMovies, list):
			self.genre_movies = newMovies

	def add_movie(self, newMovie):
		if not newMovie in self.genre_movies:
			self.genre_movies.append(newMovie)
			return True
		else:
			return False

	def remove_movie(self, remMovie):
		if remMovie in self.genre_movies:
			self.genre_movies.remove(remMovie)
			return True
		else:
			return False


if __name__ == "__main__":
	from domainmodel.movie import Movie