from pytemplate.domain.models import movie_factory
from pytemplate.service.tickets import buy_ticket_for_children, buy_ticket_for_teens


def main():
    movie_name = input("Enter the movie name: ")
    customer_age = int(input("Enter your age: "))
    age_limit = int(input("Enter the age limit for the movie (6/13): "))

    movie = movie_factory(movie_name, customer_age)

    if age_limit == 6:
        result = buy_ticket_for_children(movie)
    elif age_limit == 13:
        result = buy_ticket_for_teens(movie)
    else:
        print("Invalid age limit! Please enter 6 or 13 for the age limit")
        return

    print(result)
