class Film:
    def __init__(self, title, year, genre, num_of_plays):
        self.title = title
        self.year = year
        self.genre = genre
        self.num_of_plays = num_of_plays
        
        #Variables
        self._current_num_of_plays = 0
        
    def __str__(self):
        return f"{self.title} {self.year}"
        
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
    def __init__(self, episode_number, sezon_number, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_number = episode_number
        self.sezon_number = sezon_number
        super().play()
        
    def __str__(self):
        return f'{self.title}, SE{self.sezon_number:02d}{self.episode_number:02d}'
    
film1 = Film(title = "Django", year = 2012, genre = "western", num_of_plays= 20)
serial1 = Serial(title= "Friends", year = 1994, genre = "comedy", num_of_plays = 100, sezon_number= 1, episode_number=5)

film1.current_num_of_plays = 21

print(film1)
print(serial1)
# film1.play()
# print(f"Number of plays: {film1.current_num_of_plays}")
# film1.play()
# print(f"Number of plays this film: {film1.current_num_of_plays}")

# serial1.play()
# print(f"Number of plays this serial: {serial1.current_num_of_plays}")