from domainmodel.watchlist import Watchlist

class User:
	def __init__(self, userName, userPassword):
		self.user_name = userName.strip().lower() if isinstance(userName, str) else None
		self.user_password = userPassword if isinstance(userPassword, str) else None
		self.user_watched = list()
		self.user_reviews = list()
		self.user_watchlist = Watchlist()
		self.user_timewatching = 0

	def __repr__(self):
		return f"<User {self.user_name}>"

	def __eq__(self, other):
		return self.user_name == other.userName

	def __lt__(self, other):
		return self.user_name < other.userName

	def __hash__(self):
		return hash(self.user_name)

	@property
	def user_name(self):
		return self.user_name

	@property
	def password(self):
		return self.user_password

	@property
	def watched_movies(self):
		return self.user_watched

	@property
	def reviews(self):
		return self.user_reviews

	@property
	def watchlist(self):
		return self.user_watchlist

	@property
	def time_spent_watching_movies_minutes(self):
		return self.user_timewatching

	@property
	def comments(self):
		return self.user_comments

	@user_name.setter
	def user_name(self, newName):
		if isinstance(newName, str):
			self.user_name = newName.strip().lower()

	@password.setter
	def password(self, newPassword):
		if isinstance(newPassword, str):
			self.user_password = newPassword

	@watched_movies.setter
	def watched_movies(self, newWatched):
		if isinstance(newWatched, list):
			self.user_watched = newWatched

	@reviews.setter
	def reviews(self, newReviews):
		if isinstance(newReviews, list):
			self.user_reviews = newReviews

	@watchlist.setter
	def watchlist(self, newWatchlist):
		self.user_watchlist = newWatchlist

	@comments.setter
	def comments(self, newComments):
		if isinstance(newComments, list):
			self.user_comments = newComments

	@time_spent_watching_movies_minutes.setter
	def time_spent_watching_movies_minutes(self, newTimeWatching):
		if isinstance(newTimeWatching, int):
			self.user_timewatching = newTimeWatching

	def watch_movie(self, movie):
		if not movie in self.user_watched:
			self.user_watched.append(movie)
		self.user_timewatching += movie.runtime_minutes
		if movie in self.user_watchlist:
			self.user_watchlist.remove_movie(movie)

	def add_review(self, review):
		self.user_reviews.append(review)

	def remove_review(self, review):
		self.user_reviews.remove(review)


if __name__ == "__main__":
	from domainmodel.movie import Movie
	from domainmodel.review import Review