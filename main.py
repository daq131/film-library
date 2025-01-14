class Films:
    def __init__(self, title, year, genre, num_of_plays):
        self.title = title,
        self.year = year,
        self.genre = genre,
        self.num_of_plays = num_of_plays

class Serials(Films):
    def __init__(self, episod_number, sezon_number, *args, **kwargs):
        super().__init__(*args, **kwargs),
        self.episod_number = episod_number,
        self.sezon_number = sezon_number
    

