from datafilereaders.movie_file_csv_reader import MovieFileCSVReader


class MemoryRepo:

	def __init__(self, file_name):
		csvReader = MovieFileCSVReader(file_name)
		csvReader.read_csv_file()
		self.movies = csvReader.dataset_of_movies()
		self.actors = csvReader.dataset_of_actors()
		self.directors = csvReader.dataset_of_directors()
		self.genres = csvReader.dataset_of_genres()

	@property
	def movies(self):
		return self.movies

	@property
	def actors(self):
		return self.actors

	@property
	def directors(self):
		return self.directors

	@property
	def genres(self):
		return self.genres

	@movies.setter
	def movies(self, newMovies):
		if isinstance(newMovies, list):
			self.movies = newMovies

	@actors.setter
	def actors(self, newActors):
		if isinstance(newActors, set):
			self.actors = newActors

	@directors.setter
	def directors(self, newDirectors):
		if isinstance(newDirectors, set):
			self.directors = newDirectors

	@genres.setter
	def genres(self, newGenres):
		if isinstance(newGenres, set):
			self.genres = newGenres