from flask import Flask, request, render_template
from repository.memory_repo import MemoryRepo
from domainmodel.user import User

app = Flask(__name__)
repo = MemoryRepo('datafiles/Data1000Movies.csv')
servData = {
	"titleChars": ["0-9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"],
	"allMovies": repo.movies,
	"allDirectors": repo.directors,
	"allActors": repo.actors,
	"allGenres": repo.genres,
	"allUsers": repo.users,
	"currentUser": None,
	"currentWatchlist": None,
	"authMessage": "",
	"filterQuery": "",
	"filterCategory": "",  # TitleChar, Title, Genre, Director, or Actor
	"filteredMovies": repo.movies
}


@app.route('/')
def index():
	servData["filteredMovies"] = repo.movies
	return render_template('index.html', **servData)

@app.route('/login')
def login():
	username = request.args.get('LoginUsername')
	password = request.args.get('LoginPassword')
	user = repo.get_user(username)
	servData["filteredMovies"] = repo.movies
	if user is not None and password == user.password:
		servData["currentUser"] = user
		servData["currentWatchlist"] = servData["currentUser"].watchlist
		return render_template('logged_in.html', **servData)
	else:  # USE TEMPLATE TO DISPLAY FAILED LOGIN MESSAGE
		return render_template('index.html', **servData)

@app.route('/register')
def register():
	username = request.args.get('RegUsername')
	password1 = request.args.get('RegPassword1')
	password2 = request.args.get('RegPassword2')
	servData["filteredMovies"] = repo.movies
	if password1 == password2:
		servData["currentUser"] = User(username, password1)
		servData["currentWatchlist"] = servData["currentUser"].watchlist
		repo.add_user(servData["currentUser"])
		return render_template('logged_in.html', **servData)
	else:  # USE TEMPLATE TO DISPLAY FAILED REGISTRATION MESSAGE
		return render_template('index.html', **servData)

@app.route('/logout')
def logout():
	servData["currentUser"] = None
	servData["currentWatchlist"] = None
	servData["filteredMovies"] = repo.movies
	return render_template('index.html', **servData)

@app.route('/browse')
def browse():
	servData["filterQuery"] = request.args.get("BrowseQuery")
	servData["filterCategory"] = request.args.get("BrowseCategory")
	query = servData["filterQuery"]
	category = servData["filterCategory"]
	if query == "":
		servData["filteredMovies"] = servData["allMovies"]
	else:
		servData["filteredMovies"] = list()
		for movie in servData["allMovies"]:
			pass  # POPULATE USING CONDITIONAL CHECKS
	return render_template('index.html', **servData)

@app.route('/search')
def search():
	servData["filterQuery"] = request.args.get("SearchQuery")
	servData["filterCategory"] = request.args.get("SearchCategory")
	query = servData["filterQuery"]
	category = servData["filterCategory"]
	if query == "":
		servData["filteredMovies"] = servData["allMovies"]
	else:
		servData["filteredMovies"] = list()
		for movie in servData["allMovies"]:
			pass  # POPULATE USING CONDITIONAL CHECKS
	return render_template('index.html', **servData)


if __name__ == "__main__":
	app.run(host='localhost', port=5000, debug=True)