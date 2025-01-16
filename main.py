import random
import datetime

class Movie:
    def __init__(self, title, year, genre, num_of_plays):
        self.title = title
        self.year = year
        self.genre = genre
        self.num_of_plays = num_of_plays
        
        #Variables
        self._current_num_of_plays = self.num_of_plays
        
    def __str__(self):
        return f"{self.title} ({self.year}), "
        
    def play(self):
        self.current_num_of_plays += 1
    
    @property
    def current_num_of_plays(self):
        return self._current_num_of_plays
    
    @current_num_of_plays.setter
    def current_num_of_plays(self, value):
        if value <= self.num_of_plays:
            ValueError(f"Value {value} is lower then {self.num_of_plays}")
        else:
            self._current_num_of_plays = value
        
class Series(Movie):
    def __init__(self, title, year, genre, num_of_plays, episode_number, sezon_number):
        super().__init__(title, year, genre, num_of_plays)
        self.episode_number = episode_number
        self.sezon_number = sezon_number
        super().play()
        
    def __str__(self):
        return f'{self.title} S{self.sezon_number:02d}E{self.episode_number:02d},'
  
class Library:    
    def __init__(self):
        self.library = library
        
    def __str__(self):
        return f'{self.title}'

    def add(self, object):
        self.library.append(object)
        
    def get_movies(self):
        return sorted(i.title for i in self.library if type(i) == Movie)     
    
    def get_series(self):
        return sorted(i.title for i in self.library if type(i) == Series)
        
    def search(self):
        get_title = input("Podaj poszukiwany tytuł: ")
        for i in library:               
            if get_title == i.title:
                return f'Mamy w bazie taki tytuł: {i.title}'
                break
            else:
                pass

    def generate_views(self):
        v = random.choice(self.library)
        v.num_of_plays = random.randint(1, 101)
        return f'{v.title} z num_of_plays: {v.num_of_plays}'
    
    def top_titles(self):
        by_num_of_plays = sorted(library, key=lambda movie: movie.num_of_plays)
        res = by_num_of_plays[::-1]
        for i in res:
            return i.title
 
f1 = Movie("Kiler", 2005, "comedy", 5)
f2 = Movie("Django", 2012, "western", 20)
f3 = Movie("Hobbit", 2015, "dramat", 45)
s1 = Series("Friends", 1994, "comedy", 22, 1, 5)
s2 = Series("Friends", 1994, "comedy", 100, 4, 15)
s3 = Series("Band of the Brothers", 1994, "dramat", 84, 1, 5)

print("Biblioteka filmów: ")
library = [f2, f1, f3, s1, s2, s3]
for i in library:
    print(i)

l = Library()
print(f'Losowa pozycja z biblioteki: {l.generate_views()}')
print(f'Najpopularniejsze filmy i seriale z dnia: {datetime.datetime.today().strftime('%d.%m.%Y')}:')
print(l.top_titles())
