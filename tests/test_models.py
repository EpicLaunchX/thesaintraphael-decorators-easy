import pytest

from pytemplate.domain.models import Movie


def test_movie_name():
    movie_name, customer_age = "Inception", 10
    movie = Movie(name="Inception", customer_age=customer_age)
    assert movie_name == movie.name


def test_positive_customer_age():
    movie = Movie(name="Inception", customer_age=21)
    assert movie.customer_age > 0


def test_negative_age_movie_raises_value_error():
    with pytest.raises(ValueError, match="customer_age cannot be negative"):
        Movie(name="Inception", customer_age=-5)
