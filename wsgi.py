from flask import Flask, request, render_template
from repository.memory_repo import MemoryRepo

app = Flask(__name__)
repo = MemoryRepo('datafiles/Data1000Movies.csv')
allMovies = repo.movies
allActors = repo.actors
allDirectors = repo.directors
allGenres = repo.genres

# UPDATE PATHS TO MATCH `ACTION` ATTRIBUTES IN `FORM` TAGS


@app.route('/')
def index():
	return render_template('index.html', movies=allMovies, actors=allActors, directors=allDirectors, genres=allGenres)


if __name__ == "__main__":
	app.run(host='localhost', port=5000, debug=True)