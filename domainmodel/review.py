from datetime import datetime

from domainmodel.movie import Movie

class Review:
	def __init__(self, revMovie, revText, revRating):
		self.revMovie = revMovie if isinstance(revMovie, Movie) else None
		self.revText = revText.strip() if isinstance(revText, str) else None
		self.revRating = revRating if (isinstance(revRating, int) and (revRating in range (1,11))) else None
		self.revTimestamp = datetime.datetime.now()

	def __repr__(self):
		return f"<Review {self.revMovie}, {self.revRating}, {self.revTimestamp}, '{self.revText}'>"

	def __eq__(self, other):
		return (self.revMovie == other.revMovie and self.revText == other.revText and self.revRating == other.revRating and self.revTimestamp == other.revTimestamp)

	@property
	def movie(self):
		return self.revMovie

	@property
	def review_text(self):
		return self.revText

	@property
	def rating(self):
		return self.revRating

	@property
	def timestamp(self):
		return self.revTimestamp

	@movie.setter
	def movie(self, newMovie):
		if (isinstance(newMovie, Movie)):
			self.revMovie = newMovie
	
	@review_text.setter
	def review_text(self, newText):
		if (isinstance(newText, str)):
			self.revText = newText.strip()

	@rating.setter
	def rating(self, newRating):
		if (isinstance(newRating, int) and newRating in range(1,11)):
			self.revText = newRating

	@timestamp.setter
	def timestamp(self, newTimestamp):
		if (isinstance(newTimestamp, datetime.datetime)):
			self.revTimestamp = newTimestamp