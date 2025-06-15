import csv
from collections import Counter
from IMDbScarper import IMDbScarper

class Links:
    def __init__(self, filepath):  
        with open(filepath, "r") as file:
            reader = csv.DictReader(file)
            self.data = [row for row in reader]
        self.scraper = IMDbScarper()

    def _parse_number(self, value):
        return int(''.join(filter(str.isdigit, value))) if value and value != "Unknown" else 0

    def get_imdb(self, list_of_movies, list_of_fields):
        return sorted(
            [
                [film["movieId"]] + [film[field] for field in list_of_fields if field in film]
                for film in self.data if film["movieId"] in list_of_movies
            ],
            key=lambda x: x[0], reverse=True
        )

    def top_directors(self, n):
        director_count = Counter()

        for film in self.data:
            imdb_id = film['imdbId']
            directors = self.scraper.get_directors(imdb_id)
            director_count.update(directors)

        return dict(director_count.most_common(n))

    def most_expensive(self, n):
        return self._get_top_movies(n, key="budget", reverse=True)

    def most_profitable(self, n):
        return self._get_top_movies(n, key="profit", reverse=True)

    def longest(self, n):
        return self._get_top_movies(n, key="runtime", reverse=True)

    def top_cost_per_minute(self, n):
        return self._get_top_movies(n, key="cost_per_minute", reverse=True)

    def _get_top_movies(self, n, key, reverse=False):
        movie_stats = {}

        for film in self.data:
            imdb_id = film['imdbId']
            title = self.scraper.get_title(imdb_id)
            budget_info = self.scraper.get_budgets(imdb_id)
            runtime = self._parse_number(self.scraper.get_runtime(imdb_id))

            budget = self._parse_number(budget_info['budget'])
            gross = self._parse_number(budget_info['cumulative_gross'])

            if key == "budget":
                movie_stats[title] = budget
            elif key == "profit":
                movie_stats[title] = gross - budget
            elif key == "runtime":
                movie_stats[title] = runtime
            elif key == "cost_per_minute" and runtime > 0:
                movie_stats[title] = round(budget / runtime, 2)

        return dict(sorted(movie_stats.items(), key=lambda x: x[1], reverse=reverse)[:n])
    

if __name__ == "__main__":
    links = Links("../../ml-latest-small/links.csv")
    print(links.get_imdb(["1", "2", "3"], ["movieId", "imdbId"]))
