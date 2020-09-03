from datetime import datetime

from domainmodel.user import User

class Review:
	def __init__(self, revUser, revMovie, revText, revRating):
		self.review_user = revUser if isinstance(revUser, User) else None
		self.review_movie = revMovie if isinstance(revMovie, Movie) else None
		self.review_text = revText.strip() if isinstance(revText, str) else None
		self.review_rating = revRating if (isinstance(revRating, int) and (revRating in range (1,11))) else None
		self.review_timestamp = datetime.datetime.now()

	def __repr__(self):
		return f"<Review {self.review_movie}, {self.review_rating}, {self.review_timestamp}, '{self.review_text}'>"

	def __eq__(self, other):
		return self.review_movie == other.revMovie and self.review_text == other.revText and self.review_rating == other.revRating and self.review_timestamp == other.revTimestamp

	@property
	def movie(self):
		return self.review_movie

	@property
	def review_text(self):
		return self.review_text

	@property
	def rating(self):
		return self.review_rating

	@property
	def timestamp(self):
		return self.review_timestamp

	@property
	def user(self):
		return self.review_user

	@movie.setter
	def movie(self, newMovie):
		if isinstance(newMovie, Movie):
			self.review_movie = newMovie
	
	@review_text.setter
	def review_text(self, newText):
		if isinstance(newText, str):
			self.review_text = newText.strip()

	@rating.setter
	def rating(self, newRating):
		if isinstance(newRating, int) and newRating in range(1, 11):
			self.review_text = newRating

	@timestamp.setter
	def timestamp(self, newTimestamp):
		if isinstance(newTimestamp, datetime.datetime):
			self.review_timestamp = newTimestamp

	@user.setter
	def user(self, newUser):
		if isinstance(newUser, User):
			self.review_user = newUser