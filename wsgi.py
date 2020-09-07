from flask import Flask, request
from datafilereaders.movie_file_csv_reader import MovieFileCSVReader
from repository.memory_repo import MemoryRepo

app = Flask(__name__)
repo = MemoryRepo('datafiles/Data1000Movies.csv')
repo.read_csv_file()

# UPDATE PATHS TO MATCH `ACTION` ATTRIBUTES IN `FORM` TAGS

@app.route('/')
def index():
	return request.args.to_dict()

if __name__ == "__main__":
	app.run(host='localhost', port=5000)