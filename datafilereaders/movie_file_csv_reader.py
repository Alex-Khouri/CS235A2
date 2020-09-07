import csv

from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director

class MovieFileCSVReader:
	def __init__(self, file_name):
		self.file_name = file_name if isinstance(file_name, str) else None
		self.movies = list()
		self.actors = set()
		self.directors = set()
		self.genres = set()

	@property
	def dataset_of_movies(self):
		return self.movies

	@property
	def dataset_of_actors(self):
		return self.actors

	@property
	def dataset_of_directors(self):
		return self.directors

	@property
	def dataset_of_genres(self):
		return self.genres

	@dataset_of_movies.setter
	def dataset_of_movies(self, newMovies):
		if isinstance(newMovies, list):
			self.movies = newMovies

	@dataset_of_actors.setter
	def dataset_of_actors(self, newActors):
		if isinstance(newActors, set):
			self.actors = newActors

	@dataset_of_directors.setter
	def dataset_of_directors(self, newDirectors):
		if isinstance(newDirectors, set):
			self.directors = newDirectors

	@dataset_of_genres.setter
	def dataset_of_genres(self, newGenres):
		if isinstance(newGenres, set):
			self.genres = newGenres

	def read_csv_file(self):
		try:
			csvfile = open(self.file_name, encoding='utf-8-sig', newline='')
			reader = csv.DictReader(csvfile)
			for row in reader:
				try:
					movie = Movie(row['Title'].strip(), int(row['Year'].strip()))
					movie.description = row['Description']
					movie.director = Director(row['Director'])
					for actor in row['Actors'].split(","):
						movie.add_actor(Actor(actor.strip()))
					for genre in row['Genre'].split(","):
						movie.add_genre(Genre(genre.strip()))
					movie.runtime_minutes = int(row['Runtime (Minutes)'])
					movie.rating = float(row['Rating'])
					movie.votes = int(row['Votes'])
					actors = row['Actors'].split(',')
					for i in range(len(actors)):
						actors[i] = Actor(actors[i].strip())
						actors[i].add_movie(movie)
					director = Director(row['Director'].strip())
					director.add_movie(movie)
					genres = row['Genre'].split(',')
					for i in range(len(genres)):
						genres[i] = Genre(genres[i].strip())
						genres[i].add_movie(movie)
					self.movies.append(movie)
					self.actors.update(set(actors))
					self.directors.add(director)
					self.genres.update(set(genres))
				except:
					continue # Skips movies with invalid formatting
			csvfile.close()
		except:
			raise Exception("Error while reading CSV file!")