import os


class ListMovie:
    rute = "movie.txt"

    @classmethod
    def add_movie(cls, movie):
        with open(cls.rute, "a", encoding="utf8") as file:
            file.write(f"{movie.name}\n")

    @classmethod
    def lists_movie(cls):
        with open(cls.rute, "r", encoding="utf8") as file:
            print("List of movie". center(50, "-"))
            print(file.read())

    @classmethod
    def del_movie(cls):
        os.remove(cls.rute)
        print(f"Delete file: {cls.rute}")
