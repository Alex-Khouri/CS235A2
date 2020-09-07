from flask import Flask, request, render_template
from repository.memory_repo import MemoryRepo

app = Flask(__name__)
repo = MemoryRepo('datafiles/Data1000Movies.csv')

# UPDATE PATHS TO MATCH `ACTION` ATTRIBUTES IN `FORM` TAGS

@app.route('/')
def index():
	return render_template('index.html')

if __name__ == "__main__":
	app.run(host='localhost', port=5000, debug=True)