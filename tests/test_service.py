from pytemplate.domain.models import Movie
from pytemplate.service.tickets import buy_ticket_for_children, buy_ticket_for_teens


def test_buy_ticket_for_children_under_age():
    movie = Movie(name="Elemental", customer_age=5)
    result = buy_ticket_for_children(movie)
    assert result == "Sorry, you are not old enough to watch Elemental!"


def test_buy_ticket_for_children_appropriate_age():
    movie = Movie(name="Elemental", customer_age=6)
    result = buy_ticket_for_children(movie)
    assert result == "You are allowed to watch Elemental!"


def test_buy_ticket_for_children_over_age():
    movie = Movie(name="Elemental", customer_age=10)
    result = buy_ticket_for_children(movie)
    assert result == "You are allowed to watch Elemental!"


def test_buy_ticket_for_teens_under_age():
    movie = Movie(name="Elemental", customer_age=12)
    result = buy_ticket_for_teens(movie)
    assert result == "Sorry, you are not old enough to watch Elemental!"


def test_buy_ticket_for_teens_appropriate_age():
    movie = Movie(name="Elemental", customer_age=15)
    result = buy_ticket_for_teens(movie)
    assert result == "You are allowed to watch Elemental!"


def test_buy_ticket_for_teens_over_age():
    movie = Movie(name="Elemental", customer_age=13)
    result = buy_ticket_for_teens(movie)
    assert result == "You are allowed to watch Elemental!"
