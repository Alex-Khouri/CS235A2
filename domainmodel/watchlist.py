

class Watchlist:
	def __init__(self):
		self.watchlist_movie_list = list()
		self.iterIndex = 0

	def __repr__(self):
		return str(self.watchlist_movie_list)

	def __iter__(self):
		return self

	def __next__(self):
		if self.iterIndex >= len(self.watchlist_movie_list):
			self.iterIndex = 0
			raise StopIteration
		iterValue = self.watchlist_movie_list[self.iterIndex]
		self.iterIndex += 1
		return iterValue

	@property
	def movie_list(self):
		return self.watchlist_movie_list

	@movie_list.setter
	def movie_list(self, newMovieList):
		if isinstance(newMovieList, list):
			self.watchlist_movie_list = newMovieList

	def add_movie(self, movie):
		if not movie in self.watchlist_movie_list:
			self.watchlist_movie_list.append(movie)
			return True
		else:
			return False

	def remove_movie(self, movie):
		if movie in self.watchlist_movie_list:
			self.watchlist_movie_list.remove(movie)
			return True
		else:
			return False

	def select_movie_to_watch(self, index):
		if index in range(len(self.watchlist_movie_list)):
			return self.watchlist_movie_list[index]
		else:
			return None

	def size(self):
		return len(self.watchlist_movie_list)

	def first_movie_in_watchlist(self):
		if len(self.watchlist_movie_list) > 0:
			return self.watchlist_movie_list[0]
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


if __name__ == "__main__":
	from domainmodel.movie import Movie
	testObject = TestWatchlistMethods()
	testObject.test_init()
	testObject.test_add_movie()
	testObject.test_remove_movie()
	testObject.test_select_movie_to_watch()
	testObject.test_size()
	testObject.test_first_movie_in_watchlist()