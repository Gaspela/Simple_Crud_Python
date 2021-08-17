from services.list_movie import ListMovie
from main.movie import Movie


tmp = None
while tmp != 4:
    try:
        print("Option: ")
        print("1. Add Movie")
        print("2. To list Movie")
        print("3. Delete Movie")
        print("4. Quit")
        tmp = int(input("Select option: "))
        if tmp < 0:
            tmp = None
            print("An error occurred", tmp)

        if tmp == 1:
            name_movie = input("Name movie: ")
            movie = Movie(name_movie)
            list_Movie = ListMovie()
            ListMovie.add_movie(movie)
        elif tmp == 2:
            ListMovie.lists_movie()
        elif tmp == 3:
            ListMovie.del_movie()

    except Exception as error:
        print(f"An error occurred: {error}")
        tmp = None
else:
    print("Finished Section")
