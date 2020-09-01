from domainmodel.movie import Movie
from domainmodel.review import Review
from domainmodel.watchlist import Watchlist

class User:
	def __init__(self, userName, userPassword):
		self.userName = userName.strip().lower() if isinstance(userName, str) else None
		self.userPassword = userPassword if isinstance(userPassword, str) else None
		self.userWatched = list()
		self.userReviews = list()
		self.userWatchlist = Watchlist()
		self.userTimeWatching = 0

	def __repr__(self):
		return f"<User {self.userName}>"

	def __eq__(self, other):
		return (self.userName == other.userName)

	def __lt__(self, other):
		return (self.userName < other.userName)

	def __hash__(self):
		return hash(self.userName)

	@property
	def user_name(self):
		return self.userName

	@property
	def password(self):
		return self.userPassword

	@property
	def watched_movies(self):
		return self.userWatched

	@property
	def reviews(self):
		return self.userReviews

	@property
	def watchlist(self):
		return self.userWatchlist

	@property
	def time_spent_watching_movies_minutes(self):
		return self.userTimeWatching

	@user_name.setter
	def user_name(self, newName):
		if isinstance(newName, str):
			self.userName = newName.strip().lower()

	@password.setter
	def password(self, newPassword):
		if isinstance(newPassword, str):
			self.userPassword = newPassword

	@watched_movies.setter
	def watched_movies(self, newWatched):
		if isinstance(newWatched, list):
			self.userWatched = newWatched

	@reviews.setter
	def reviews(self, newReviews):
		if isinstance(newReviews, list):
			self.userReviews = newReviews

	@watchlist.setter
	def watchlist(self, newWatchlist):
		if isinstance(newWatchlist, Watchlist):
			self.userWatchlist = newWatchlist

	@time_spent_watching_movies_minutes.setter
	def time_spent_watching_movies_minutes(self, newTimeWatching):
		if isinstance(newTimeWatching, int):
			self.userTimeWatching = newTimeWatching

	def watch_movie(self, movie):
		self.userWatched.append(movie)
		self.userTimeWatching += movie.runtime_minutes

	def add_review(self, review):
		self.userReviews.append(review)