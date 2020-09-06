from flask import Flask, request

app = Flask(__name__)

# UPDATE PATHS TO MATCH `ACTION` ATTRIBUTES IN `FORM` TAGS

@app.route('/<SearchQuery><SearchType>')
def search_movies(SearchQuery, SearchType):
	pass

@app.route('/<LoginUsername><LoginPassword>')
def login(LoginUsername, LoginPassword):
	pass

@app.route('/<RegUsername><RegPassword1><RegPassword2>')
def register(RegUsername, RegPassword1, RegPassword2):
	pass

@app.route('/')
def logout(SearchQuery, SearchType):
	pass

if __name__ == "__main__":
	app.run(host='localhost', port=5000)