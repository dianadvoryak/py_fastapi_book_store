import pytest

from src.category.models import Category


@pytest.fixture
def category():
    categories = [
        Category(name="Android", slug="android"),
        Category(name="Ios", slug="ios")
    ]
    return categories
    # return Category(name="Android", slug="android")
    # Ios = Category(name="Ios", slug="ios")
    # db.add(Android)
    # db.add(Ios)
    # db.commit()
    # print(tom.id)


def test_fixture(category):
    assert category.name == "Android"