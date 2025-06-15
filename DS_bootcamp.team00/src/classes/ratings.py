import csv
from datetime import datetime
from collections import Counter, defaultdict
from statistics import mean, median, variance

class Ratings:
    def __init__(self, path_to_the_file):
        with open(path_to_the_file, 'r') as file:
            read = csv.DictReader(file)
            self.data = [row for row in read]
        self.movies = self.Movies(self.data)
        self.users = self.Users(self.data)
        
    class Movies():
        def __init__(self, data):
            self.data = data   


        def dist_by_year(self):
            years = [datetime.fromtimestamp(int(row["timestamp"])).year for row in self.data]
            return dict(sorted(Counter(years).items(), key=lambda item: item[0]))
        

        def dist_by_rating(self, key="rating"):
            ratings = [float(row[key]) for row in self.data]
            ratings_distribution = dict(sorted(Counter(ratings).items(), key=lambda item: item[0]))
            return ratings_distribution
        

        def top_by_num_of_ratings(self, n, key="movieId"):
            count = Counter(int(row[key]) for row in self.data)
            return dict(sorted(count.items(), key=lambda item: item[1], reverse=True)[:n])
        

        def top_by_ratings(self, n, metric="average", key="movieId"):
            ratings = defaultdict(list)
            for row in self.data:
                ratings[row[key]].append(float(row["rating"]))

            if metric == "average":
                result = {int(item): round(mean(vals), 2) for item, vals in ratings.items()}
            elif metric == "median":
                result = {int(item): round(median(vals), 2) for item, vals in ratings.items()}
            else:
                raise ValueError("Invalid metric! Use 'average' or 'median'.")

            return dict(sorted(result.items(), key=lambda item: item[1], reverse=True)[:n])
        

        def top_controversial(self, n, key="movieId"):
            ratings = defaultdict(list)
            for row in self.data:
                ratings[row[key]].append(float(row["rating"]))
            
            variances = {int(item): round(variance(vals), 2) for item, vals in ratings.items() if len(vals) > 1}
            return dict(sorted(variances.items(), key=lambda item: item[1], reverse=True)[:n])

    class Users(Movies):
        def __init__(self, data):
            super().__init__(data)


        def top_by_num_of_ratings(self, n):
            return super().top_by_num_of_ratings(n, key="userId")


        def top_by_ratings(self, n, metric="average"):
            return super().top_by_ratings(n, key="userId", metric=metric)


        def top_controversial(self, n):
            return super().top_controversial(n, key="userId")