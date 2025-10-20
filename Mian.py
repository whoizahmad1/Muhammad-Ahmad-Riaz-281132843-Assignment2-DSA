from Movieslist import MovieList

def main():
    db = MovieList()
    db.load_from_file("movies.txt")

    db.add_movie("Titanic", 1997, 195)
    db.add_movie("Alien", 1979, 117)
    db.add_movie("Platoon", 1986, 120)

    db.print_movies()

    db.find_movie("Alien")

    db.delete_movie("Titanic")
    db.print_movies()

    db.save_to_file("movies.txt")


main()