import pytest 
from classes.movies import Movies

data_file = "../../ml-latest-small/movies.csv"

@pytest.fixture
def instance_movies():
    return Movies(data_file)


def test_dist_by_release(instance_movies):
    result = instance_movies.dist_by_release()

    assert isinstance(result, dict)
    assert all(isinstance(key, int) for key in result.keys())
    assert all(isinstance(value, int) for value in result.values())
    assert list(result.values()) == sorted(result.values(), reverse=True)


def test_dist_by_genres(instance_movies):
    result = instance_movies.dist_by_genres()

    assert isinstance(result, dict)
    assert all(isinstance(key, str) for key in result.keys())
    assert all(isinstance(value, int) for value in result.values())
    assert list(result.values()) == sorted(result.values(), reverse=True)


def test_most_genres(instance_movies):
    result = instance_movies.most_genres(10)

    assert isinstance(result, dict)
    assert all(isinstance(key, str) for key in result.keys())
    assert all(isinstance(value, int) for value in result.values())
    assert list(result.values()) == sorted(result.values(), reverse=True)