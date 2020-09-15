from datafilereaders.movie_file_csv_reader import MovieFileCSVReader


class MemoryRepo:

	def __init__(self, file_name):
		csvReader = MovieFileCSVReader(file_name)
		csvReader.read_csv_file()
		self.repo_movies = csvReader.dataset_of_movies
		self.repo_actors = csvReader.dataset_of_actors
		self.repo_directors = csvReader.dataset_of_directors
		self.repo_genres = csvReader.dataset_of_genres
		self.repo_users = list()

	@property
	def movies(self):
		return self.repo_movies

	@property
	def actors(self):
		return self.repo_actors

	@property
	def directors(self):
		return self.repo_directors

	@property
	def genres(self):
		return self.repo_genres

	@property
	def users(self):
		return self.repo_users

	@movies.setter
	def movies(self, newMovies):
		if isinstance(newMovies, list):
			self.repo_movies = newMovies

	@actors.setter
	def actors(self, newActors):
		if isinstance(newActors, set):
			self.repo_actors = newActors

	@directors.setter
	def directors(self, newDirectors):
		if isinstance(newDirectors, set):
			self.repo_directors = newDirectors

	@genres.setter
	def genres(self, newGenres):
		if isinstance(newGenres, set):
			self.repo_genres = newGenres

	@users.setter
	def users(self, newUsers):
		if isinstance(newUsers, list):
			self.repo_users = newUsers

	def add_user(self, newUser):
		if newUser not in self.repo_users and newUser.user_name not in [user.user_name for user in self.repo_users]:
			self.repo_users.append(newUser)
			return True
		else:
			return False

	def remove_user(self, remUser):
		if remUser in self.repo_users:
			self.repo_users.remove(remUser)
			return True
		else:
			return False

	def get_user(self, username):
		for user in self.repo_users:
			if user.user_name == username:
				return user
		return None


class TestMemoryRepo:

	def test_init(self):
		repo = MemoryRepo('datafiles/Data1000Movies.csv')


if __name__ == "__main__":
	from domainmodel.movie import Movie
	from domainmodel.actor import Actor
	from domainmodel.genre import Genre
	from domainmodel.director import Director