import pytest
from classes.tags import Tags

data_file = "../../ml-latest-small/tags.csv"

@pytest.fixture
def instance_tags():
    return Tags(data_file)


def test_most_words(instance_tags):
    result = instance_tags.most_words(10)

    assert isinstance(result, dict)
    assert all(isinstance(key, str) for key in result.keys())
    assert all(isinstance(value, int) for value in result.values())
    assert list(result.values()) == sorted(result.values(), reverse=True)


def test_longest(instance_tags):
    result = instance_tags.longest(10)

    assert isinstance(result, list)
    assert all(isinstance(word, str) for word in result)
    assert result == sorted(result, key=len, reverse=True)


def test_most_words_and_longest(instance_tags):
    result = instance_tags.most_words_and_longest(10)

    assert isinstance(result, list)
    assert all(isinstance(word, str) for word in result)


def test_most_popular(instance_tags):
    result = instance_tags.most_popular(10)

    assert isinstance(result, dict)
    assert all(isinstance(key, str) for key in result.keys())
    assert all(isinstance(value, int) for value in result.values())
    assert list(result.values()) == sorted(result.values(), reverse=True)


def test_tags_with(instance_tags):
    result = instance_tags.tags_with("love")

    assert isinstance(result, list)
    assert all(isinstance(tag, str) for tag in result)
    assert result == sorted(result)