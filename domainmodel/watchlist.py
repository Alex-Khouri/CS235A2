from domainmodel.movie import Movie


class Watchlist:
	def __init__(self):
		self.movieList = list()
		self.iterIndex = 0

	def __repr__(self):
		return str(self.movieList)

	def __iter__(self):
		return self

	def __next__(self):
		if self.iterIndex >= len(self.movieList):
			self.iterIndex = 0
			raise StopIteration
		iterValue = self.movieList[self.iterIndex]
		self.iterIndex += 1
		return iterValue

	@property
	def movie_list(self):
		return self.movieList

	@movie_list.setter
	def movie_list(self, newMovieList):
		if isinstance(newMovieList, list):
			self.movieList = newMovieList

	def add_movie(self, movie):
		if isinstance(movie, Movie) and not movie in self.movieList:
			self.movieList.append(movie)

	def remove_movie(self, movie):
		if isinstance(movie, Movie) and movie in self.movieList:
			self.movieList.remove(movie)

	def select_movie_to_watch(self, index):
		if index in range(len(self.movieList)):
			return self.movieList[index]
		else:
			return None

	def size(self):
		return len(self.movieList)

	def first_movie_in_watchlist(self):
		if len(self.movieList) > 0:
			return self.movieList[0]
		else:
			return None


class TestWatchlistMethods:
	def test_init(self):
		watchlist = Watchlist()
		assert str(watchlist) == "[]"

	def test_add_movie(self):
		watchlist = Watchlist()
		watchlist.add_movie(Movie("Moana", 2016))
		watchlist.add_movie(Movie("Ice Age", 2002))
		watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
		test_output = ""
		for movie in watchlist:
			test_output += str(movie) + "\n"
		assert test_output.strip() == "<Movie Moana, 2016>\n<Movie Ice Age, 2002>\n<Movie Guardians of the Galaxy, 2012>"
		assert str(watchlist) == "[<Movie Moana, 2016>, <Movie Ice Age, 2002>, <Movie Guardians of the Galaxy, 2012>]"

	def test_remove_movie(self):
		watchlist = Watchlist()
		watchlist.add_movie(Movie("Moana", 2016))
		watchlist.add_movie(Movie("Ice Age", 2002))
		watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
		watchlist.remove_movie(Movie("Moana", 2016))
		watchlist.remove_movie(Movie("Guardians of the Galaxy", 2012))
		test_output = ""
		for movie in watchlist:
			test_output += str(movie) + "\n"
		assert test_output.strip() == "<Movie Ice Age, 2002>"
		assert str(watchlist) == "[<Movie Ice Age, 2002>]"

	def test_select_movie_to_watch(self):
		watchlist = Watchlist()
		watchlist.add_movie(Movie("Moana", 2016))
		watchlist.add_movie(Movie("Ice Age", 2002))
		watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
		assert str(watchlist.select_movie_to_watch(0)) == "<Movie Moana, 2016>"
		assert str(watchlist.select_movie_to_watch(1)) == "<Movie Ice Age, 2002>"
		assert str(watchlist.select_movie_to_watch(2)) == "<Movie Guardians of the Galaxy, 2012>"
		assert str(watchlist.select_movie_to_watch(3)) == "None"
		assert str(watchlist.select_movie_to_watch(-1)) == "None"

	def test_size(self):
		watchlist = Watchlist()
		assert watchlist.size() == 0
		watchlist.add_movie(Movie("Moana", 2016))
		watchlist.add_movie(Movie("Ice Age", 2002))
		watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
		assert watchlist.size() == 3
		watchlist.remove_movie(Movie("Moana", 2016))
		watchlist.remove_movie(Movie("Guardians of the Galaxy", 2012))
		assert watchlist.size() == 1

	def test_first_movie_in_watchlist(self):
		watchlist = Watchlist()
		watchlist.add_movie(Movie("Moana", 2016))
		watchlist.add_movie(Movie("Ice Age", 2002))
		watchlist.add_movie(Movie("Guardians of the Galaxy", 2012))
		assert str(watchlist.first_movie_in_watchlist()) == "<Movie Moana, 2016>"
		watchlist.remove_movie(Movie("Moana", 2016))
		assert str(watchlist.first_movie_in_watchlist()) == "<Movie Ice Age, 2002>"
		watchlist.remove_movie(Movie("Ice Age", 2002))
		assert str(watchlist.first_movie_in_watchlist()) == "<Movie Guardians of the Galaxy, 2012>"
		watchlist.remove_movie(Movie("Guardians of the Galaxy", 2012))
		assert str(watchlist.first_movie_in_watchlist()) == "None"


testObject = TestWatchlistMethods()
testObject.test_init()
testObject.test_add_movie()
testObject.test_remove_movie()
testObject.test_select_movie_to_watch()
testObject.test_size()
testObject.test_first_movie_in_watchlist()