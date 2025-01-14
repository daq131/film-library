class Film:
    def __init__(self, title, year, genre, num_of_plays):
        self.title = title,
        self.year = year,
        self.genre = genre,
        self.num_of_plays = num_of_plays
        
        #Variables
        self._current_num_of_plays = 0
        
    def __str__(self):
        return f"{self.title} {self.year}, {self.genre}, {self.num_of_plays}"
        
    def play(self, play = 1):
        self.current_num_of_plays += play
    
    @property
    def current_num_of_plays(self):
        return self._current_num_of_plays
    
    @current_num_of_plays.setter
    def current_num_of_plays(self, value):
        if value > self.num_of_plays:
            self._current_num_of_plays = value
        else:
            ValueError(f"Value {value} is lower then {self.num_of_plays}")
        
class Serial(Film):
    def __init__(self, episod_number, sezon_number, *args, **kwargs):
        super().__init__(*args, **kwargs),
        self.episod_number = episod_number,
        self.sezon_number = sezon_number
        super().play()
    
film1 = Film(title = "Django", year = 2012, genre = "western", num_of_plays= 20)
serial1 = Serial(title="Friends", year = 1994, genre = "comedy", num_of_plays = 100, episod_number="1", sezon_number= "1")

film1.current_num_of_plays = 21
print(film1.current_num_of_plays)

# print(film1)
# film1.play()
# print(f"Number of plays: {film1.current_num_of_plays}")
# film1.play()
# print(f"Number of plays this film: {film1.current_num_of_plays}")

# serial1.play()
# print(f"Number of plays this serial: {serial1.current_num_of_plays}")