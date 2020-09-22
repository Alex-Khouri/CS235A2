from flask import Flask, request, render_template, session
from repository.memory_repo import MemoryRepo
from domainmodel.user import User

app = Flask(__name__)
app.secret_key = b'09s1nfe5m9dj4fs0'
# Flask session uses the following keys:
# 		authStatus, authMessage, currUsername
# Valid authStatus values: "logged in", "logged out", "logging in", "registering"
repo = MemoryRepo('datafiles/Data1000Movies.csv')
titleChars = ["0-9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
servData = {
	"allMovies": repo.movies,
	"allDirectors": repo.directors,
	"allActors": repo.actors,
	"allGenres": repo.genres,
	"allUsers": repo.users,
	"charLinks": [f'<a class="browse-link" href="/browse?BrowseCategory=TitleChar&BrowseQuery={char}">{char}</a>' for char in titleChars],
	"genreLinks": [f'<a class="browse-link" href="/browse?BrowseCategory=Genre&BrowseQuery={genre.name}">{genre.name}</a>' for genre in repo.genres],
	"directorLinks": [f'<a class="browse-link" href="/browse?BrowseCategory=Director&BrowseQuery={director.director_full_name}">{director.director_full_name}</a>' for director in repo.directors],
	"actorLinks": [f'<a class="browse-link" href="/browse?BrowseCategory=Actor&BrowseQuery={actor.actor_full_name}">{actor.actor_full_name}</a>' for actor in repo.actors]
}


@app.route('/')
def index():
	session["currUsername"] = session.get("currUsername")
	session["authStatus"] = session.get("authStatus", "logged out")
	session["authMessage"] = ""
	clientData = {
		"filteredMovies": repo.movies,
		"currWatchlist": None
	}
	return render_template('index.html', **servData, **clientData)

@app.route('/login')
def login():
	username = request.args.get('LoginUsername')
	password = request.args.get('LoginPassword')
	user = repo.get_user(username)
	clientData = {
		"filteredMovies": repo.movies,
		"currWatchlist": None
	}
	if user is None:
		session["authStatus"] = "logging in"
		session["authMessage"] = "Invalid username - please try again"
	elif user.password != password:
		session["authStatus"] = "logging in"
		session["authMessage"] = "Invalid password - please try again"
	else:
		session["authStatus"] = "logged in"
		session["authMessage"] = ""
		session["currUsername"] = username
		clientData["currWatchlist"] = user.watchlist
	return render_template('index.html', **servData, **clientData)

@app.route('/register')
def register():
	username = request.args.get('RegUsername').strip().lower()
	password1 = request.args.get('RegPassword1')
	password2 = request.args.get('RegPassword2')
	clientData = {
		"filteredMovies": repo.movies,
		"currWatchlist": None
	}
	if password1 != password2:
		session["authStatus"] = "registering"
		session["authMessage"] = "Passwords don't match - please try again"
	elif repo.get_user(username) is not None:
		session["authStatus"] = "registering"
		session["authMessage"] = "Username already taken - please try again"
	else:
		session["authStatus"] = "logged in"
		session["authMessage"] = ""
		session["currUsername"] = username
		user = User(username, password1)
		repo.add_user(user)
		clientData["currWatchlist"] = user.watchlist
	return render_template('index.html', **servData, **clientData)

@app.route('/logout')
def logout():
	session["currUsername"] = None
	clientData = {
		"filteredMovies": repo.movies,
		"currWatchlist": None
	}
	return render_template('index.html', **servData, **clientData)

@app.route('/browse')
def browse():
	category = request.args.get("BrowseCategory")  # i.e. TitleChar, Genre, Director, or Actor
	query = request.args.get("BrowseQuery").strip().lower()  # "0-9" if category == TitleChar
	user = repo.get_user(session["currUsername"])
	clientData = {
		"filteredMovies": list(),
		"currWatchlist": user.watchlist if user is not None else None
	}
	if query == "":  # There are no known circumstances that should trigger this
		clientData["filteredMovies"] = servData["allMovies"]
	else:
		for movie in servData["allMovies"]:
			if category == "TitleChar":
				first = movie.title.strip().lower()[0]
				if first.isalpha() and first == query or first.isdigit() and query == "0-9":
					clientData["filteredMovies"].append(movie)
			elif category == "Genre":
				for genre in movie.genres:
					if genre.name.strip().lower() == query:
						clientData["filteredMovies"].append(movie)
						break
			elif category == "Director":
				if movie.director.director_full_name.strip().lower() == query:
					clientData["filteredMovies"].append(movie)
			elif category == "Actor":
				for actor in movie.actors:
					if query in actor.actor_full_name.strip().lower().split():
						clientData["filteredMovies"].append(movie)
						break
			else:
				print("ERROR: Invalid browsing category passed from HTML")
	return render_template('index.html', **servData, **clientData)

@app.route('/search')
def search():
	category = request.args.get("SearchCategory").strip().lower()  # i.e. title, genre, director, or actor
	query = request.args.get("SearchQuery").strip().lower()
	user = repo.get_user(session["currUsername"])
	clientData = {
		"filteredMovies": list(),
		"currWatchlist": user.watchlist if user is not None else None
	}
	if query == "":
		clientData["filteredMovies"] = servData["allMovies"]
	else:
		for movie in servData["allMovies"]:
			if category == "title":
				if movie.title.strip().lower() == query:
					clientData["filteredMovies"].append(movie)
			elif category == "genre":
				for genre in movie.genres:
					if genre.name.strip().lower() == query:
						clientData["filteredMovies"].append(movie)
						break
			elif category == "director":
				if movie.director.director_full_name.strip().lower() == query:
					clientData["filteredMovies"].append(movie)
			elif category == "actor":
				for actor in movie.actors:
					if query in actor.actor_full_name.strip().lower().split():
						clientData["filteredMovies"].append(movie)
						break
			else:
				print("ERROR: Invalid search category passed from HTML")
	return render_template('index.html', **servData, **clientData)


if __name__ == "__main__":
	app.run(host='localhost', port=5000, debug=True)