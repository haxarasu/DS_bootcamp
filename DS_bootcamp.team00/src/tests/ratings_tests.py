import pytest
from classes.ratings import Ratings

data_file = "../../ml-latest-small/ratings.csv"

@pytest.fixture
def instance_ratings():
    return Ratings(data_file)


@pytest.fixture
def instance_users_ratings(instance_ratings):
    return instance_ratings.users


def test_dist_by_year(instance_ratings):
    result = instance_ratings.movies.dist_by_year()

    assert isinstance(result, dict)
    assert all(isinstance(key, int) for key in result.keys())
    assert all(isinstance(value, int) for value in result.values())
    assert list(result.keys()) == sorted(result.keys())


def test_dist_by_rating(instance_ratings):
    result = instance_ratings.movies.dist_by_rating()

    assert isinstance(result, dict)
    assert all(isinstance(key, float) for key in result.keys())
    assert all(isinstance(value, int) for value in result.values())
    assert list(result.keys()) == sorted(result.keys())


def test_top_by_num_of_ratings(instance_ratings):
    result = instance_ratings.movies.top_by_num_of_ratings(10)

    assert isinstance(result, dict)
    assert all(isinstance(key, int) for key in result.keys())
    assert all(isinstance(value, int) for value in result.values())
    assert list(result.values()) == sorted(result.values(), reverse=True)


def test_top_by_ratings(instance_ratings):
    result = instance_ratings.movies.top_by_ratings(10)

    assert isinstance(result, dict)
    assert all(isinstance(key, int) for key in result.keys())
    assert all(isinstance(value, float) for value in result.values())
    assert list(result.values()) == sorted(result.values(), reverse=True)


def test_top_controversial(instance_ratings):
    result = instance_ratings.movies.top_controversial(10)
    print(result)
    assert isinstance(result, dict)
    assert all(isinstance(key, int) for key in result.keys())
    assert all(isinstance(value, float) for value in result.values())
    assert list(result.values()) == sorted(result.values(), reverse=True)


def test_top_by_num_of_ratings_users(instance_users_ratings):
    result = instance_users_ratings.top_by_num_of_ratings(10)

    assert isinstance(result, dict)
    assert all(isinstance(key, int) for key in result.keys())
    assert all(isinstance(value, int) for value in result.values())
    assert list(result.values()) == sorted(result.values(), reverse=True)


def test_top_by_ratings_users(instance_users_ratings):
    result = instance_users_ratings.top_by_ratings(10)

    assert isinstance(result, dict)
    assert all(isinstance(key, int) for key in result.keys())
    assert all(isinstance(value, float) for value in result.values())
    assert list(result.values()) == sorted(result.values(), reverse=True)


def test_top_controversial_users(instance_users_ratings):
    result = instance_users_ratings.top_controversial(10)

    assert isinstance(result, dict)
    assert all(isinstance(key, int) for key in result.keys())
    assert all(isinstance(value, float) for value in result.values())
    assert list(result.values()) == sorted(result.values(), reverse=True)