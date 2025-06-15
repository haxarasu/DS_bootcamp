import csv
import re
from collections import Counter

class Movies:
    def __init__(self, path_to_the_file):
        with open(path_to_the_file, "r") as file:
            read = csv.DictReader(file)
            self.data = [row for row in read]


    def dist_by_release(self):
        years = []

        for row in self.data:
            title = row["title"]
            match = re.search(r'\((\d{4})\)', title)
            if match:
                years.append(int(match.group(1)))
        
        years = Counter(years)
        
        release_years = dict(years.most_common())
        
        return release_years
    

    def dist_by_genres(self):
        genres = []

        for row in self.data:
            if "|" in row["genres"]:
                genres.extend(row["genres"].split("|"))  
            else:
                genres.append(row["genres"]) 
        
        genre_counts = Counter(genres)
        sorted_genres = dict(genre_counts.most_common())  

        return sorted_genres
        

    def most_genres(self, n):
        movies = []

        for row in self.data:
            if "|" in row["genres"]:
                genres_number = len(row["genres"].split("|"))
                movies.append((row["title"], genres_number))
            else:
                movies.append((row["title"], 1))
        
        movies = dict(sorted(movies, key=lambda x: x[1], reverse=True)[:n])

        return movies