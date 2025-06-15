from imdb import IMDb

class IMDbScarper:
    def __init__(self):  
        self.ia = IMDb()
        self.movie_cache = {}

    def _get_movie(self, imdb_id):
        if imdb_id not in self.movie_cache:
            try:
                self.movie_cache[imdb_id] = self.ia.get_movie(imdb_id)
            except Exception as e:
                print(f"Error fetching movie {imdb_id}: {e}")
                self.movie_cache[imdb_id] = None
        return self.movie_cache[imdb_id]

    def get_directors(self, imdb_id):
        movie = self._get_movie(imdb_id)
        return [director['name'] for director in movie.get('director', [])] if movie else []

    def get_budgets(self, imdb_id):
        movie = self._get_movie(imdb_id)
        if not movie:
            return {"budget": "Unknown", "cumulative_gross": "Unknown"}

        box_office = movie.get('box office', {})
        return {
            "budget": box_office.get('Budget', 'Unknown'),
            "cumulative_gross": box_office.get('Cumulative Worldwide Gross', 'Unknown')
        }

    def get_title(self, imdb_id):
        movie = self._get_movie(imdb_id)
        return movie.get('title', 'Unknown') if movie else "Unknown"

    def get_runtime(self, imdb_id):
        movie = self._get_movie(imdb_id)
        if not movie:
            return "Unknown"

        runtime = movie.get('runtime', [])
        return str(runtime[0]) if runtime else "Unknown"
