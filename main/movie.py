class Movie:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return (f"Movie: {self.name}")

    @property
    def name(selft):
        return selft.name

    @name.setter
    def name(self, name):
        self.name = name
