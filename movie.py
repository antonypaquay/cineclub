import os
import json
import logging

logging.basicConfig(level=logging.WARNING)

CUR_DIR = os.path.dirname(__file__)
DATA_FILE = os.path.join(CUR_DIR, "data", "movies.json")


def get_all_movies():

    with open(DATA_FILE, "r") as file:
        movies_title = json.load(file)

    movies = [Movie(movie_title) for movie_title in movies_title]
    return movies


class Movie:
    def __init__(self, title: str):
        self.title = title.title()

    def __str__(self):
        return self.title

    def _get_movies(self):
        with open(DATA_FILE, "r") as file:
            return json.load(file)

    def _write_movies(self, movies):
        with open(DATA_FILE, "w") as file:
            json.dump(movies, file, indent=4)

    def add_to_movies(self):
        movies = self._get_movies()
        if not self.title in movies:
            movies.append(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f"Le film {self.title} est déjà dans la liste.")
            return False

    def remove_to_movies(self):
        movies = self._get_movies()
        if self.title in movies:
            movies.remove(self.title)
            self._write_movies(movies)
            return True
        else:
            logging.warning(f"Le film {self.title} n'existe pas dans la liste.")
            return False

    def remove_all_movies(self):
        movies = self._get_movies()
        movies = []
        self._write_movies(movies)
        return True


if __name__ == "__main__":
    movie = Movie("Dikkenek")
    print(movie.add_to_movies())
