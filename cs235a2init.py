from datafilereaders.movie_file_csv_reader import MovieFileCSVReader
from domainmodel.movie import TestMovie

def main():
    filename = 'datafiles/Data1000Movies.csv'
    movie_file_reader = MovieFileCSVReader(filename)
    movie_file_reader.read_csv_file()

    movie = movie_file_reader.dataset_of_movies[0]
    movieTest = TestMovie()
    print(movieTest.test_print_all(movie))


if __name__ == "__main__":
    main()