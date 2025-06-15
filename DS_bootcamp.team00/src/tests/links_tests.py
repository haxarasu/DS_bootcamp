import pytest
from classes.links import Links

data_file = "ml-latest-small/links.csv"

@pytest.fixture
def instance_links():
    return Links(data_file)

def test_get_imdb(instance_links):
    result = instance_links.get_imdb(["1", "2", "3"], ["title", "imdbId"])

    assert isinstance(result, list)
    assert all(isinstance(entry, list) for entry in result)
    assert all(isinstance(entry[0], str) for entry in result)

    movie_ids = [entry[0] for entry in result]
    assert movie_ids == sorted(movie_ids, reverse=True)


def test_most_expensive(instance_links):
    result = instance_links.most_expensive(10)

    assert isinstance(result, dict)
    assert all(isinstance(title, str) for title in result.keys())
    assert all(isinstance(budget, int) for budget in result.values())

    budgets = list(result.values())
    assert budgets == sorted(budgets, reverse=True)


def test_top_directors(instance_links):
    result = instance_links.top_directors(10)

    assert isinstance(result, dict)
    assert all(isinstance(director, str) for director in result.keys())
    assert all(isinstance(count, int) for count in result.values())

    counts = list(result.values())
    assert counts == sorted(counts, reverse=True)


def test_most_profitable(instance_links):
    result = instance_links.most_profitable(10)

    assert isinstance(result, dict)
    assert all(isinstance(title, str) for title in result.keys())
    assert all(isinstance(profit, int) for profit in result.values())

    profits = list(result.values())
    assert profits == sorted(profits, reverse=True)


def test_longest(instance_links):
    result = instance_links.longest(10)

    assert isinstance(result, dict)
    assert all(isinstance(title, str) for title in result.keys())
    assert all(isinstance(runtime, int) for runtime in result.values())

    runtimes = list(result.values())
    assert runtimes == sorted(runtimes, reverse=True)


def test_cost_per_minute(instance_links):
    result = instance_links.cost_per_minute(10)

    assert isinstance(result, dict)
    assert all(isinstance(title, str) for title in result.keys())
    assert all(isinstance(cost, float) for cost in result.values())

    costs = list(result.values())
    assert costs == sorted(costs, reverse=True)