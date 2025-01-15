import random

class Movie:
    def __init__(self, title, year, genre, num_of_plays):
        self.title = title
        self.year = year
        self.genre = genre
        self.num_of_plays = num_of_plays
        
        #Variables
        self._current_num_of_plays = self.num_of_plays
        
    def __str__(self):
        return f"{self.title} {self.year}, "
        
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
          return [i.title for i in self.library if type(i) == Movie]      
    
    def get_series(self):
          return [i.title for i in self.library if type(i) == Series]
        
    def search():
        pass
    
    def run_gen_views(func):
        def wrapper(*args, **kwargs):
            for i in range(10):
                func(*args, **kwargs)
        return wrapper
    
    @run_gen_views
    def generate_views(self):
        v = random.choice(self.library)
        v.num_of_plays = random.randint(1, 101)
        return f'{v} num_of_plays: {v.num_of_plays}'

    def top_titles(self):
        top3 = sorted(i.num_of_plays for i in library)
        return top3[::-1]

f1 = Movie("Kiler" , 2005 , "comedy" , 0)
f2 = Movie("Django", 2012, "western", 20)
s1 = Series("Friends", 1994, "comedy", 99, 1, 5)
s2 = Series("Friends", 1994, "comedy", 100, 4, 15)

library = [f2, f1, s1, s2]
for i in library:
    print(i)

l = Library()
print(l.add(f1))
print(l.get_movies())
print(l.get_series())
print(l.generate_views())
print(l.top_titles())
# print(l.run_gen_views())
# z = l.add(f1)
# print(z)

# film1.play()
# print(f"{film1.num_of_plays}")
# film1.current_num_of_plays = 21
# print(f"Number of plays: {film1.current_num_of_plays}")

# serial1.play()
# print(f"Number of plays this serial: {serial1.current_num_of_plays}")