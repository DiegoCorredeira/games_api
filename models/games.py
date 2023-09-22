

class GamesModel():

    def __init__(self, id, name, genre, plataform, year):
        self.id = id
        self.name = name
        self.genre = genre
        self.plataform = plataform
        self.year = year

    def json(self):
        return {
            'id': self.id,
            'name': self.name,
            'genre': self.genre,
            'plataform': self.plataform,
            'year': self.year
        }
