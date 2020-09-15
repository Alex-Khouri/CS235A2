from flask import Flask, request, render_template
from repository.memory_repo import MemoryRepo
from domainmodel.user import User

app = Flask(__name__)
repo = MemoryRepo('datafiles/Data1000Movies.csv')
allMovies = repo.movies
allActors = repo.actors
allDirectors = repo.directors
allGenres = repo.genres
allUsers = repo.users
currentUser = None


@app.route('/')
def index():
	return render_template('index.html', movies=allMovies, actors=allActors, directors=allDirectors, genres=allGenres)

@app.route('/login')
def login():
	username = request.args.get('LoginUsername')
	password = request.args.get('LoginPassword')
	user = repo.get_user(username)
	if user is not None and password == user.password:
		currentUser = user
		return render_template('logged_in.html', movies=allMovies, actors=allActors, directors=allDirectors, genres=allGenres)
	else:  # USE TEMPLATE TO DISPLAY FAILED LOGIN MESSAGE
		return render_template('index.html', movies=allMovies, actors=allActors, directors=allDirectors, genres=allGenres)

@app.route('/register')
def register():
	username = request.args.get('RegUsername')
	password1 = request.args.get('RegPassword1')
	password2 = request.args.get('RegPassword2')
	if password1 == password2:
		currentUser = User(username, password1)
		repo.add_user(currentUser)
		return render_template('logged_in.html', movies=allMovies, actors=allActors, directors=allDirectors, genres=allGenres)
	else:  # USE TEMPLATE TO DISPLAY FAILED LOGIN MESSAGE
		return render_template('index.html', movies=allMovies, actors=allActors, directors=allDirectors, genres=allGenres)

@app.route('/logout')
def logout():
	currentUser = None
	return render_template('index.html', movies=allMovies, actors=allActors, directors=allDirectors, genres=allGenres)


if __name__ == "__main__":
	app.run(host='localhost', port=5000, debug=True)